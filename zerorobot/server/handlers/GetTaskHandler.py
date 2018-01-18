# THIS FILE IS SAFE TO EDIT. It will not be overwritten when rerunning go-raml.

import json

from zerorobot import service_collection as scol
from zerorobot.server.handlers.views import task_view


def GetTaskHandler(task_guid, service_guid):
    '''
    Retrieve the detail of a task
    It is handler for GET /services/<service_guid>/task_list/<task_guid>
    '''
    try:
        service = scol.get_by_guid(service_guid)
    except KeyError:
        return json.dumps({'code': 404, 'message': "service with guid '%s' not found" % service_guid}), \
            404, {"Content-type": 'application/json'}

    try:
        task = service.task_list.get_task_by_guid(task_guid)
    except KeyError:
        return json.dumps({'code': 404, 'message': "task with guid '%s' not found" % task_guid}), \
            404, {"Content-type": 'application/json'}

    return json.dumps(task_view(task, service)), 200, {"Content-type": 'application/json'}