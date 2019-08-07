# encoding: utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse

def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/index.html')
