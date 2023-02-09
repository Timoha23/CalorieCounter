from django.urls import path, include
from . import views

app_name = 'calories'

urlpatterns = [
    path('add_calories/', views.add_calories, name='add_calories'),
    path('', views.index, name='index')
]