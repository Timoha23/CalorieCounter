from django.contrib import admin

from .models import (Products, EatType, UserAddCalorieHistory,
                     SportsExercises, UserRemoveCalorieHistory)


class ProductAdminConfig(admin.ModelAdmin):
    list_display = ('name', 'fats', 'calories', 'proteins', 'carbohydrates')


class UserCalorieHistoryAdminConfig(admin.ModelAdmin):
    list_display = ('user', 'product', 'amount', 'type', 'pub_date')


class SportsExercisesAdminConfig(admin.ModelAdmin):
    list_display = ('name', 'calories_count')


class UserRemoveCalorieHistoryAdminConfig(admin.ModelAdmin):
    list_display = ('user', 'type', 'minutes', 'pub_date')


admin.site.register(Products, ProductAdminConfig)
admin.site.register(EatType)
admin.site.register(UserAddCalorieHistory, UserCalorieHistoryAdminConfig)
admin.site.register(SportsExercises, SportsExercisesAdminConfig)
admin.site.register(UserRemoveCalorieHistory,
                    UserRemoveCalorieHistoryAdminConfig)
