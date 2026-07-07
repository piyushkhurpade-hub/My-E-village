from django.urls import path
from . import views

app_name = 'schemes'

urlpatterns = [
    path('', views.list_schemes, name='list'),
    path('<int:scheme_id>/', views.scheme_detail, name='detail'),
    path('add/', views.add_scheme, name='add'),
]
