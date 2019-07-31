from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('delete/', views.delete, name="delete"),

    path('view/', views.view, name="view"),
    path('update/', views.update, name="update"),

    path('add_view/', views.add_view, name="add_view"),
    path('add/', views.add, name="add"),

    path('changepass_view/', views.changepass_view, name="changepass_view"),
    path('changepass/', views.changepass, name="changepass"),
]