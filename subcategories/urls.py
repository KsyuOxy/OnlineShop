from django.urls import path, include
from .views import subcategory
from mainsite.views import index


urlpatterns = [
    path('sub=<int:subcategory_id>/', subcategory, name='subcategory'),
    path('', include('products.urls')),
]
