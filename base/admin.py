from django.contrib import admin
from .models import Product
# Register your models here.
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ('name', 'price', 'stock', 'description')  # Add the fields you want to display
admin.site.register(Product)