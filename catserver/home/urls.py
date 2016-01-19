#-*- coding:utf-8 -*-
from django.contrib.auth.urls import urlpatterns
from django.conf.urls import patterns, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic.base import RedirectView, TemplateView
from home import views
from catserver import settings

urlpatterns = [
                       url(r'^$', views.index, name="index"),
                       
                       #for authentication
                       url(r'^signin/$', views.signin, name="signin"),
                       url(r'^sign/$', views.sign, name="sign"),
                       url(r'^signout/$', views.signout, name="signout"),
                       
                       #for sidemenu
                       url(r'^products/$', views.products, name="products"),
                       url(r'^components/$', views.components, name="components"),
                       url(r'^apps/$', views.apps, name="apps"),
                       url(r'^solutions/$', views.solutions, name="solutions"),
                       url(r'^developer/$', views.developers, name="developers"),
                       url(r'^documents/$', views.documents, name="documents"),
                       url(r'^support/$', views.support, name="support"),
                       url(r'^contact/$', views.contact, name="contact"),
                       url(r'^tutorial/(?P<page>[\.\w-]+)$', views.tutorial, name="tutorial"),
                       url(r'^manage/$', views.manage, name="manage"),
                       
                       #for load static files
                       url('^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root':settings.STATIC_ROOT}),
                       
                       ]

#urlpatterns += staticfiles_urlpatterns()