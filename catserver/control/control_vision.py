#-*- coding:utf-8 -*-

from django.http.response import HttpResponse, HttpResponseRedirect
from control import models
from cv2 import *
from catserver import settings
from datetime import datetime
from models import DBImageFile

class Control_Vision(object):
    def __init__(self, request):
        self.request = request
        
    def __del__(self):
        pass
    
    def capture(self):
        try:
            cam = VideoCapture(0)
            s, image = cam.read()
            _time = datetime.now()
            tstamp = _time.strftime("%Y-%m-%d_%H:%M:%S:%f")
            success_filepath = tstamp+"_capture.jpg"
            fail_filepath = "no_image.jpg"
            ret = imwrite(settings.STATIC_DATA_ROOT+"/"+success_filepath, image)
            if ret is True:
                db = DBImageFile()
                db.filepath = success_filepath
                db.save()
                return success_filepath
            else:
                return fail_filepath
        except Exception, e:
            print "Exception : ", e
            
            