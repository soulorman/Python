#encoding: utf-8

import redis
import json

from django.conf import settings

from django.core.management import BaseCommand
from asset.models import Host, Host_All, Resource

class Command(BaseCommand):

    def handle(self, *args, **options):
        conn = redis.StrictRedis(**settings.REDIS)
        while True:
            rt = conn.brpop('cmdb:asset:client:todb', timeout=5)
            if rt is None:
                continue
            _context = json.loads(rt[1])
            _ip = _context.get('ip', '')
            _Json = _context.get('json', '{}')

            Host.create_or_replace( 
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

