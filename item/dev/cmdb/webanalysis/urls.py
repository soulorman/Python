# encoding: utf-8
from django.urls import path
from . import views

app_name = 'webanalysis'

urlpatterns = [
    path('index/',  views.index, name='index'),
    path('upload/', views.upload, name='upload'),
    path('dist_status_code/', views.dist_status_code, name='dist_status_code'),
    path('tren_visit/', views.tren_visit, name='tren_visit')
]
