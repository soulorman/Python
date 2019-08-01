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

    path('create_view/', views.create_view, name="create_view"),
    path('create/', views.create, name="create"),

    path('changepass_view/', views.changepass_view, name="changepass_view"),
    path('changepass/', views.changepass, name="changepass"),
]