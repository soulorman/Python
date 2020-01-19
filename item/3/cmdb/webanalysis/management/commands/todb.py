# encoding: utf-8

import os
import json
import time
import traceback
 
from django.core.management import BaseCommand
from django.conf import settings
from datetime import datetime
from webanalysis.models import AccessLog


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, 'media', 'notices')
        while True:
            lists = os.listdir(path)

            for filename in lists:
                notice = None
                path_notice = os.path.join(path, filename)
                with open(path_notice, 'rt') as f:
                    notice = json.loads(f.read())

                try:
                    self.parse(notice)
                except BaseException as e:
                    print(e)
                    print(traceback.format_exc())
                
                os.unlink(path_notice)

            time.sleep(5)


    def parse(self, notice):
        file_id = notice['id']
        path = notice['path']

        with open(path, 'rt') as f:
            for line in f:
                try:
                    nodes = line.split()
                    log = AccessLog()
                    log.file_id = file_id
                    log.access_time = datetime.strptime(nodes[3], '[%d/%b/%Y:%H:%M:%S').strftime('%Y-%m-%d %H:%M:%S')
                    log.ip = nodes[0]
                    log.url = nodes[6]
                    log.status_code = nodes[8]
                    log.save()
                except BaseException as e:
                    print(e)
                    print(line)
        print('parse over : {}'.format(path))
