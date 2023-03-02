from django import forms
from django.core.exceptions import ValidationError

from .models import EatType, Products, UserRemoveCalorieHistory


class AddCalorieForm(forms.Form):
    types = forms.ModelChoiceField(queryset=EatType.objects.all(),
                                   label='Тип приема пищи')
    query = forms.CharField(max_length=300, label='Название пищи')
    amount = forms.IntegerField(label='Количество в граммах',
                                max_value=100000,
                                min_value=1)

    def clean_query(self):
        query = self.cleaned_data.get('query')
        if not Products.objects.filter(name=query).exists():
            print('ERROR query')
            raise ValidationError('Данного продукта нет в базе')
        return query


class RemoveCalorieForm(forms.ModelForm):

    class Meta:
        model = UserRemoveCalorieHistory
        fields = ('type', 'minutes')


class RemoveCalorieCustomForm(forms.ModelForm):
    calories = forms.IntegerField(min_value=0, max_value=1500)

    class Meta:
        model = UserRemoveCalorieHistory
        fields = ('custom_type', 'minutes', 'calories')
