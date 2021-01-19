from django.urls import path, include
from .views import index, products, filtered_sidebar, details_product


urlpatterns = [
    path('', index, name='home_page'),
    path('products/', products, name='products'),
    path('<slug:slug>/details', details_product, name='details_product'),
    path('filtered/', index, name='filtered'),
    path('filtered_sidebar/', filtered_sidebar, name='filtered_sidebar'),
    path('', include('subcategories.urls')),
    path('', include('categories.urls')),
]
