from django.shortcuts import render, render_to_response
from control_robot import Control_Robot as Robot
from control_vision import Control_Vision
from control_sensor import Control_Sensor
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.


"""
control sensor database
"""
def control_sensor(request, cmd):
    _cmd_list = ['add', 'update', 'delete']
    
    if cmd == _cmd_list[0]: #add
        Control_Sensor(request).add()
    elif cmd == _cmd_list[1]: #update
        Control_Sensor(request).update()
    elif cmd == _cmd_list[2]: #delete
        Control_Sensor(request).delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))