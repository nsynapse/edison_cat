#-*- coding:utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework import routers
from restapi import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)

urlpatterns = [
    #url(r'^u/(?P<cmd>[\.\w-]+)$',login_required(control_user),{}, name="control_user" ),
    
    #url(r'^building$', views.building_status, name='building_status'),
                    
]

#urlpatterns += staticfiles_urlpatterns()