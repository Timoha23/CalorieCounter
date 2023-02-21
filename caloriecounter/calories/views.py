import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import AddCalorieForm
from .models import Products, UserCalorieHistory


def index(request):
    return render(request, template_name='calories/index.html')


@login_required
def create_calories(request):
    """Страница с добавлением продуктов для юзера"""
    if request.method == 'POST':
        form = AddCalorieForm(request.POST)
        if form.is_valid():
            product = Products.objects.get(name=form.cleaned_data.get('query'))
            UserCalorieHistory.objects.create(
                user=request.user,
                type=form.cleaned_data.get('types'),
                product=product,
                amount=form.cleaned_data.get('amount'),
            )
            return redirect('calories:create_calories')
        else:
            return redirect('calories:index')

    breakfast = UserCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Завтрак',
        pub_date__date=datetime.date.today(),
    )

    lunch = UserCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Обед',
        pub_date__date=datetime.date.today(),
    )

    dinner = UserCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Ужин',
        pub_date__date=datetime.date.today(),
    )

    snack = UserCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Перекус',
        pub_date__date=datetime.date.today(),
    )

    all_types_eat = UserCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        pub_date__date=datetime.date.today(),
    )

    calories_for_user = 0
    for prod in all_types_eat:
        calories_for_user += prod.amount/100 * prod.product.calories

    if breakfast.exists() is False:
        breakfast = False
    if dinner.exists() is False:
        dinner = False
    if lunch.exists() is False:
        lunch = False
    if snack.exists() is False:
        snack = False

    form = AddCalorieForm()
    products = Products.objects.all()

    context = {
        'form': form,
        'products': products,
        'breakfast': breakfast,
        'lunch': lunch,
        'dinner': dinner,
        'snack': snack,
        'calories_for_user': calories_for_user,
    }
    return render(
        request,
        template_name='calories/calories.html',
        context=context
    )


def delete_created_calories(request, id):
    """Удаление созданных каллорий"""
    object = UserCalorieHistory.objects.get(id=id)
    object.delete()
    return redirect('calories:create_calories')
