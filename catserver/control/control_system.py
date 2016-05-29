#-*- coding:urf-8 -*-

class Control_System(object):
    def __init__(self, request):
        pass
    
    def __del__(self):
        pass
    
    def update(self, info):
        if type(info)==dict:
            print "type ok"