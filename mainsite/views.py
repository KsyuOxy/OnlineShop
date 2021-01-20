from django.shortcuts import render
from products.models import Product
from categories.models import Category
from subcategories.models import Subcategory
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404, JsonResponse


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




