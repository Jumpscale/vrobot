from js9 import j

from . import (PRIORITY_NORMAL, PRIORITY_RECURRING, PRIORITY_SYSTEM,
               TASK_STATE_ERROR, TASK_STATE_NEW, TASK_STATE_OK,
               TASK_STATE_RUNNING)
from .task import Task


def _instantiate_task(task, service):
    func = getattr(service, task['action_name'])
    t = Task(func, task['args'], resp_q=None)
    if task['state'] in [TASK_STATE_RUNNING, TASK_STATE_NEW]:
        t.state = TASK_STATE_NEW
    else:
        t.state = task['state']
    t.guid = task['guid']
    if task['eco']:
        t.eco = j.core.errorhandler.getErrorConditionObject(ddict=task['eco'])
    if task['result']:
        t._result = task['result']
    return t