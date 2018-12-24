from webapp.models import Food, Order, OrderFood
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from django.urls import reverse
from django.http import HttpResponseRedirect


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})