#-*- coding:utf-8 -*-
from django.contrib.auth.urls import urlpatterns
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView, TemplateView
from control import views
from catserver import settings

urlpatterns = [
               #url(r'capture/^$', views.dashboard, name="index"),
               #url(r'^vision/(?P<cmd>[\.\w-]+)$', views.control_vision, name='control_vision'),
               #url(r'^robot/(?P<cmd>[\.\w-]+)$', views.control_robot, name='control_robot'),
               ]
