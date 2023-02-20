from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    calories = models.IntegerField(verbose_name='Каллории')
    proteins = models.FloatField(verbose_name='Белки')
    fats = models.FloatField(verbose_name='Жиры')
    carbohydrates = models.FloatField(verbose_name='Углеводы')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name


class EatType(models.Model):
    name_ru = models.CharField(max_length=100, verbose_name='Время приема пищи(завтрак, обед, ужин)')
    name_en = models.CharField(max_length=100, verbose_name='Время приема пищи на англ.')

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def __str__(self):
        return self.name_ru
