from django.urls import path, include
from lotto import views

urlpatterns = [
    path('', views.index),
]