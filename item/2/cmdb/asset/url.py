# encoding: utf-8

app_name = 'asset'

from django.urls import path

urlpatterns = [
    path('index/', views.index, name='index'),
]
