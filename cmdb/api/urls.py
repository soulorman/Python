#encoding: utf-8

from django.urls import path
from .views import v1

app_name = 'api'

urlpatterns = [
   path('v1/client/<uuid>/', v1.ClientView.as_view(), name='client'),
]
