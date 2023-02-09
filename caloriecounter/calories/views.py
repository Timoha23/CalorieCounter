from django.shortcuts import render

def index(request):
    return render(request, template_name='calories/index.html')


def add_calories(request):
    return render(request, template_name='calories/add_calories.html')
