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


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = []


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ['status']


class OrderFoodForm(forms.ModelForm):
    class Meta:
        model = OrderFood
        exclude = ['order']