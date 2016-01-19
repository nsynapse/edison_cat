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

# administrator signin for management website
def signin(request):
    csrfdic = {}
    csrfdic.update(csrf(request))
    return render_to_response("signin.html", csrfdic)

def sign(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/signin/')
    
@login_required    
def signout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
    
    
# side menus
def products(request):
    return render_to_response("products.html", context_instance=RequestContext(request))

def components(request):
    return render_to_response("components.html", context_instance=RequestContext(request))

def apps(request):
    return render_to_response("apps.html", context_instance=RequestContext(request))

def solutions(request):
    return render_to_response("solutions.html", context_instance=RequestContext(request))

def developers(request):
    return render_to_response("developer.html", context_instance=RequestContext(request))

def documents(request):
    return render_to_response("documents.html", context_instance=RequestContext(request))

def support(request):
    return render_to_response("supports.html", context_instance=RequestContext(request))

def contact(request):
    return render_to_response("contact.html", context_instance=RequestContext(request))

def tutorial(request, page):
    return render_to_response("tutorial.html", context_instance=RequestContext(request))

def manage(request):
    return render_to_response("manage.html", context_instance=RequestContext(request))
#