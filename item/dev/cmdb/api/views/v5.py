#encoding: utf-8

import json
import time

from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

#from utils.signutils import get_sign
from asset.models import Host, Host_More, Monitor_Resource

# 继承view的类
class APIView(View):

    def __init__(self):
        # 继承构造函数，并加一个属性 secret_key
        super(APIView, self).__init__()
        #self.secret_key = {'123456789' : 'abcdef'}
    # 验证客户端的数据是否完整，但是因为字典乱序，其他类型符号总是[] 暂时抛弃  # 3.5之前字典无序，3.6后有序
    # def valid_sign(self, request):
    #     data = {}
    #     for key in request.GET:
    #         data[key] = request.GET.get(key)

    #     for key in request.POST:
    #         data[key] = request.POST.get(key)

    #     data.update(self.get_json())
    #     key = data.pop('key', '')
    #     sign = data.pop('sign', '')
    #     unix_time = data.pop('time', '')

    #     secret = self.secret_key.get(key, '')
        
    #     if not secret:
    #         return False, 'error key'

    #     data_sign = get_sign(data, unix_time, key, secret)

    #     if sign != data_sign:
    #         return False, 'error data'

    #     try:
    #         unix_time = int(unix_time)
    #         current_unix_time = time.time()
    #         if not(unix_time >= current_unix_time - 5 *60 and unix_time <= current_unix_time + 5 *60):
    #             return False, 'error time'
    #     except BaseException as e:
    #         return False, 'error time'

    #     return True, ''


    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        is_valid = True
        #is_valid, errors =  self.valid_sign(request)
        if is_valid:
            return super(APIView, self).dispatch(request, *args, **kwargs)
        else:
            return self.response(code=400, errors=errors)

    def get_json(self):
        """得到客户端发送过来的body

        :return: 被编码过后的内容或者空字典
        """
        try:
            return json.loads(self.request.body.decode('utf-8'))
        except BaseException as e:
            return {}

    def response(self, result=None, code=200, errors={}):
        """返回的编码
        
        :param result:页面的内容
        :param code: 代码格式
        :param errors:错误信息
        :return: 信息
        """
        return JsonResponse({'code': code, 'result' : result, 'errors' : errors})
        

class ClientView(APIView):
    def post(self, request, *args, **kwargs):
        """获取post的内容

        :param request: 客户端发送的内容
        :param args: 任意参数
        :param kwargs: 任意关键字参数
        :return: 内容、格式、错误信息
        """
        _ip = kwargs.get('ip', '')
        _Json = self.get_json()

        host = Host.create_or_replace(
                                        _ip, \
                                        _Json.get('name', ''), \
                                        _Json.get('os', ''), \
                                        _Json.get('kernel', ''), \
                                        _Json.get('cpu_number', 0), \
                                        _Json.get('cpu_core', 0), \
                                        _Json.get('cpu_vcore', 0), \
                                        _Json.get('arch', ''), \
                                        _Json.get('get_mem_info', '[]'), \
                                        _Json.get('disk_info', '{}'), \
                                        _Json.get('get_gpu_info', '无')
                                    )

        Host_more = Host_More.create_or_replace( 
                                        _ip, \
                                        _Json.get('mac', ''), \
                                        _Json.get('cpu_name', ''), \
                                        _Json.get('server_producter', ''), \
                                        _Json.get('server_name', 0), \
                                        _Json.get('serial', 0), \
                                        _Json.get('network', 0), \
                                        _Json.get('partitons', ''),
                                    )
        result = host.as_dict().update(Host_more.as_dict())
        return self.response(result)


    def get(self, request, *args, **kwargs):
        """获取get的内容

        :param request: 客户端发送的内容
        :param args: 任意参数
        :param kwargs: 任意关键字参数
        :return: 内容、格式、错误信息
        """
        _ip = kwargs.get('ip', '')
        if _ip == '':
            hosts = Host.objects.all()
            return self.response([host.as_dict() for host in hosts])
        else:
            try:
                host = Host.objects.get(ip=_ip)
                return self.response(host.as_dict())
            except ObjectDoesNotExist as e:
                return self.response(code=404)


    def delete(self, request, *args, **kwargs):
        """获取delete的内容

        :param request: 客户端发送的内容
        :param args: 任意参数
        :param kwargs: 任意关键字参数
        :return: 内容、格式、错误信息
        """
        _ip = kwargs.get('ip', '')
        if _ip != '':
            try:
                host = Host.objects.get(ip=_ip)
                host.delete(_ip)
                return self.response(host.as_dict())
            except ObjectDoesNotExist as e:
                pass

        return self.response(code=404)


class ResourceView(APIView):

    def post(self, request, *args, **kwargs):
        """获取post的内容

        :param request: 客户端发送的内容
        :param args: 任意参数
        :param kwargs: 任意关键字参数
        :return: 内容、格式、错误信息
        """
        _ip = kwargs.get('ip', '')
        _Json = self.get_json()
        mon_res = Monitor_Resource.create_or_replace(
                                _ip, \
                                _Json.get('process_isalive', ''), \
                                _Json.get('process_cpu_use', ''), \
                                _Json.get('process_mem_free', ''), \
                                _Json.get('cpu_total_use', 0), \
                                _Json.get('mem_free', 0), \
                                _Json.get('disk_read', 0), \
                                _Json.get('disk_write', 0), \
                                _Json.get('network_upload', 0), \
                                _Json.get('network_download', 0), \
                                _Json.get('volume', '[]'),
                            )

        return self.response(mon_res.as_dict())