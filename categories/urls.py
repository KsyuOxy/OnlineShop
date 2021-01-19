from django.urls import path, include
from .views import category, filter_product_params


urlpatterns = [
    path('products/cat=<int:category_id>/', category, name='category'),
    path('filter_product_params', filter_product_params, name='filter_product_params'),
    path('', include('subcategories.urls')),
    path('', include('products.urls')),
]
