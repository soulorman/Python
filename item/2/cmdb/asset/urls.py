# encoding: utf-8
from asset import views
from django.urls import path

app_name = 'asset'

urlpatterns = [
   path('index/', views.index, name='index'),
   path('list/ajax', views.list_ajax, name='list_ajax'),  
]
