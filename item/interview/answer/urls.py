from django.urls import path
from answer import views

app_name = 'answer'

urlpatterns = [
    path('index/', views.index, name="index"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    # 根路径直接跳转
    #path('', RedirectView.as_view(url='/user/login')),
    path('interview_options/', views.interview_options, name="interview_options"),
    path('interview_options_answer/', views.interview_options_answer, name="interview_options_answer"),
    path('interview_sort_answer/', views.interview_sort_answer, name="interview_sort_answer"),
]
