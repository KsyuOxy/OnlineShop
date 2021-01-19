from django.shortcuts import render
from .models import Subcategory
from categories.models import Category
from products.models import Product


def subcategory(request, subcategory_id):
    data = dict()

    all_products = Product.objects.all()
    all_categories = Category.objects.all()
    all_subcategories = Subcategory.objects.all()

    data['products'] = all_products
    data['categories'] = all_categories
    data['subcategories'] = all_subcategories

    subcategory_products = Subcategory.objects.get(id=subcategory_id)
    data['subcategory_products'] = subcategory_products

    return render(request, 'subcategories/subcategory.html', context=data)



