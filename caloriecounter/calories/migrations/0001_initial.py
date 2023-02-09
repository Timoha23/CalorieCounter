# Generated by Django 4.1.6 on 2023-02-09 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название продукта')),
                ('calories', models.IntegerField(verbose_name='Каллории')),
                ('proteins', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Белки')),
                ('fats', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Жиры')),
                ('carbohydrates', models.DecimalField(decimal_places=3, max_digits=10, verbose_name='Углеводы')),
            ],
        ),
    ]
