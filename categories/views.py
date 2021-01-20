from django.shortcuts import render, redirect
from .models import Category
from subcategories.models import Subcategory
from products.models import Product


# filtered by subcategories, price, color
def category(request, category_id):
    data = dict()

    # gets the selected category
    category_sub = Category.objects.get(id=category_id)   # selected category
    data['category_sub'] = category_sub

    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories

    # Filter by Color  -----------------------------------------------------------------
    color_categories = []

    color_of_products = request.GET.getlist('color')
    data['color_of_products'] = color_of_products
    products_by_color = []

    for product in all_products:
        if product.color.lower() not in color_categories:
            color_categories.append(product.color.lower())
        if product.color.lower() in color_of_products:
            products_by_color.append(product)

    data['color_categories'] = color_categories
    data['products_by_color'] = products_by_color

    if color_of_products:
        return render(request, 'categories/filter_products_by_color.html', context=data)

    # Filter by Subcategories ----------------------------------------------------------
    filtered_subcategories = request.GET.getlist('sub')    # gets filtered subcategories
    filtered_subcategories = list(map(int, filtered_subcategories))

    # products of filtered subcategories
    filtered_products = Product.objects.filter(subcategory__id__in=filtered_subcategories)

    data['filtered_products'] = filtered_products
    data['filtered_subcategories'] = filtered_subcategories

    if filtered_subcategories:
        return render(request, 'mainsite/filtered_sidebar.html', context=data)

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
        return render(request, 'categories/filter_product_params.html', context=data)

    return render(request, 'categories/category.html', context=data)


def filter_product_params(request):
    data = dict()
    all_products = Product.objects.all()
    data['products'] = all_products

    filtered_prices = request.GET.getlist('price')
    filtered_prices = list(map(float, filtered_prices))
    data['filtered_prices'] = filtered_prices

    print(filtered_prices, 'params')

    price_first = request.GET.getlist('price')[0]
    data['price_first'] = float(price_first)
    price_last = request.GET.getlist('price')[1]
    data['price_last'] = float(price_last)
    print('from', data['price_first'], 'to', data['price_last'])

    return render(request, 'categories/filter_product_params.html', context=data)


# Filter by Color  -----------------------------------------------------------------
def filter_products_by_color(request):
    data = dict()

    color_of_products = request.GET.get('color')
    data['color_of_products'] = color_of_products

    all_products = Product.objects.all()
    data['products'] = all_products

    color_categories = []
    products_by_color = dict()

    for product in all_products:
        if product.color.lower() not in color_categories:
            color_categories.append(product.color.lower())
            products_by_color.update({product.color: []})
        products_by_color[f'{product.color}'].append(product)

    data['color_categories'] = color_categories
    data['products_by_color'] = products_by_color
    return render(request, 'categories/filter_products_by_color.html', context=data)




