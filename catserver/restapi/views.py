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
@api_view(['GET'])
def network_command(request, cmd):
    _response = {}
    if request.method == 'GET':
        try:
            return Response(_response, status.HTTP_200_OK)
        except Exception, e:
            print "Exception(network) : ", e
    else:
        return Response(_response, status.HTTP_400_BAD_REQUEST)
    
    return Response(_response, status.HTTP_404_NOT_FOUND)



