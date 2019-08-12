# encoding: utf-8
import os
import json
import shutil

from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
import ansible.constants as C

from django.core.management import BaseCommand
from django.conf import settings

from asset.models import Host,Host_All

class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        if result.task_name == 'collect_host':
            self.collect_host(result._result)
            self.collect_host_all(result._result)


    def collect_host(self, result):
        facts = result.get('ansible_facts', {})
        resource = {
            'ip' : facts.get('ansible_default_ipv4', {}).get('address', ''),
            'name' : facts.get('ansible_nodename', ''),
            'os' : facts.get('ansible_lsb', {}).get('description', ''),
            'kernel' : facts.get('ansible_kernel', ''),
            'cpu_number' : facts.get('ansible_processor_count', 0),
            'cpu_core': facts.get('ansible_processor_cores', 0),
            'cpu_vcore': facts.get('ansible_processor_vcpus', 0),
            'arch' : facts.get('ansible_architecture', ''),
            'mem_size': str(int(facts.get('ansible_memtotal_mb', 0)) // 1024)+'GB',
            'disk_info': [ { k : v.get('size', '')} for k,v in facts.get('ansible_devices', {}).items() if "sd" in k]
            }
        Host.create_or_replace(**resource)


    def collect_host_all(self, result):
        facts = result.get('ansible_facts', {})
        resource = {
            'ip' : facts.get('ansible_default_ipv4', {}).get('address', ''),
            'mac' : facts.get('ansible_default_ipv4', {}).get('macaddress', ''),
            'cpu_name' : facts.get('ansible_processor', [])[2],
            'server_producter' : facts.get('ansible_system_vendor', ''),
            'server_name' : facts.get('ansible_product_version', ''),
            'serial' : facts.get('ansible_product_serial', ''),
            'network' : [i for i in facts.get('ansible_interfaces', []) if "veth" not in i and "br" not in i and "d" not in i],
            'partitons' : [ { i.get('device','') : {i.get('mount','') : str(int(i.get('size_total',0)) // 1024 // 1024//1024)+'GB'}}  for i in facts.get('ansible_mounts', {})],
            }
 
        Host_All.create_or_replace(**resource)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        AnsibleOptions = namedtuple('AnsibleOptions', ['connection', 'module_path', 'forks', 'become', 'become_method', 'become_user', 'check', 'diff'])
        ansible_options = AnsibleOptions(connection='smart', module_path=[], forks=10, become=None, become_method=None, become_user=None, check=False, diff=False)

        loader = DataLoader() 
        passwords = {}
        results_callback = ResultCallback()
        inventory = InventoryManager(loader=loader, sources=os.path.join(settings.BASE_DIR, 'etc', 'hosts'))
        variable_manager = VariableManager(loader=loader, inventory=inventory)
        play_source =  {
                'name' : "cmdb",
                'hosts' : 'all',
                'gather_facts' : 'no',
                'tasks' : [
                      {
                        'name' : 'collect_host',
                        'setup' : ''
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
