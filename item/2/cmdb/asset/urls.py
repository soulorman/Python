# encoding: utf-8
from asset import views
from django.urls import path

app_name = 'asset'

urlpatterns = [
    # 首页以及首页ajax
    path('index/', views.index, name='index'),
    path('list/ajax', views.list_ajax, name='list_ajax'),
    path('delete/ajax', views.delete_ajax, name='delete_ajax'),
    path('get/ajax', views.get_ajax, name='get_ajax'),
    path('edit/ajax', views.edit_ajax, name='edit_ajax'),
    path('resource/ajax', views.resource_ajax, name='resource_ajax'),
    # 跳转资源页面
    path('resource/', views.resource, name='resource'),
    path('other/ajax', views.other_ajax, name='other_ajax'),
    
    path('deploy/ajax', views.deploy, name='deploy'),
    path('resource_other/ajax', views.resource_other, name='resource_other'),
    path('info/ajax', views.info_up_ajax, name='info_up_ajax'),
    path('get_up/ajax', views.get_up_ajax, name='get_up_ajax'),
    path('edit_up/ajax', views.edit_up_ajax, name='edit_up_ajax'),
    path('delete_up/ajax', views.delete_up_ajax, name='delete_up_ajax'),
    path('create_up/ajax', views.create_up_ajax, name="create_up_ajax"),
    path('error_info/ajax', views.error_info_ajax, name="error_info_ajax"),

    path('asset_dev/ajax', views.asset_dev_ajax, name="asset_dev_ajax"),

    # path('log/ajax', views.log_ajax, name='log_ajax'),
    path('cpu/ajax', views.cpu_ajax, name='cpu_ajax'),
    path('pmem/ajax', views.pmem_ajax, name='pmem_ajax'),
    path('pcpu/ajax', views.pcpu_ajax, name='pcpu_ajax'),
    path('table/ajax', views.table_ajax, name='table_ajax'),
    path('gpu/ajax', views.gpu_ajax, name='gpu_ajax'),
    path('yuce/ajax', views.gpu_yuce, name='gpu_yuce'),

]
