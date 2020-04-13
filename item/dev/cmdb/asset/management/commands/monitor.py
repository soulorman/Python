#encoding: utf-8
import time
import requests
import json

from django.core.management import BaseCommand
from asset.models import Monitor_Resource
from asset.error_info import get_error_info
from django.utils import timezone
from datetime import timedelta


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        """监控进程

        :param: 接受所有参数
        :return: 无
        """
        while True:
            end_time = timezone.now()
            start_time = end_time - timedelta(hours=24)
            info = Monitor_Resource.objects.values('ip').distinct()
            for i in info:
                _ip = i['ip']
                _time = start_time
                error_info = get_error_info(_ip, _time)
                if error_info:
                    self.ding_push_message(error_info)

            time.sleep(10)


    def ding_push_message(self, err_info):
        """报错发送钉钉群

        :param err_info:报错信息
        :return: 无
        """
        # 请求的URL，WebHook地址
        web_url = "https://oapi.dingtalk.com/robot/send?access_token=312f10cdc9912967aff99ace779f6e3702fc40f9b7798d1655818def3cf4be01"
        # 构建发送消息
        msg = ''
        for e in err_info:
            str_info = "报错:   " + e[0]
            str_actual = "实值:   " + e[1]
            str_time = "时间:   " + e[2]
            length = (len(str_time) + 5) * '-'
            msg += str_info + "\n" + str_actual + "\n" + str_time + "\n" + length + "\n"   

        header = {
            "Content-Type": "application/json",
            "Charset": "UTF-8"
        }
    
        message = {
            "msgtype": "text",
            "text": {
                "content": msg
            },
            "at": {
                "isAtAll": True
            }
        }
        
        message_json = json.dumps(message)
        info = requests.post(url=web_url, data=message_json, headers=header)

        return info