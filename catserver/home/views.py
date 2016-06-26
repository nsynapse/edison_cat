#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib import auth
from django.template.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from control.models import DBSensor, DBSystemInfo
import psutil

# render index page
def index(request):
    return render_to_response("index.html", context_instance=RequestContext(request))
    
    
# side menus
def dashboard(request):
    return render_to_response("dashboard.html", context_instance=RequestContext(request))

def vision(request):
    return render_to_response("vision.html", context_instance=RequestContext(request))

def control(request):
    return render_to_response("control.html", context_instance=RequestContext(request))

def sensor(request):
    all_sensors = DBSensor.objects.all()
    system = DBSystemInfo.objects.all()
    return render_to_response("sensor.html", {'sensors':all_sensors, 'system':system}, context_instance=RequestContext(request))

def setting_log(request):
    return render_to_response("setting_log.html", context_instance=RequestContext(request))

def setting_system(request):
    nets = psutil.net_if_addrs()
    system = DBSystemInfo.objects.all()
    return render_to_response("setting_system.html",{'nets':nets, 'system':system}, context_instance=RequestContext(request))

def setting_sensor(request):
    all_sensors = DBSensor.objects.all()
    return render_to_response("setting_sensor.html", {'sensors':all_sensors}, context_instance=RequestContext(request))

#