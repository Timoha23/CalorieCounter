import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .forms import AddCalorieForm, RemoveCalorieForm, RemoveCalorieCustomForm
from .models import (
    Products, UserAddCalorieHistory, UserRemoveCalorieHistory,
    SportsExercises
)


def index(request):
    return render(request, template_name='calories/index.html')


@login_required
def create_calories(request):
    """Страница с добавлением продуктов для юзера"""

    form = AddCalorieForm(request.POST or None)
    if request.method == 'POST':
        # form = AddCalorieForm(request.POST)
        if form.is_valid():
            product = Products.objects.get(name=form.cleaned_data.get('query'))
            UserAddCalorieHistory.objects.create(
                user=request.user,
                type=form.cleaned_data.get('types'),
                product=product,
                amount=form.cleaned_data.get('amount'),
            )
            return redirect('calories:create_calories')
        else:
            return redirect('calories:index')

    breakfast = UserAddCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Завтрак',
        pub_date__date=datetime.date.today(),
    )

    lunch = UserAddCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Обед',
        pub_date__date=datetime.date.today(),
    )

    dinner = UserAddCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Ужин',
        pub_date__date=datetime.date.today(),
    )

    snack = UserAddCalorieHistory.objects.select_related('product').filter(
        user=request.user,
        type__name_ru='Перекус',
        pub_date__date=datetime.date.today(),
    )

    all_types_eat = UserAddCalorieHistory.objects.select_related(
        'product').filter(
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

    # form = AddCalorieForm()
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


@login_required
def delete_created_calories(request, id):
    """Удаление созданных калорий"""
    object = get_object_or_404(UserAddCalorieHistory, id=id)
    object.delete()
    return redirect('calories:create_calories')


@login_required
def remove_calories(request):
    """Добавление тренировки или иных действий способствующих
    сжиганию калорий"""

    form = RemoveCalorieForm(request.POST or None)
    custom_form = RemoveCalorieCustomForm(request.POST or None)
    history = UserRemoveCalorieHistory.objects.select_related(
        'type').filter(pub_date__date=datetime.date.today()).order_by('-pub_date')[:10]
    calories_for_user = 0
    for el in history:
        calories_for_user += el.calories

    context = {
        'form': form,
        'custom_form': custom_form,
        'history': history,
        'calories_for_user': calories_for_user,
        'history_exists': history.exists(),
    }

    if request.method == 'POST':

        if form.is_valid() or custom_form.is_valid():
            if 'form_with_exercises' in request.POST:
                calories = (
                    form.cleaned_data.get('minutes')/60 *
                    SportsExercises.objects.get(name=form.cleaned_data.get(
                        'type')).calories_count
                )

                UserRemoveCalorieHistory.objects.create(
                    user=request.user,
                    type=SportsExercises.objects.get(
                        name=form.cleaned_data.get('type')
                    ),
                    custom_type=None,
                    minutes=form.cleaned_data.get('minutes'),
                    calories=calories
                )

            elif 'custom_user_form' in request.POST:
                UserRemoveCalorieHistory.objects.create(
                    user=request.user,
                    custom_type=custom_form.cleaned_data.get('custom_type'),
                    type=None,
                    minutes=form.cleaned_data.get('minutes'),
                    calories=custom_form.cleaned_data.get('calories'),
                )

            return redirect('calories:remove_calories')
        else:
            if 'custom_user_form' in request.POST:
                form.errors.clear()
            return render(
                request,
                context=context,
                template_name='calories/remove_calories.html',
            )

    return render(
        request,
        context=context,
        template_name='calories/remove_calories.html'
    )


@login_required
def delete_removed_calories(request, id):
    object = get_object_or_404(UserRemoveCalorieHistory, id=id)
    object.delete()
    return redirect('calories:remove_calories')
