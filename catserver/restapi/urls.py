#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^system/$', views.system_update, name='system_update'),
    url(r'^vision/(?P<cmd>.*)$', views.vision_command, name='vision_command'),
    url(r'^sensor/$', views.sensor_api, name='api_sensor'),
    url(r'^camera/(?P<cmd>.*)$', views.camera_command, name='camera_command'),
    url(r'^log/(?P<cmd>.*)$', views.log_command, name='log_command'),
    url(r'^network/(?P<cmd>.*)$', views.network_command, name='network_command'),
]

#urlpatterns += staticfiles_urlpatterns()