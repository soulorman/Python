#encoding: utf-8

import json
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from asset.models import Host


class ClientView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super(ClientView, self).dispatch(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
        _json = {}
        try:
            _json = json.loads(request.body)
        except BaseException as e:
            pass
        host = Host.create_or_replace(
                        _json.get('ip',''),\
                        _json.get('name',''),\
                        _json.get('mac',''),\
                        _json.get('os',''),\
                        _json.get('kernel',''),\
                        _json.get('cpu_core',0),\
                        _json.get('cpu_thread',0),\
                        _json.get('arch',''),\
                        _json.get('mem',0),\
                        _json.get('cpu',0),\
                        _json.get('disk','{}'))
        return JsonResponse({'code' : 200, "result" : host.as_dict(),'errors' : {}})
