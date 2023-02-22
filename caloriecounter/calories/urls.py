from django.urls import path

from . import views

app_name = 'calories'

urlpatterns = [
    path('add_calories/', views.create_calories, name='create_calories'),
    path('delete_created_calories/<int:id>/', views.delete_created_calories, name='delete_created_calories'),
    path('remove_calories/', views.remove_calories, name='remove_calories'),
    path('', views.index, name='index'),
]
