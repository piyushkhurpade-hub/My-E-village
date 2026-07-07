from django.urls import path
from . import views

app_name = 'marketplace'

urlpatterns = [
    path('', views.list_products, name='list'),
    path('add/', views.add_product, name='add'),
]
