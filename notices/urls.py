from django.urls import path
from . import views

app_name = 'notices'

urlpatterns = [
    path('', views.list_notices, name='list'),
    path('add/', views.add_notice, name='add'),
]
