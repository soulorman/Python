#encoding: utf-8

from datetime import timedelta

from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import Host,Resource


def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return render(request,'asset/index.html')


def list_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403,'result' : []})
    
    result = [ host.as_dict() for host in Host.objects.all()]
    return JsonResponse({'code': 200, 'result' : result})


def delete_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403,'result' : []}) 
    
    _id = request.GET.get('id', 0)
    try:
        Host.objects.get(pk=_id).delete()
    except ObjectDoesNotExist as e:
        pass

    return JsonResponse({'code': 200})


def resource_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403,'result' : []})

    try:
        _id = request.GET.get('id', 0)
        host = Host.objects.get(pk=_id)
        end_time = timezone.now()
        start_time = timezone.now() - timedelta(hours = 1)
        resources =  Resource.objects.filter(ip=host.ip, created_time__gte=start_time).order_by('created_time')
        
        tmp_resources = {}
        for resource in resources:
            tmp_resources[resource.created_time.strftime('%Y-%m-%d %H:%M')] = { 'cpu' : resource.cpu, 'mem' : resource.mem }
        
        xAxis = []
        CPU_datas = []
        MEM_datas = []
        while start_time <= end_time:
            key = start_time.strftime('%Y-%m-%d %H:%M')
            resource =  tmp_resources.get(key, {})
            xAxis.append(key)
            CPU_datas.append(resource.get('cpu',0))
            MEM_datas.append(resource.get('mem',0))
            start_time += timedelta(minutes=5)


        
        # for resource in resources:
        #     xAxis.append(resource.created_time.strftime('%H:%M'))
        #     CPU_datas.append(resource.cpu)
        #     MEM_datas.append(resource.mem)

        return JsonResponse({'code' : 200, 'result' : {'xAxis' : xAxis, 'CPU_datas' : CPU_datas, 'MEM_datas' : MEM_datas}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : []})