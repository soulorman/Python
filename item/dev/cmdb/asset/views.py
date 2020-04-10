# encoding: utf-8

from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

from collections import defaultdict
from datetime import timedelta
from functools import wraps

from .models import Host, Host_More, Monitor_Resource, Gpu, Deploy, Wealth
from .utils import compose, compose_up, save_new_deploy_info
from .select_sql import select
from .error_info import  get_error_info


def login_required(func):
    """验证的装饰器
    
    缓存没有用户，而且没ajax的返回登录页面，缓存有ajax的返回403
    :param :func 不知道
    :return: 验证结果
    """
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        if request.session.get('user') is None:
            if request.is_ajax():
                return JsonResponse({'code':403,'result':[]})
            return redirect('user:login')
        return func(request, *args, **kwargs)
    return wrapper

@login_required
def index(request):
    """跳转软/硬件资源的首页

    :param request:前端页面返回的请求内容
    :return: 资源首页
    """
    return  render(request, 'asset/index.html')


@login_required
def list_ajax(request):
    """跳转软/硬件资源的首页

    :param request:前端页面返回的请求内容
    :return: 资源首页
    """
    result = [ host.as_dict() for host in Host.objects.all()]
    return JsonResponse({'code' : 200, 'result': result })


@login_required
def delete_ajax(request):
    """删除主机信息

    :param request:前端页面返回的请求内容
    :return: 删除成功或者报错信息
    """
    _id = request.GET.get('id', 0)
    try:
        Host.delete(_id)
        Host_More.delete(_id)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


@login_required
def get_ajax(request):
    """获取编辑的主机信息

    :param request:前端页面返回的请求内容
    :return: 更多的主机信息或者错误信息
    """
    _id = request.GET.get('id', 0)
    try:
        result = compose(_id)
        return JsonResponse({'code' : 200,'result': result  })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})
    
@login_required
def edit_save_ajax(request):
    """保存编辑的内容

    :param request:前端页面返回的请求内容
    :return: 保存成功的信息或者失败的信息
    """
    _ip = request.POST.get('ip', '')
    _user = request.POST.get('user', '')
    _remark = request.POST.get('remark', '')
    try:
        Host.update_remark(_ip, _remark)
        Host_More.update_user(_ip, _user)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


def resource_ajax(request):
    if not request.session.get('user'):
        return JsonResponse({'code' : 403})

    _ip = request.GET.get('ip', '')
    try:
        xAxis, CPU_datas, MEM_datas=Monitor_Resource.get_resource_data(_ip)
        return JsonResponse({'code' : 200, 'result' : {'xAxis':xAxis, 'CPU_datas': CPU_datas,'MEM_datas':MEM_datas}})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})

@login_required
def monitor(request):
    """跳转监控页面

    :param request:前端页面返回的请求内容
    :return: 监控页面和所有数据
    """
    _ip = request.GET.get('ip', '')
    try:
        result = Monitor_Resource.objects.filter(ip=_ip).order_by('-created_time')[0]
    except ObjectDoesNotExist as e:
        raise e

    return render(request, 'asset/monitor.html', {'result':result.as_dict()})


@login_required
def table_ajax(request):
    """显示第一部分表格的内容

    :param request:前端页面返回的请求内容
    :return: 所有进程信息或者错误信息
    """
    _ip = request.GET.get('ip', '')
    try:
        resource_all = Monitor_Resource.objects.filter(ip=_ip).order_by('-created_time')[0]
        result = resource_all.process_isalive.replace(' ','').split(',')[:-1:]
        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


@login_required
def cpu_ajax(request):
    """显示总cpu的使用率

    :param request:前端页面返回的请求内容
    :return: cpu使用率或者错误信息
    """
    _ip = request.GET.get('ip', '')
    try:
        resource_all =  Monitor_Resource.objects.filter(ip=_ip).order_by('-created_time')[0]        
        result = resource_all.cpu_total_use
        return JsonResponse({'code' : 200, 'result' : result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


@login_required
def other_ajax(request):
    """显示其他系统资源占用率

    :param request:前端页面返回的请求内容
    :return: 其他系统资源占用率或者错误信息
    """
    _ip = request.GET.get('ip', '')
    try:
        result =  Monitor_Resource.objects.filter(ip=_ip).order_by('-created_time')[0]
        return JsonResponse({'code' : 200, 'result' : result.as_dict()})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400, 'errors' : e})


@login_required
def pmem_ajax(request):
    """显示每个进程的内存占有率

    :param request:前端页面返回的请求内容
    :return: x，y轴的信息
    """
    # 该逻辑设计个人感觉不好，待改进
    # 思路如下：首先，在这里定义所需要的进程名称。然后按序排好，在数据库，强行按照这个顺序依次存放数值
    # 如果添加进程，首先在这里添加进程，然后在列表后面必须按序添加信息
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
        resources = Monitor_Resource.objects.filter(ip=_ip, created_time__gte=start_time).order_by('created_time')
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

        #     导入的这个包 相当于下面这话
        #     for name in legend:
        #     dict_text[name] = []
        dict_text = defaultdict(list) 
        for five_all in MEM_datas:
            # 循环判断有没有值，没有值就赋值0，有值就付值
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


@login_required
def pcpu_ajax(request):
    """显示每个进程的内存占有率

    :param request:前端页面返回的请求内容
    :return: x，y轴的信息
    """
    # 同上
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
        resources = Monitor_Resource.objects.filter(ip=_ip, created_time__gte=start_time).order_by('created_time')
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


@login_required
def gpu_yuce(request):
    """显示预测情况

    :param request:前端页面返回的请求内容
    :return:预测结果
    """
    try:
        result = select()
        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


@login_required
def gpu_ajax(request):
    """显示显卡信息

    :param request:前端页面返回的请求内容
    :return:gpu使用情况
    """
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


# 部署项目展示代码段
@login_required
def deploy(request):
    """跳转部署页面

    :param request:前端页面返回的请求内容
    :return: 部署页面
    """
    return  render(request, 'asset/deploy.html')


@login_required
def info_deploy_ajax(request):
    """获取部署页面的信息

    :param request:前端页面返回的请求内容
    :return: Deploy的所有信息
    """
    result = [ deploy.as_dict() for deploy in Deploy.objects.all()]
    return JsonResponse({'code' : 200, 'result': result })


@login_required
def get_deploy_ajax(request):
    """获取将要编辑的部署信息

    :param request:前端页面返回的请求内容
    :return: Deploy的所有信息或者错误信息
    """  
    _id = request.GET.get('id', 0)
    try:
        result = compose_up(_id)
        return JsonResponse({'code' : 200,'result': result  })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


@login_required
def edit_save_deploy_ajax(request):
    """保存编辑完的信息

    :param request:前端页面返回的请求内容
    :return: 保存成功或者报错信息
    """  
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


@login_required
def delete_deploy_info_ajax(request):
    """删除信息

    :param request:前端页面返回的请求内容
    :return: 保存成功或者报错信息
    """  
    _id = request.GET.get('id', 0)
    try:
        Deploy.delete(_id)
        return JsonResponse({'code' : 200 })
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})


@login_required
def create_deploy_ajax(request):
    """创建新的部署信息

    :param request:前端页面返回的请求内容
    :return: 创建成功或者报错信息
    """  
    is_valid = True
    errors = {}
    try:
        Deploy.objects.get(hospital_address=request.POST.get('hospital_address',''))
        is_valid = False
        errors['hospital_address'] = '医院已存在,请重新填写'
    except BaseException as e:
        pass

    if is_valid:
        save_new_deploy_info(request.POST)
        return JsonResponse({'code' : 200 })
    else:
        return JsonResponse({'code' : 400, 'errors' : errors })


@login_required
def server_role_information(request):
    """跳转服务器角色页面

    :param request:前端页面返回的请求内容
    :return: 服务器角色页面
    """ 
    return render(request, 'asset/server_role_information.html')


# 服务器角色信息
@login_required
def server_role_information_ajax(request):
    """返回服务器角色的所有信息

    :param request:前端页面返回的请求内容
    :return: 服务器角色所有信息
    """  
    result = [ wealth.as_dict() for wealth in Wealth.objects.all()]
    return JsonResponse({'code' : 200, 'result': result })

@login_required
def error_info_ajax(request):
    """报警

    :param request:前端页面返回的请求内容
    :return: 24小时的报警信息
    """  
    _ip = request.GET.get('ip', '')
    end_time = timezone.now()
    start_time = end_time - timedelta(hours=24)
    try: 
        result = get_error_info(_ip,start_time)
        return JsonResponse({'code' : 200, 'result': result})
    except ObjectDoesNotExist as e:
        return JsonResponse({'code' : 400 ,'errors' : e})
