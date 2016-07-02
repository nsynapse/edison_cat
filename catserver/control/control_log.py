#-*- coding:utf-8 -*-

class Control_Log(object):
    def __init__(self, request):
        self.request = request
    
    def __del__(self):
        pass
    
    """
    realtime sensor monitoring
    """
    def monitor(self):
        if self.request.method == 'GET':
            pass
        pass
    
    """
    view log
    """
    def view(self):
        if self.request.method == 'GET':
            pass
        pass