from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Products(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name='Название продукта'
    )
    calories = models.IntegerField(
        verbose_name='Калории'
    )
    proteins = models.FloatField(
        verbose_name='Белки'
    )
    fats = models.FloatField(
        verbose_name='Жиры'
    )
    carbohydrates = models.FloatField(
        verbose_name='Углеводы'
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class EatType(models.Model):
    name_ru = models.CharField(
        max_length=100,
        verbose_name='Время приема пищи(завтрак, обед, ужин)'
    )
    name_en = models.CharField(
        max_length=100,
        verbose_name='Время приема пищи на англ.'
    )

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name_ru


class UserCalorieHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='calorie_user',
        verbose_name='Пользователь'
    )
    product = models.ForeignKey(
        Products,
        on_delete=models.CASCADE,
        related_name='product_in_history',
        verbose_name='Продукт'
    )
    amount = models.IntegerField(
        verbose_name='Количество в граммах'
    )
    type = models.ForeignKey(
        EatType,
        on_delete=models.SET_NULL,
        related_name='type_in_history',
        verbose_name='Время приема пищи(завтрак, обед, ужин)',
        null=True
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления продукта'
    )

    class Meta:
        verbose_name = 'История добавления каллорий'
        verbose_name_plural = 'История добавления каллорий'

    def __str__(self):
        return self.product.name


class SportsExercises(models.Model):
    """Модель в которой представлены упражнения и расход
    калорий в час при занятии этими упражнениями"""
    name = models.CharField(max_length=256, verbose_name='Название упражнения')
    calories_count = models.IntegerField(verbose_name='Количество калорий')

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'

    def __str__(self):
        return self.name


class UserRemoveCalorieHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='remove_calorie_user',
        verbose_name='Пользователь'
    )

    type = models.ForeignKey(
        SportsExercises,
        on_delete=models.SET_NULL,
        related_name='type_in_remove_history',
        verbose_name='Время приема пищи(завтрак, обед, ужин)',
        null=True
    )

    hours = models.FloatField(
        verbose_name='Количество часов за упражнением'
    )

    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата добавления упражнения'
    )
