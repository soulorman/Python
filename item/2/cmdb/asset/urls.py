# encoding: utf-8
from asset import views
from django.urls import path

app_name = 'asset'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('list/ajax', views.list_ajax, name='list_ajax'),
    path('delete/ajax', views.delete_ajax, name='delete_ajax'),
    path('get/ajax', views.get_ajax, name='get_ajax'),
    path('edit/ajax', views.edit_ajax, name='edit_ajax'),
    path('resource/ajax', views.resource_ajax, name='resource_ajax'),
    ## 跳转资源页面
    path('resource/', views.resource, name='resource'),
    path('show/ajax', views.show_ajax, name='show_ajax'),
   # path('log/ajax', views.log_ajax, name='log_ajax'),
    path('cpu/ajax', views.cpu_ajax, name='cpu_ajax'),
    path('pmem/ajax', views.pmem_ajax, name='pmem_ajax'),
   
]
