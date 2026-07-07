from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('', views.list_guides, name='list'),
]
