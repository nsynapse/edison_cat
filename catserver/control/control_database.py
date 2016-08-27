#-*- coding:utf-8 -*-
from models import DBSensor as DB
import uuid
    
class Control_Database(object):
    
    def __init__(self, request):
        self.request = request
    
    def __del__(self):
        pass
    
    def list(self):
        return False
    
    