from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index),
    path('destination/<int:place_id>/', views.destination, name='destination')
]