#enconding: utf-8

import json
import os
import shutil
from collections import namedtuple

from django.core.management import BaseCommand
from django.conf import settings

from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C
from asset.models import Host,Resource,Host_All,Monitor

class ResultCallback(CallbackBase):

    def __init__(self):
        super(ResultCallback, self).__init__()
        self._cache_host = {}

    def v2_runner_on_ok(self, result, **kwargs):
        if result.task_name == 'collect_host':
            facts = result._result.get('ansible_facts', {})
            ip = facts.get('ansible_default_ipv4', {}).get('address', '')
            self._cache_host[result._host.name] = ip
        elif result.task_name == 'collect_monitor':
            ip = self._cache_host.get(result._host.name)
            monitor_info = eval(result._result.get('stdout_lines','')[0])
            self.collect_monitor(ip,**monitor_info)


    def collect_monitor(self, ip, **result):
            self.ip =  ip
            isalive = result.get('isalive','')
            cpu = result.get('cpu','')
            mem = result.get('mem','')

            cpu_use = result.get('cpu_use',0)
            mem_free = result.get('mem_free',0)
            disk_read = result.get('disk_read',0)
            disk_write = result.get('disk_write',0)
            upload_success = result.get('upload_success',0)
            yuce_success = result.get('yuce_success',0)
            network = result.get('network_info',[])
            Monitor.create_or_replace(self.ip,isalive,cpu,mem,cpu_use,mem_free,disk_read,disk_write,upload_success,yuce_success,network)

class Command(BaseCommand):
    def handle(self, *args, **options):
        AnsibleOptions = namedtuple('AnsibleOptions', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
        ansible_options = AnsibleOptions(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
        loader = DataLoader() 
        passwords = {}
        results_callback = ResultCallback()
        inventory = InventoryManager(loader=loader, sources=os.path.join(settings.BASE_DIR,'etc','hosts'))
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        path_resource = '/tmp/collect_cmdb_monitor.sh'

        play_source =  {
                'name' : "cmdb",
                'hosts' : 'all',
                'gather_facts' : 'no',
                'tasks' : [
                    {
                      'name' : 'collect_host',
                      'setup' : ''
                    },
                    {
                      'name' : 'copyfile',
                      'copy' : 'src={0} dest={1} mode=700'.format(os.path.join(settings.BASE_DIR, 'etc', 'collect_monitor.sh'), path_resource)
                    },
                    {
                      'name' : 'collect_monitor',
                      'command' : '/bin/bash {0}'.format(path_resource)
                    }
              ]
            }

        play = Play().load(play_source, variable_manager=variable_manager, loader=loader)
        tqm = None
        try:
            tqm = TaskQueueManager(
                      inventory=inventory,
                      variable_manager=variable_manager,
                      loader=loader,
                      options=ansible_options,
                      passwords=passwords,
                      stdout_callback=results_callback,
                  )
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

            shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)
