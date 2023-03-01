import datetime

from django.contrib.auth import get_user_model
from django.db.models import Sum
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404

from .forms import CreationForm
from calories.models import UserAddCalorieHistory, UserRemoveCalorieHistory


User = get_user_model()


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('calories:index')
    template_name = 'users/signup.html'


def user_profile(request, username):
    """Профиль юзера"""

    user = get_object_or_404(User, username=username)
    added_calories = UserAddCalorieHistory.objects.select_related(
        'product').filter(user=user)
    removed_calories = UserRemoveCalorieHistory.objects.filter(user=user)

    # добавлено/убавлено калорий за сегодня
    today_added_calories_stat = added_calories.filter(
        pub_date__date=datetime.date.today()).aggregate(
            Sum('product__calories')).get(
            'product__calories__sum'
        )

    today_removed_calories_stat = removed_calories.filter(
        pub_date__date=datetime.date.today()).aggregate(
            Sum('calories')).get(
            'calories__sum'
        )

    # добавлено/убавлено калорий за 7 дней
    seven_days = datetime.date.today() - datetime.timedelta(days=7)
    seven_days_added_calories_stat = added_calories.filter(
        pub_date__date__gte=seven_days).aggregate(
            Sum('product__calories')).get(
            'product__calories__sum'
        )
    seven_days_removed_calories_stat = removed_calories.filter(
        pub_date__date__gte=seven_days).aggregate(
            Sum('calories')).get(
            'calories__sum'
        )

    # добавлено/убавлено калорий за все время
    all_days_added_calories_stat = added_calories.aggregate(
            Sum('product__calories')).get(
            'product__calories__sum'
        )

    all_days_removed_calories_stat = removed_calories.aggregate(
            Sum('calories')).get(
            'calories__sum'
        )

    # статистика за сегодня
    today_added_calories = added_calories.filter(
        pub_date__date=datetime.date.today())

    if today_added_calories.exists():
        today_user_fats = today_added_calories.aggregate(
            Sum('product__fats')).get(
            'product__fats__sum')
        today_user_proteins = today_added_calories.aggregate(
            Sum('product__proteins')).get(
            'product__proteins__sum')
        today_user_carbohydrates = today_added_calories.aggregate(
            Sum('product__carbohydrates')).get(
            'product__carbohydrates__sum')
    else:
        today_user_fats, today_user_proteins, today_user_carbohydrates = (
            0, 0, 0
        )

    # статистика за 7 дней
    seven_days_added_calories = added_calories.filter(
        pub_date__date__gte=seven_days)

    if seven_days_added_calories.exists():

        seven_days_user_fats = seven_days_added_calories.aggregate(
            Sum('product__fats')).get(
            'product__fats__sum')

        seven_days_user_proteins = seven_days_added_calories.aggregate(
            Sum('product__proteins')).get(
            'product__proteins__sum')

        seven_days_user_carbohydrates = seven_days_added_calories.aggregate(
            Sum('product__carbohydrates')).get(
            'product__carbohydrates__sum')
    else:
        seven_days_user_fats, seven_days_user_proteins,
        seven_days_user_carbohydrates = (
            0, 0, 0
        )

    # статистика за все время
    if added_calories.exists():
        all_days_user_fats = added_calories.aggregate(
            Sum('product__fats')).get(
            'product__fats__sum')

        all_days_user_proteins = added_calories.aggregate(
            Sum('product__proteins')).get(
            'product__proteins__sum')

        all_days_user_carbohydrates = added_calories.aggregate(
            Sum('product__carbohydrates')).get(
            'product__carbohydrates__sum')
    else:
        all_days_user_fats, all_days_user_proteins,
        all_days_user_carbohydrates = (
            0, 0, 0
        )

    context = {
        'user': user,
        'added_calories': added_calories,
        'removed_calories': removed_calories,
        'today_user_fats': int(today_user_fats),
        'today_user_proteins': int(today_user_proteins),
        'today_user_carbohydrates': int(today_user_carbohydrates),
        'seven_days_user_fats': int(seven_days_user_fats),
        'seven_days_user_proteins': int(seven_days_user_proteins),
        'seven_days_user_carbohydrates': int(seven_days_user_carbohydrates),
        'all_days_user_fats': int(all_days_user_fats),
        'all_days_user_proteins': int(all_days_user_proteins),
        'all_days_user_carbohydrates': int(all_days_user_carbohydrates),
        'today_added_calories_stat': today_added_calories_stat,
        'today_removed_calories_stat': today_removed_calories_stat,
        'seven_days_added_calories_stat': seven_days_added_calories_stat,
        'seven_days_removed_calories_stat': seven_days_removed_calories_stat,
        'all_days_added_calories_stat': all_days_added_calories_stat,
        'all_days_removed_calories_stat': all_days_removed_calories_stat,
        'added_calories_exists': added_calories.exists(),
        'removed_calories_exists': removed_calories.exists(),
    }

    return render(request, template_name='users/profile.html', context=context)
