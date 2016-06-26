#-*- coding:utf-8 -*-

from models import DBSystemInfo as DB
import psutil

class Control_System(object):
    def __init__(self, request):
        self.request = request
    
    def __del__(self):
        pass
    
    def update(self):
        if self.request.method == 'POST':
            try:
                _net_if = self.request.POST.get('net_if','')
                
                if DB.objects.exists():
                    _db = DB.objects.latest('id')
                    _db.net_if = _net_if
                    _nets = psutil.net_if_addrs()
                    _db.net_address = _nets[_net_if][0].address
                    _db.websocket_port = self.request.POST.get('websocket_port',9002)
                    _db.save()
                else:
                    _new_db = DB()
                    _new_db.net_if = self.request.POST.get('net_if','')
                    _new_db.websocket_port = self.request.POST.get('websocket_port',9002)
                    _nets = psutil.net_if_addrs()
                    _new_db.net_address = _nets[_net_if][0].address
                    _new_db.save()
                
                return True
                    
            except Exception, e:
                print "Exception(Control_System update) : ", e
        
        return False
            
            