#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response, render
from django.template.context import RequestContext
from django.contrib import auth
from django.template.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from control.models import DBSensor, DBSystemInfo
import psutil

# render index page
def index(request):
    return render(request, "index.html")
    #return render_to_response("index.html", context=RequestContext(request))
    
    
"""
dashboard menu
"""
# side menus
def dashboard(request):
    return render(request, "dashboard.html")
    #return render_to_response("dashboard.html", context=RequestContext(request))

"""
vision menu
"""
def vision(request):
    return render(request, "vision.html")
    #return render_to_response("vision.html", context=RequestContext(request))

"""
control menu
"""
def control(request):
    system = DBSystemInfo.objects.all()
    return render(request, "control.html", {'system':system})
    #return render_to_response("control.html", context=RequestContext(request))

"""
sensor menu
"""
def sensor(request):
    all_sensors = DBSensor.objects.all()
    system = DBSystemInfo.objects.all()
    return render(request, "sensor.html", {'sensors':all_sensors, 'system':system})
    #return render_to_response("sensor.html", {'sensors':all_sensors, 'system':system}, context=RequestContext(request))
"""
log database menu
"""
def logdb(request):
    return render(request, "logdb.html")
    #return render_to_response("logdb.html", context=RequestContext(request))

"""
sensor monitoring in detail
"""
def sensordetail(request, uid):
    system = DBSystemInfo.objects.all()
    sensor = DBSensor.objects.filter(uid=uid)[0]
    return render(request, "sensordetail.html", {'sensor':sensor, 'system':system})
    #return render_to_response("sensordetail.html", {'sensor':sensor, 'system':system}, context=RequestContext(request))

"""
log setting menu
"""
def setting_log(request):
    return render(request, "setting_log.html")
    #return render_to_response("setting_log.html", context=RequestContext(request))

"""
system setting menu
"""
def setting_system(request):
    nets = psutil.net_if_addrs()
    system = DBSystemInfo.objects.all()
    return render(request, "setting_system.html", {'nets':nets, 'system':system})

"""
sensor setting menu
"""
def setting_sensor(request):
    all_sensors = DBSensor.objects.all()
    return render(request, "setting_sensor.html", {'sensors':all_sensors})
    #return render_to_response("setting_sensor.html", {'sensors':all_sensors}, context=RequestContext(request))

#