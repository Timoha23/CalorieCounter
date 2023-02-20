from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddCalorieForm
from .models import Products


#################
from django.db.models.functions import Lower
from django.http import JsonResponse


def search(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        results = []
        if len(q) > 2:
            results = list(Products.objects.filter(title__istartswith=q).values_list(Lower('title'), flat=True))
        return JsonResponse(results, safe=False)
###################

def index(request):
    return render(request, template_name='calories/index.html')


@login_required
def create_calories(request):
    form = AddCalorieForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data.get('types'))
        print('aaa')
        return redirect('calories:create_calories')
    context = {
        'form': form,
    }
    return render(
        request,
        template_name='calories/calories.html',
        context=context
    )
