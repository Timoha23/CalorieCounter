from django.contrib import admin

from .models import Products, EatType


class ProductAdminConfig(admin.ModelAdmin):
    list_display = ('name', 'fats', 'calories', 'proteins', 'carbohydrates')


admin.site.register(Products, ProductAdminConfig)
admin.site.register(EatType)
