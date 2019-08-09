# encoding: utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Host, Host_All, Resource
from .utils import compose


def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/index.html')


def list_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    result = [ host.as_dict() for host in Host.objects.all() ]
    return JsonResponse({'code' : 200, 'result': result })


def delete_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    _id = request.GET.get('id', 0)
    try:
        Host.delete(_id)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def get_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _id = request.GET.get('id', 0)
    try:
        result = compose(_id)
        return JsonResponse({'code' : 200,'result': result  })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})
    

def edit_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.POST.get('ip', '')
    _user = request.POST.get('user', '')
    _remark = request.POST.get('remark', '')

    try:
        Host.update_remark(_ip, _remark)
        Host_All.update_user(_ip, _user)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def resource_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    try:
        xAxis, CPU_datas, MEM_datas=Resource.get_resource_data(_ip)
        return JsonResponse({'code' : 200, 'result' : {'xAxis':xAxis, 'CPU_datas': CPU_datas,'MEM_datas':MEM_datas}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def resource(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request, 'asset/resource.html')