from webapp.models import Food, Order, OrderFood
from django.views.generic import DetailView, CreateView, UpdateView, View, DeleteView, ListView
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from webapp.forms import FoodCreateForm, FoodUpdateForm, OrderCreateForm, OrderForm, OrderFoodForm
from django.shortcuts import get_object_or_404, redirect


class FoodListView(ListView):
    model = Food
    template_name = 'food_list.html'


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail.html'


class FoodDeleteView(DeleteView):
    model = Food
    template_name = 'food_delete.html'

    def get_success_url(self):
        return reverse('index')


class FoodUpdateView(UpdateView):
    model = Food
    template_name = 'food_update.html'
    form_class = FoodUpdateForm

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class FoodCreateView(CreateView):
    model = Food
    template_name = 'food_create.html'
    form_class = FoodCreateForm

    def get_success_url(self):
        return reverse('webapp:food_detail', kwargs={'pk': self.object.pk})


class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    form_class = OrderCreateForm

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderDetailView(DetailView):
    model = Order
    template_name = 'order_detail.html'


class OrderListView(ListView):
    model = Order
    template_name = 'order_list.html'


class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderForm

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.pk})


class OrderFoodCreateView(CreateView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_create.html'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order'] = Order.objects.get(pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        form.instance.order = Order.objects.get(pk=self.kwargs.get('pk'))
        return super().form_valid(form)


class OrderFoodUpdateView(UpdateView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_update.html'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})


class OrderFoodDeleteView(DeleteView):
    model = OrderFood
    form_class = OrderFoodForm
    template_name = 'order_food_delete.html'

    def get_success_url(self):
        return reverse('webapp:order_detail', kwargs={'pk': self.object.order.pk})


def order_cancel_view(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if order.status in ('delivered', 'on_way'):
        raise Exception('Невозможно отменить доставленный заказ')
    else:
        order.status = 'canceled'
        order.save()

    return redirect('webapp:order_detail', pk)
