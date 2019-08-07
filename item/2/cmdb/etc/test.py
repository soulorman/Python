#encoding: utf-8

import json
import shutil
from ansible.module_utils.common.collections import ImmutableDict
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager
from ansible.plugins.callback import CallbackBase
from ansible import context
import ansible.constants as C


class ResultCallback(CallbackBase):
    def v2_runner_on_ok(self, result, **kwargs):
        host = result._host
        print(result.task_name)
        print(json.dumps({host.name: result._result}, indent=4))


context.CLIARGS = ImmutableDict(connection='smart', module_path=[], forks=10, become=None,
                                become_method=None, become_user=None, check=False, diff=False)

loader = DataLoader() 
passwords = {}

results_callback = ResultCallback()

inventory = InventoryManager(loader=loader, sources='hosts')

variable_manager = VariableManager(loader=loader, inventory=inventory)

play_source =  {
        'name' : "test",
        'hosts' : 'all',
        'gather_facts' : 'no',
        'tasks' : [
              {
                'name' : 'fact',
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
              passwords=passwords,
              stdout_callback=results_callback,  
          )
    result = tqm.run(play)
finally:
    if tqm is not None:
        tqm.cleanup()

    shutil.rmtree(C.DEFAULT_LOCAL_TMP, True)