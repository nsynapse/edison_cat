#-*- coding:utf-8 -*-
from models import DBSensor as DB
import uuid
    
class Control_Sensor(object):
    
    def __init__(self, request):
        self.request = request
    
    def __del__(self):
        pass
    
    def add(self):
        if self.request.method == 'POST':
            try:
                new_db = DB()
                new_db.uid = uuid.uuid4().hex
                new_db.name = self.request.POST.get('device_name','')
                new_db.min = self.request.POST.get('min',0)
                new_db.max = self.request.POST.get('max',1)
                new_db.save()
                print "Add new sensor device"
                return True
            except Exception, e:
                print "Exception : ", e
                new_db.delete()
                
        return False
                
    
    def delete(self):
        if self.request.method == 'POST':
            try:
                _uid = self.request.POST['device_uid']
                _device = DB.objects.filter(uid=_uid)
                
                if _device.exists():
                    _device[0].delete()
                    return True
            except Exception, e:
                print "Exception : ", e
        return False
    
    def update(self):
        pass