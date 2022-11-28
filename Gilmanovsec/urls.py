
from django.contrib import admin
from django.urls import path
from Gilmanovapp import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('form/', views.form),
]
