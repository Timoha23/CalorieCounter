from django.urls import path
from . import views


app_name = 'calories'

urlpatterns = [
    path('add_calories/', views.create_calories, name='create_calories'),
    path('test/', views.search, name='search'),
    path('', views.index, name='index'),
]
