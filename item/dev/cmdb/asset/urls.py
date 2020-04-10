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
    path('edit_save/ajax', views.edit_save_ajax, name='edit_save_ajax'),

    #动态监控的跳转页面
    path('monitor/', views.monitor, name="monitor"),
    path('table/ajax', views.table_ajax, name='table_ajax'),
    path('cpu/ajax', views.cpu_ajax, name='cpu_ajax'),
    path('other/ajax', views.other_ajax, name='other_ajax'),
    path('pmem/ajax', views.pmem_ajax, name='pmem_ajax'),
    path('pcpu/ajax', views.pcpu_ajax, name='pcpu_ajax'),
    path('yuce/ajax', views.gpu_yuce, name='gpu_yuce'),
    path('gpu/ajax', views.gpu_ajax, name='gpu_ajax'),

    # 部署资源的跳转
    path('deploy/ajax', views.deploy, name='deploy'),
    path('info_deploy/ajax', views.info_deploy_ajax, name='info_deploy_ajax'),
    path('get_deploy/ajax', views.get_deploy_ajax, name='get_deploy_ajax'),
    path('edit_save_deploy/ajax', views.edit_save_deploy_ajax, name='edit_save_deploy_ajax'),
    path('delete_deploy_info/ajax', views.delete_deploy_info_ajax, name='delete_deploy_info_ajax'),
    path('create_deploy/ajax', views.create_deploy_ajax, name="create_deploy_ajax"),

    # 服务器角色信息
    path('server_role_information', views.server_role_information, name='server_role_information'),
    path('server_role_information/ajax', views.server_role_information_ajax, name="server_role_information_ajax"),

    #报警
    path('error_info/ajax', views.error_info_ajax, name="error_info_ajax"),
]