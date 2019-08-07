# encoding: utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse

from .models import Host

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/index.html')


def list_ajax(request):
    if not request.session.get('user'):
        return redirect('user:login')


    result = [ host.as_dict() for host in Host.objects.all() ]
    return JsonResponse({'code' : 200, 'result': result })