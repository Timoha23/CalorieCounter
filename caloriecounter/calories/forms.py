from django import forms
from .models import EatType


class AddCalorieForm(forms.Form):
    types = forms.ModelChoiceField(queryset=EatType.objects.all(), label='Тип приема пищи')
    query = forms.CharField(max_length=300, label='Название пищи')
    amount = forms.IntegerField(label='Количество в граммах')
