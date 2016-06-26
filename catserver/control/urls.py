#-*- coding:utf-8 -*-
from django.contrib.auth.urls import urlpatterns
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView, TemplateView
from control import views
from catserver import settings

urlpatterns = [
               url(r'^sensor/(?P<cmd>.*)$', views.control_sensor, name="control_sensor"),
               url(r'^system/(?P<cmd>.*)$', views.control_system, name="control_system"),
               #url(r'^vision/(?P<cmd>[\.\w-]+)$', views.control_vision, name='control_vision'),
               #url(r'^robot/(?P<cmd>[\.\w-]+)$', views.control_robot, name='control_robot'),
               ]
