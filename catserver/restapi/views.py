#-*- coding:utf-8 -*-

from django.shortcuts import render
from datetime import datetime
from rest_framework.renderers import JSONRenderer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from util import Host
from control.control_vision import Control_Vision
from control.control_sensor import Control_Sensor
from rest_framework.status import HTTP_400_BAD_REQUEST
from api_log import API_Log


"""
API for system status
"""
@api_view(['GET'])
def system_update(request):
    
    _response = {"date":"-", "ipaddress":""}
    
    if request.method == 'GET':
        try:
            _time = datetime.now()
            _host = Host()
            _info = _host.getSystemInfo()
            _info["wlan0"] = _host.getIPAddress("wlan0")
            _info["eth0"] = _host.getIPAddress("eth0")
            _response["date"] = _time.strftime("%Y-%m-%d %H:%M:%S")
            _response.update(_info)
            
            return Response(_response, status.HTTP_200_OK)

        except Exception, e:
            print "Exception(system) : ",e
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    return Response(_response, status.HTTP_404_NOT_FOUND)

"""
API for camera
"""
@api_view(['GET'])
def camera_command(request, cmd):
    
    _response = {"date":"-", "filepath":""}
    
    if request.method == 'GET':
        try:
            if cmd == "capture":
                vision = Control_Vision(request)
                
                _time = datetime.now()
                _response["date"] = _time.strftime("%Y-%m-%d %H:%M:%S")
                _response["filepath"] = vision.capture() 
            
                return Response(_response, status.HTTP_200_OK)
            else:
                return Response(_response, status.HTTP_200_OK)

        except Exception, e:
            print "Exception(camera) : ",e
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    return Response(_response, status.HTTP_404_NOT_FOUND)


"""
API for vision control
"""
@api_view(['GET'])
def vision_command(request, cmd):
    
    _response = {"date":"-"}
    
    if request.method == 'GET':
        try:
            _time = datetime.now()
            _response["date"] = _time.strftime("%Y-%m-%d %H:%M:%S")
            
            return Response(_response, status.HTTP_200_OK)

        except Exception, e:
            print "Exception(vision) : ",e
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    return Response(_response, status.HTTP_404_NOT_FOUND)


"""
API for network control
"""
@api_view(['GET', 'POST'])
def network_command(request, cmd):
    _response = {}
    if request.method == 'GET':
        try:
            if cmd=="save":
                print request
            return Response(_response, status.HTTP_200_OK)
        except Exception, e:
            print "Exception(network) : ", e
    elif request.method == 'POST':
        print cmd
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    
    return Response(_response, status.HTTP_404_NOT_FOUND)



"""
API for sensor control
"""
@api_view(['GET'])
def sensor_api(request):
    _response = {}
    
    if request.method == 'GET':
        try:
            _q = request.GET.get('q',None)
            _uid = request.GET.get('p',None)
            _response = Control_Sensor(request).getInfo(_uid)
            return Response(_response, status.HTTP_200_OK)
            
        except Exception, e:
            print "Exception(sensor) : ", e
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    
    return Response(_response, status.HTTP_404_NOT_FOUND)
        
        
        
"""
API for log control
"""
@api_view(['GET'])
def log_command(request):
    _response = {}
    
    if request.method == 'GET':
        try:
            _uid = request.GET.get('uid',None)
        except Exception, e:
            print "Exception(log) : ", e
    elif request.method == 'POST':
        try:
            pass
        except Exception, e:
            print "Exception(log) : ", e
    else:
        return Response(_response, status,HTTP_400_BAD_REQUEST)
    
    
    return Response(_response, status.HTTP_404_NOT_FOUND)
        
        
        