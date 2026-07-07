from django.urls import path
from . import views

app_name = 'agriculture'

urlpatterns = [
    path('', views.agri_home, name='home'),
    path('add-tip/', views.add_tip, name='add_tip'),
]
