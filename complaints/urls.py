from django.urls import path
from . import views

app_name = 'complaints'

urlpatterns = [
    path('submit/', views.submit_complaint, name='submit'),
    path('update/<int:complaint_id>/', views.update_complaint, name='update'),
]
