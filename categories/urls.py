from django.urls import path, include
from .views import category, filter_product_params, filter_products_by_color


urlpatterns = [
    path('products/cat=<int:category_id>/', category, name='category'),
    path('filter_product_params', filter_product_params, name='filter_product_params'),
    path('filter_products_by_color', filter_products_by_color, name='filter_products_by_color'),
    path('', include('subcategories.urls')),
    path('', include('products.urls')),
]
