#encoding: utf-8

from datetime import timedelta

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist

from .models import Host,Resource,Host_All,Monitor
from django.forms.models import model_to_dict

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


def gpu_info():
    list = []
    gpu = Resource.objects.all()
    for i in gpu:
        a = model_to_dict(i).get('gpu','')
        b = eval(a)
        c = b.get('gpu_user',[])
    for j in c:
        for k,v in j.items():
            list.append(k + '(' +  v  +')')

    if list:
        return hanshu(list,list,list)


def hanshu(list1,list2,list3):

    l1 = []
    for index,value in enumerate(list1):
        l1.append((index,[value]))
    for index,value in enumerate(list2):
        l1[index][1].append(value)
    for index,value in enumerate(list3):
        l1[index][1].append(value)

    return l1


def monitor(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    ip = request.GET['IP']
    result = Monitor.objects.get(ip=ip)
    result_dict=model_to_dict(result)

    result_dict['isalive'] = result_dict['isalive'].replace(' ','').split(',')[:-1:]
    result_dict['cpu'] = result_dict['cpu'].replace(' ','').split(',')[:-1:]
    result_dict['mem'] = result_dict['mem'].replace(' ','').split(',')[:-1:]

    gpu = gpu_info()

    return render(request,'asset/monitor.html',{'result' : result_dict, 'ip' : ip,'gpu':gpu})


def get_allinfo_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' :403})

    try:
        _id = request.GET.get('id', 0)
        host = Host.objects.get(pk=_id)
        host_alls =  Host_All.objects.filter(ip=host.ip)

        tmp_resources = {}
        for host_all in host_alls:
            tmp_resources['result'] = {
                'id' : _id,
                'name' : host.name,
                'ip' : host.ip,
                'mac' : host.mac,
                'os' : host.os,
                'kernel' : host.kernel,
                'arch' : host.arch,
                'cpu' : host.cpu,
                'cpu_core' : host.cpu_core,
                'cpu_thread' : host.cpu_thread,
                'cpu_type' : host_all.cpu_type,
                'mem' : host.mem,
                'mem_scalable' : host_all.mem_scalable,
                'mem_slot':host_all.mem_slot,
                'server_type' : host_all.server_type,
                'server_producter' : host_all.server_producter,
                'server_number' : host_all.server_number,
                'gpu_info'  : host_all.gpu_info,
                'network' : host_all.network,
                'disk' : host.disk,
                'root' : host_all.root,
                'data' : host_all.data,
                'created_time' : host.created_time,
                'user' : host.user,
                'remark' : host.remark
            }
            return JsonResponse({'code': 200, 'result' : tmp_resources['result']})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : []})

def resource_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403,'result' : []})

    try:
        _id = request.GET.get('id', 0)
        host = Host.objects.get(pk=_id)
        end_time = timezone.now()
        start_time = timezone.now() - timedelta(days = 1)
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
            start_time += timedelta(minutes=10)
        # for resource in resources:
        #     xAxis.append(resource.created_time.strftime('%H:%M'))
        #     CPU_datas.append(resource.cpu)
        #     MEM_datas.append(resource.mem)

        return JsonResponse({'code' : 200, 'result' : {'xAxis' : xAxis, 'CPU_datas' : CPU_datas, 'MEM_datas' : MEM_datas}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : []})



