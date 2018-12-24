from webapp.models import Food, Order, OrderFood
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.forms import FoodCreateForm, FoodUpdateForm


class FoodListView(ListView):
    model = Food
    template_name = 'index.html'


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = FoodUpdateForm


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodCreateForm

    def get_success_url(self):
        return reverse('food_detail', kwargs={'pk': self.object.pk})


