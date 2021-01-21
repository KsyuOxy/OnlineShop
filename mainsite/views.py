from django.shortcuts import render, redirect
from products.models import Product
from categories.models import Category
from subcategories.models import Subcategory
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse


# Create your views here.
def index(request):
    data = dict()

    all_products = Product.objects.all
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories

    subcategories_lash = all_subcategories.filter(category__name='Lash')
    subcategories_brow = all_subcategories.filter(category__name='Brow')
    print(subcategories_lash)
    print(subcategories_brow)

    best_sale_lash = Product.objects.filter(subcategory__id__in=subcategories_lash, in_stock=True).order_by('-count_of_sold')
    best_sale_brow = Product.objects.filter(subcategory__id__in=subcategories_brow, in_stock=True).order_by('-count_of_sold')
    print(best_sale_lash)
    print(best_sale_brow)

    data['best_sale_lash'] = best_sale_lash
    data['best_sale_brow'] = best_sale_brow

    return render(request, 'mainsite/index.html', context=data)


def products(request):
    data = dict()

    filtered_subcategories = request.GET.getlist('sub')
    filtered_subcategories = list(map(int, filtered_subcategories))

    all_products = Product.objects.all()
    print(all_products)
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories
    data['filtered_subcategories'] = filtered_subcategories

    if filtered_subcategories:
        filtered_products = Product.objects.filter(subcategory__id__in=filtered_subcategories)
        data['filtered_products'] = filtered_products
        return render(request, 'mainsite/filtered_sidebar.html', context=data)
    return render(request, 'mainsite/products.html', context=data)


def filtered_sidebar(request):
    data = dict()

    filtered_subcategories = request.GET.getlist('sub')
    filtered_subcategories = list(map(int, filtered_subcategories))

    filtered_products = Product.objects.filter(subcategory__id__in=filtered_subcategories)

    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['filtered_products'] = filtered_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories
    data['filtered_subcategories'] = filtered_subcategories

    # Filter by Price -----------------------------------------------------------------
    filtered_prices = request.GET.getlist('price')
    filtered_prices = list(map(float, filtered_prices))
    data['filtered_prices'] = filtered_prices
    print('try', filtered_prices)

    if filtered_prices:
        price_first = request.GET.getlist('price')[0]
        data['price_first'] = float(price_first)
        price_last = request.GET.getlist('price')[1]
        data['price_last'] = float(price_last)
        print('from', data['price_first'], 'to', data['price_last'])
        return render(request, 'mainsite/filter_product_params.html', context=data)

    return render(request, 'mainsite/filtered_sidebar.html', context=data)


def details_product(request, slug):
    try:
        data = dict()
        product = Product.objects.get(slug=slug)
        data['product'] = product
        return render(request, 'mainsite/product-details-sticky-right.html', context=data)

    except ObjectDoesNotExist:
        raise Http404


def log_reg(request):
    return render(request, 'account/login-register.html')


def ajax_reg(request) -> JsonResponse:
    response = dict()
    _login = request.GET.get('login_field')
    try:
        User.objects.get(username=_login)
        response['message_login'] = 'занят'
    except User.DoesNotExist:
        response['message_login'] = 'свободен'

    return JsonResponse(response)


def sign_in(request):
    data = {}
    if request.method == "GET":
        if request.user.is_authenticated:
            data['report'] = 'User is already authenticated'
            return render(request, 'mainsite/index.html', context=data)
        return render(request, 'account/login-register.html')

    elif request.method == "POST":
        _login = request.POST.get('login_field')
        _password = request.POST.get('password_field')
        user = authenticate(request, username=_login, password=_password)

        if user is None:
            data['report'] = 'User not found or wrong password'
            return render(request, 'account/login-register.html', context=data)
        else:
            data['report'] = 'You have successfully authenticated'
            login(request, user)
            return render(request, 'mainsite/index.html', context=data)


def ajax_log_passwd(request) -> JsonResponse:
    response = dict()

    _login = request.GET.get('login_field')
    _password = request.GET.get('password_field')

    user = authenticate(request, username=_login, password=_password)
    if user is not None:
        response['message_user'] = 'ok'
        # login(request, user)
        return JsonResponse(response)
    else:
        response['message_user'] = 'error'
        return JsonResponse(response)


def register(request):
    data = dict()
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'account/login-register.html', context={})

    elif request.method == "POST":
        login = request.POST.get('login_field_reg')
        email = request.POST.get('email_field_reg')
        passwd1 = request.POST.get('password_field_reg')
        passwd2 = request.POST.get('password_confirmation_field')

        data['login'] = login
        data['email'] = email
        data['passwd1'] = passwd1
        data['passwd2'] = passwd2

        if passwd1 != passwd2:
            report = 'Passwords must match'
        elif '' in data.values():
            report = 'All fields are required'
        elif len(passwd1) < 8:
            report = 'The password is too short'
        else:
            user = User.objects.create_user(login, email, passwd1)
            user.save()
            if user:
                data['report'] = 'You have successfully registered'
                return render(request, 'mainsite/index.html', context=data)
            report = 'Oops! Something wrong.'
        data['report'] = report
        return render(request, 'account/login-register.html', context=data)


def logout_user(request):
    logout(request)
    return redirect('/home_page')
