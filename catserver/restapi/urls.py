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
    url(r'^vision/$', views.vision_update, name='vision_update'),
]

#urlpatterns += staticfiles_urlpatterns()