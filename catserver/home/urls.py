#-*- coding:utf-8 -*-
from django.contrib.auth.urls import urlpatterns
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView, TemplateView
from home import views
from catserver import settings

urlpatterns = [
                       url(r'^$', views.dashboard, name="index"),
                       
                       #for sidemenu
                       url(r'^vision/$', views.vision, name="vision"),
                       url(r'^setting/log/$', views.setting_log, name="setting_log"),
                       url(r'^setting/system$', views.setting_system, name="setting_system"),
                       url(r'^setting/sensor$', views.setting_sensor, name="setting_sensor"),
                       url(r'^control/$', views.control, name="control"),
                       url(r'^sensor/$', views.sensor, name="sensor"),
                       url(r'^logdb/$', views.logdb, name="logdb"),
                       url(r'^sensordetail/(?P<uid>.*)$', views.sensordetail, name="sensordetail"),
                       url(r'^dashboard/$', views.dashboard, name="dashboard"),
                       
                       
                       #for load static files
                       #url('^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
                       
                       ]

#urlpatterns += staticfiles_urlpatterns()