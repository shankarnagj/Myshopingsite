from django.urls import path
from . import views

app_name = 'ordersapp'

urlpatterns = [
    path('create/',views.order_create,name = 'order_create'),
]