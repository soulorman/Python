from django.urls import path
from backend import views

app_name = 'backend'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # 根路径直接跳转
    #path('', RedirectView.as_view(url='/user/login')),

    path('create/ajax/', views.create_ajax, name="create_ajax"),
    path('delete/ajax/', views.delete_ajax, name="delete_ajax"),
    path('flush/ajax/', views.flush_ajax, name="flush_ajax"),
    path('edit/ajax/', views.edit_ajax, name="edit_ajax"),
    path('get/ajax/', views.get_ajax, name="get_ajax"),
    path('changepass/ajax/', views.changepass_ajax, name="changepass_ajax"),

    path('scores/', views.scores, name="scores"),
    path('record/', views.record, name="record"),
    path('correct_short/', views.correct_short, name="correct_short"),
    path('edit_short/', views.edit_short, name="edit_short"),
]
