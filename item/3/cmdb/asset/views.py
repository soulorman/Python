# encoding: utf-8

from collections import defaultdict
from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from .models import Host, Host_All, Resource, Gpu, Deploy, Wealth
from .utils import compose, compose_up
from .select_sql import select
from .error_info import  get_error_info
from datetime import timedelta
from django.utils import timezone


def index(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/index.html')


def list_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    result = [ host.as_dict() for host in Host.objects.all()]
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
    try:
        result =  Resource.objects.filter(ip=_ip).order_by('-created_time')[0]
    except ObjectDoesNotExist as e:
        raise e

    return render(request, 'asset/resource.html', {'result':result.as_dict()})


def other_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    
    try:
        result =  Resource.objects.filter(ip=_ip, ).order_by('-created_time')[0]
        return JsonResponse({'code' : 200, 'result' : result.as_dict()})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def table_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    
    try:
        resource_all = Resource.objects.filter(ip=_ip, ).order_by('-created_time')[0]
        
        result = resource_all.process_isalive.replace(' ','').split(',')[:-1:]

        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})

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
        return JsonResponse({'code' : 403})

    legend = [
        'auth',
        'path',
        'recovery',
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
        start_time = end_time - timedelta(hours=1)

        resources = Resource.objects.filter(ip=_ip, created_time__gte=start_time).order_by('created_time')

        tmp_resources = {}
        for resource in resources:
            tmp_resources[resource.created_time.strftime('%m-%d %H:%M')] = {'process_mem_use' : resource.process_mem_use }

        xAxis = []
        MEM_datas = []
        while start_time <= end_time:   
            key = start_time.strftime('%m-%d %H:%M')
            resource = tmp_resources.get(key, {})
            xAxis.append(key)
            MEM_datas.append(resource.get('process_mem_use', '[]').replace(' ','').split(',')[:-1:])
            start_time += timedelta(minutes=5)
        # dict_text = {}
        # for name in legend:
        #     dict_text[name] = []
    #     for five_all in MEM_datas:
    #         if five_all == []:       
    #             dict_text[name].append(0)
    #     else:
    #         for mem_use in five_all:
    #             dict_text[name].append(mem_use)
        # 

        #     导入的这个包 相当于下面这话
        #     for name in legend:
        #     dict_text[name] = []

        dict_text = defaultdict(list) 
        for five_all in MEM_datas:
            five_all = [0] * len(legend) if five_all == [] else five_all
            for i in range(len(five_all)):
                dict_text[legend[i]].append(five_all[i])

        series = []
        for k,v in dict_text.items():
            text_first = ['name', 'type', 'data']
            text_second = [k, 'line', v]

            series.append(dict(zip(text_first,text_second)))

        return JsonResponse({'code' : 200, 'result' : {'legend': legend, 'xAxis' : xAxis, 'series':series}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : e})


def pcpu_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    legend = [
        'auth',
        'path',
        'recovery',
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
        start_time = end_time - timedelta(hours=1)

        resources = Resource.objects.filter(ip=_ip, created_time__gte=start_time).order_by('created_time')

        tmp_resources = {}
        for resource in resources:
            tmp_resources[resource.created_time.strftime('%m-%d %H:%M')] = {'process_cpu_use' : resource.process_cpu_use }

        xAxis = []
        MEM_datas = []
        while start_time <= end_time:
            key = start_time.strftime('%m-%d %H:%M')
            resource = tmp_resources.get(key, {})
            xAxis.append(key)
            MEM_datas.append(resource.get('process_cpu_use', '[]').replace(' ','').split(',')[:-1:])
            start_time += timedelta(minutes=5)

        # dict_text = {}
        # for name in legend:
        #     dict_text[name] = []
    #     for five_all in MEM_datas:
    #         if five_all == []:       
    #             dict_text[name].append(0)
    #     else:
    #         for mem_use in five_all:
    #             dict_text[name].append(mem_use)
        # 

        #     导入的这个包 相当于下面这话
        #     for name in legend:
        #     dict_text[name] = []

        dict_text = defaultdict(list) 
        for five_all in MEM_datas:
            five_all = [0] * len(legend) if five_all == [] else five_all
            for i in range(len(five_all)):
                dict_text[legend[i]].append(five_all[i])

        series = []
        for k,v in dict_text.items():
            text_first = ['name', 'type', 'data']
            text_second = [k, 'line', v]

            series.append(dict(zip(text_first,text_second)))

        return JsonResponse({'code' : 200, 'result' : {'legend': legend, 'xAxis' : xAxis, 'series':series}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'result' : e})


def gpu_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    end_time = timezone.now()
    start_time = end_time - timedelta(minutes=1)

    try:
        #result = Gpu.objects.filter(ip=_ip, created_time__gte=start_time).order_by('-created_time')[0]
        resource_all = Gpu.objects.all().values('ip','gpu_user_name').order_by('ip')
        
        result = {}
        for handle in resource_all:
            handle['gpu_user_name'] = handle['gpu_user_name'].replace(' ','').split(',')[:-1:]

            for txt in enumerate(handle['gpu_user_name']):
                if txt[0] not in result:
                    result[txt[0]] = []
                result[txt[0]].append(txt[1])

   
        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def gpu_yuce(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    try:
        result = select()
        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def deploy(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/deploy.html')


def info_up_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    result = [ deploy.as_dict() for deploy in Deploy.objects.all()]
    return JsonResponse({'code' : 200, 'result': result })


def get_up_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _id = request.GET.get('id', 0)
    try:
        result = compose_up(_id)

        return JsonResponse({'code' : 200,'result': result  })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def edit_up_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _hospital_address = request.POST.get('hospital_address', '')
    _project_name = request.POST.get('project_name', '')
    _deploy_version = request.POST.get('deploy_version', '')
    _update_time = request.POST.get('update_time', '')
    _remark = request.POST.get('remark', '')

    try:
        Deploy.update_remark(_hospital_address, _project_name, _deploy_version, _update_time, _remark)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def delete_up_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    _id = request.GET.get('id', 0)
    try:
        Deploy.delete(_id)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def create_up_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    is_valid = True
    errors = {}
    
    deploy = Deploy()
    deploy.hospital_address = request.POST.get('hospital_address','')
    deploy.project_name = request.POST.get('project_name', '')
    deploy.deploy_version = request.POST.get('deploy_version', '')
    deploy.update_time = request.POST.get('update_time', timezone.now())
    deploy.remark = request.POST.get('remark', '')
    
    try:
        Deploy.objects.get(hospital_address=request.POST.get('hospital_address',''))
        is_valid = False
        errors['hospital_address'] = '医院已存在,请重新填写'
    except BaseException as e:
        pass

    if is_valid:
        deploy.save()
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })


def error_info_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    end_time = timezone.now()
    start_time = end_time - timedelta(hours=24)
    try: 
        result = get_error_info(_ip,start_time)
        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


def resource_other(request):
    if not request.session.get('user'):
        return redirect('user:login')

    return  render(request, 'asset/resource_other.html')


def asset_dev_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403 })

    result = [ wealth.as_dict() for wealth in Wealth.objects.all()]
    return JsonResponse({'code' : 200, 'result': result })

