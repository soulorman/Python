#encoding: utf-8

from django.urls import path, include
from .views import v1, v2, v3, v4, v5

app_name = 'api'

urlpatterns = [
    # path('v1/client/', v1.ClientView.as_view(), name='v1_client'),
    # path('v1/client/<ip>/', v1.ClientView.as_view(), name='v1_client_key'),
    # path('v1/client/<ip>/resource/', v1.ResourceView.as_view(), name='v1_resource'),

    # path('v2/client/', v2.ClientView.as_view(), name='v2_client'),
    # path('v2/client/<ip>/', v2.ClientView.as_view(), name='v2_client_key'),
    # path('v2/client/<ip>/resource/', v2.ResourceView.as_view(), name='v2_resource'),

    # path('v3/client/', v3.ClientView.as_view(), name='v3_client'),
    # path('v3/client/<ip>/', v3.ClientView.as_view(), name='v3_client_key'),
    # path('v3/client/<ip>/resource/', v3.ResourceView.as_view(), name='v3_resource'),

    # path('v4/client/', v4.ClientView.as_view(), name='v4_client'),
    # path('v4/client/<ip>/', v4.ClientView.as_view(), name='v4_client_key'),
    # path('v4/client/<ip>/resource/', v4.ResourceView.as_view(), name='v4_resource'),

    path('v5/client/', v5.ClientView.as_view(), name='v5_client'),
    path('v5/client/<ip>/', v5.ClientView.as_view(), name='v5_client_key'),
    path('v5/client/<ip>/resource/', v5.ResourceView.as_view(), name='v5_resource'),
]
