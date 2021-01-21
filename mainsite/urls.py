from django.urls import path, include
from .views import index, products, filtered_sidebar, details_product, log_reg, register, ajax_log_passwd, ajax_reg, sign_in, logout_user


urlpatterns = [
    path('', index, name='home_page'),
    path('log_reg', log_reg, name='log_reg'),
    path('products/', products, name='products'),
    path('<slug:slug>/details', details_product, name='details_product'),
    path('filtered/', index, name='filtered'),
    path('filtered_sidebar/', filtered_sidebar, name='filtered_sidebar'),
    path('', include('subcategories.urls')),
    path('', include('categories.urls')),
    path('register', register, name='register'),
    path('ajax_reg', ajax_reg, name='ajax_reg'),
    path('ajax_log_passwd', ajax_log_passwd, name='ajax_log_passwd'),
    path('login', sign_in, name='login'),
    path('logout', logout_user, name='logout'),
]
