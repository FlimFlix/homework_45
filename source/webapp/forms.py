from django import forms
from webapp.models import Food, Order, OrderFood


class FoodCreateForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


class FoodUpdateForm(forms.ModelForm):
    class Meta:
        model = Food
        exclude = []


