from django.shortcuts import render
from categories.models import Category
from subcategories.models import Subcategory
from .models import Product


def product_details(request, product_id):
    data = dict()

    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories
    return render(request, 'mainsite/product-details-sticky-right.html', context=data)
