"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from webapp.views import FoodCreateView, FoodDetailView, FoodListView, FoodDeleteView, FoodUpdateView, \
    OrderCreateView, OrderListView, OrderDetailView, OrderUpdateView, OrderFoodCreateView, order_cancel_view, \
    OrderFoodUpdateView, OrderFoodDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', OrderListView.as_view(), name='order_list'),
    path('order/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('order/<int:pk>/cancel', order_cancel_view, name='order_cancel'),
    path('order/<int:pk>/foods', OrderFoodCreateView.as_view(), name='order_food_create'),
    path('order/<int:pk>/update', OrderUpdateView.as_view(), name='order_update'),
    path('foods', FoodListView.as_view(), name='food_list'),
    path('food/create', FoodCreateView.as_view(), name='food_create'),
    path('food/<int:pk>', FoodDetailView.as_view(), name='food_detail'),
    path('food/<int:pk>/delete', FoodDeleteView.as_view(), name='food_delete'),
    path('food/<int:pk>/update', FoodUpdateView.as_view(), name='food_update'),
    path('order/create', OrderCreateView.as_view(), name='order_create'),
    path('order/<int:pk>/order_food_update', OrderFoodUpdateView.as_view(), name='order_food_update'),
    path('order/<int:pk>/order_food_delete', OrderFoodDeleteView.as_view(), name='order_food_delete')

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
