#encoding: utf-8

import json
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from asset.models import Host,Resource

class APIView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(APIView, self).dispatch(request, *args, **kwargs)

    def get_json(self):
        try:
            return json.loads(self.request.body.decode('utf-8'))
        except BaseException as e:
            return {}

    def response(self, result=None, code=200, errors={}):

        return JsonResponse({'code': code, 'result' : result, 'errors' : errors})
        

class ClientView(APIView):

    def post(self, request, *args, **kwargs):
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
                                        _Json.get('mem_size', ''), \
                                        _Json.get('disk_info', '{}')
                                    )
        return self.response(host.as_dict())


class ResourceView(APIView):

    def post(self, request, *args, **kwargs):
        _ip = kwargs.get('ip', '')
        _Json = self.get_json()

        Resource.create_obj(
                                _ip, \
                                _Json.get('cpu', ''), \
                                _Json.get('mem', '')
                            )
        return self.response()