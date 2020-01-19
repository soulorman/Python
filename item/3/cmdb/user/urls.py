from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    path('create/ajax/', views.create_ajax, name="create_ajax"),
    path('delete/ajax/', views.delete_ajax, name="delete_ajax"),
    path('edit/ajax/', views.edit_ajax, name="edit_ajax"),
    path('get/ajax/', views.get_ajax, name="get_ajax"),
    path('changepass/ajax/', views.changepass_ajax, name="changepass_ajax"),
]