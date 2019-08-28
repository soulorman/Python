# encoding: utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Host, Host_All, Resource
from .utils import compose

from datetime import timedelta
from django.utils import timezone


def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/index.html')


def list_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    result = [ host.as_dict() for host in Host.objects.all().using('db2')]
    return JsonResponse({'code' : 200, 'result': result })


def delete_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    _id = request.GET.get('id', 0)
    try:
        Host.delete(_id)
        Host_All.delete(_id)
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

    _ip = request.GET.get('ip', '')
    result =  Resource.objects.filter(ip=_ip).order_by('-created_time')[0]
    result.process_isalive = result.process_isalive.replace(' ','').split(',')[:-1:]
    result.process_cpu_use = result.process_cpu_use.replace(' ','').split(',')[:-1:]
    result.process_mem_use = result.process_mem_use.replace(' ','').split(',')[:-1:]

    return render(request, 'asset/resource.html', {'result':result.as_dict()})


def show_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    
    try:
        resource_all =  Resource.objects.filter(ip=_ip, ).order_by('-created_time')[0]
        
        result = resource_all.process_isalive.replace(' ','').split(',')[:-1:]

        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})

'''
def log_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    os.

    '''


def cpu_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    
    try:
        resource_all =  Resource.objects.filter(ip=_ip, ).order_by('-created_time')[0]        
        result = resource_all.cpu_total_use
        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def pmem_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403,'result' : []})

    legend = [
        'auth',
        'path',
        'insights',
        'thoslide',
        'config',
        'registry',
        'tensorflow_model_server',
        'save_log',
        'celery',
        'redis',
        'nginx',
        'mysql'
    ]

    try:
        _ip = request.GET.get('ip', 0)

        end_time = timezone.now()
        start_time = timezone.now() - timedelta(hours=5)

        resources = Resource.objects.filter(ip=_ip, created_time__gte=start_time).order_by('created_time')

        tmp_resources = {}
        for resource in resources:
            tmp_resources[resource.created_time.strftime('%m-%d %H:%M')] = {'process_mem_use' : resource.process_mem_use }
    
        xAxis = []
        MEM_datas = []
        while start_time <= end_time:
            key = start_time.strftime('%m-%d %H:%M')
            resource =  tmp_resources.get(key, {})
            xAxis.append(key)
            MEM_datas.append(resource.get('process_mem_use', '[]').replace(' ','').split(',')[:-1:])
            start_time += timedelta(minutes=1)

        return JsonResponse({'code' : 200, 'result' : {'legend': legend, 'xAxis' : xAxis, 'MEM_datas' : MEM_datas}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : e})
