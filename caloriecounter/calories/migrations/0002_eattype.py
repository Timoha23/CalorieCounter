# Generated by Django 4.1.6 on 2023-02-15 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EatType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ru', models.CharField(max_length=100, verbose_name='Время приема пищи(завтрак, обед, ужин)')),
                ('name_en', models.CharField(max_length=100, verbose_name='Время приема пищи на англ.')),
            ],
            options={
                'verbose_name': 'Тип',
                'verbose_name_plural': 'Типы',
            },
        ),
    ]
