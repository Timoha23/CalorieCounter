from django.db import models


class Products(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название продукта')
    calories = models.IntegerField(verbose_name='Каллории')
    proteins = models.DecimalField(verbose_name='Белки', max_digits=10, decimal_places=3)
    fats = models.DecimalField(verbose_name='Жиры', max_digits=10, decimal_places=3)
    carbohydrates = models.DecimalField(verbose_name='Углеводы', max_digits=10, decimal_places=3)
