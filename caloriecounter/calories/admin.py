from django.contrib import admin

from .models import Products, EatType, UserCalorieHistory


class ProductAdminConfig(admin.ModelAdmin):
    list_display = ('name', 'fats', 'calories', 'proteins', 'carbohydrates')


class UserCalorieHistoryAdminConfig(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'type', 'pub_date')


admin.site.register(Products, ProductAdminConfig)
admin.site.register(EatType)
admin.site.register(UserCalorieHistory, UserCalorieHistoryAdminConfig)
