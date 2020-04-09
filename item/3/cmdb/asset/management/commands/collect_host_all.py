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
from asset.models import Host,Host_All

class ResultCallback(CallbackBase):
    def __init__(self):
        super(ResultCallback, self).__init__()
        self._cache_host = {}

    def v2_runner_on_ok(self, result, **kwargs):
        if result.task_name == 'collect_host':
            facts = result._result.get('ansible_facts', {})
            ip = facts.get('ansible_default_ipv4', {}).get('address', '')
            self._cache_host[result._host.name] = ip
        elif result.task_name == 'collect_hard_info':
            ip = self._cache_host.get(result._host.name)
            hard_info = eval(result._result.get('stdout_lines','')[0])

            self.collect_host(ip,**hard_info)


    def collect_host(self, ip, **result):
            self.ip =  ip
            gpu_info = result.get('Gpu_info',[])[0]
            network  = result.get('Network_Info', [])
            mem_scalable = result.get('Mem_scalable',0)
            mem_slot =  result.get('Mem_slot_Number',0)
            server_type =  result.get('Server_Type','')
            server_producter = result.get('Server_Producter','')
            server_number = result.get('Server_Number', 0)
            cpu_type = result.get('Cpu_Type',{})
            root = result.get('Root_Size','')
            data = result.get('Data_Size', ['无'])

            Host_All.create_or_replace(self.ip, cpu_type, mem_scalable, mem_slot, server_type, server_producter, server_number, gpu_info, network, root, data)


class Command(BaseCommand):
    def handle(self, *args, **options):
        AnsibleOptions = namedtuple('AnsibleOptions', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
        ansible_options = AnsibleOptions(connection='local', module_path=['/to/mymodules'], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)
        loader = DataLoader()
        passwords = {}
        results_callback = ResultCallback()
        inventory = InventoryManager(loader=loader, sources=os.path.join(settings.BASE_DIR,'etc','hosts'))
        variable_manager = VariableManager(loader=loader, inventory=inventory)

        path_collect_host = '/tmp/collect_host_cmdb.sh'
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
                        'name' : 'copy_file',
                        'copy' : 'src={0} dest={1} mode=700'.format(os.path.join(settings.BASE_DIR, 'etc', 'collect_host.sh'), path_collect_host)
                    },
                    {
                        'name' : 'collect_hard_info',
                        'command' : '/bin/bash {0}'.format(path_collect_host)
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
