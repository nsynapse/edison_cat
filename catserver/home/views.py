#-*- coding:utf-8 -*-

from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.contrib import auth
from django.template.context_processors import csrf
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

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
    return render_to_response("sensor.html", context_instance=RequestContext(request))

def setting_log(request):
    return render_to_response("setting_log.html", context_instance=RequestContext(request))

def setting_system(request):
    return render_to_response("setting_system.html", context_instance=RequestContext(request))

def setting_sensor(request):
    return render_to_response("setting_sensor.html", context_instance=RequestContext(request))

#