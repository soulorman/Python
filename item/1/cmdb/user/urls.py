from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('create/ajax/', views.create_ajax, name="create_ajax"),
    path('delete/ajax/', views.delete_ajax, name="delete_ajax"),
    path('get/ajax/', views.get_ajax, name="get_ajax"),
    path('update/ajax/', views.update_ajax, name="update_ajax"),
]
