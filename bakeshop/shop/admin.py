from django.contrib import admin
from .models import Category, Customer, MealType, Product

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(MealType)
admin.site.register(Product)