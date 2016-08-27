#-*- coding:utf-8 -*-

from django.shortcuts import render, render_to_response
from control_robot import Control_Robot as Robot
from control_vision import Control_Vision
from control_sensor import Control_Sensor
from control_system import Control_System
from control_database import Control_Database
#from control_log import Control_Log
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


"""
Control system database
"""
def control_system(request, cmd):
    _cmd_list = ['update']
    if cmd == _cmd_list[0]: #update
        Control_System(request).update()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


"""
Control log database
"""
def control_database(request, cmd):
    _cmd_list = ['list']
    if cmd == _cmd_list[0]: #list
        Control_Database(request).list()
        
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))





"""
Control Sensor Log
"""
"""
def control_log(request, cmd):
    _cmd_list = ['monitor', 'view']
    if cmd == _cmd_list[0]: #Monitor
        Control_Log(request).monitor()
    elif cmd == _cmd_list[1]: #view
        Control_Log(request).view()
"""