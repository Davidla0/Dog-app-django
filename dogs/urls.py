from django.contrib import admin
from django.urls import path

from dogs import views


urlpatterns = [
    path('', views.MainView, name='mainpage'),
    path('photo/<str:pk>/', views.ViewPhoto, name = 'photo'),

]
