from django.contrib import admin
from .models import Category, Customer, MealType, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'email', 'created_at', 'updated_at',)

@admin.register(MealType)
class MealTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'description', 'is_sale', 'sale_price', 'created_at', 'updated_at',)
    list_filter = ('is_sale',)