from django.urls import path
from webapp.views import FoodCreateView, FoodDetailView, FoodListView, FoodDeleteView, FoodUpdateView, \
    OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView, OrderFoodCreateView, order_cancel_view, \
    OrderFoodUpdateView, OrderFoodDeleteView, order_deliver_view

app_name = 'webapp'

urlpatterns = [
    path('', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/cancel', order_cancel_view, name='order_cancel'),
    path('order/<int:pk>/deliver', order_deliver_view, name='order_deliver'),
    path('order/<int:pk>/foods', OrderFoodCreateView.as_view(), name='order_food_create'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('foods', FoodListView.as_view(), name='food_list'),
    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/order_food_update', OrderFoodUpdateView.as_view(), name='order_food_update'),
    path('order/<int:pk>/order_food_delete', OrderFoodDeleteView.as_view(), name='order_food_delete'),
]
