# encoding: utf-8

from django.urls import path
from . import views

app_name = 'webanalysis'

urlpatterns = [
    path('index/',  views.index, name='index'),
    path('upload/', views.upload, name='upload')
]
