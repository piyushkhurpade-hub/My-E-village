from django.urls import path
from . import views

app_name = 'health'

urlpatterns = [
    path('', views.list_services, name='list'),
    path('add/', views.add_service, name='add'),
]
