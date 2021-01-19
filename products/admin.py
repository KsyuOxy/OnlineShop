from django.contrib import admin
from .models import Product


class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory', 'in_stock', 'price', 'discount', 'discount_price', 'date_last_sale']
    list_display_links = ['subcategory']
    list_editable = ['name', 'price', 'discount_price']

    list_filter = ['subcategory', 'in_stock', 'discount']
    search_fields = ['name', 'price']

    class Meta:
        model = Product


admin.site.register(Product, ProductModelAdmin)
