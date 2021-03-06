#-*- coding:utf-8 -*-
from models import DBSensor as DB
import uuid
    
class Control_Sensor(object):
    
    def __init__(self, request):
        self.request = request
    
    def __del__(self):
        pass
    
    """
    Add new sensor into database
    """
    def add(self):
        if self.request.method == 'POST':
            try:
                new_db = DB()
                new_db.uid = uuid.uuid4().hex
                new_db.name = self.request.POST.get('sensor_name','')
                try:
                    new_db.min = float(self.request.POST.get('sensor_range_min',0.0))
                except ValueError:
                    new_db.min = 0.0
                
                try:
                    new_db.max = float(self.request.POST.get('sensor_range_max',1.0))
                except ValueError:
                    new_db.max = 1.0
                    
                try:
                    new_db.unit = self.request.POST.get('sensor_data_unit','')
                except ValueError:
                    new_db.unit = ''
                    
                try:
                    new_db.buffersize = int(self.request.POST.get('sensor_data_buffer_size',100))
                except ValueError:
                    new_db.buffersize = 100;
                        
                
                new_db.save()
                return True
            except Exception, e:
                print "Exception : ", e
                
        return False
                
    """
    Delete device in database
    """
    def delete(self):
        if self.request.method == 'POST':
            try:
                _uid = self.request.POST.get('sensor_uid','')
                _sensor = DB.objects.filter(uid=_uid)
            
                if _sensor.exists():
                    _sensor[0].delete()
                    return True
            except Exception, e:
                print "Exception : ", e
        return False
    
    """
    Update sensor information
    """
    def update(self):
        if self.request.method == 'POST':
            try:
                _uid = self.request.POST.get('sensor_uid','')
                _sensor = DB.objects.get(uid=_uid)
                if _sensor is not None:
                    _sensor.name = self.request.POST.get('sensor_name','')
                    try:
                        _sensor.min = float(self.request.POST.get('sensor_range_min',0.0))
                    except ValueError:
                        _sensor.min = 0.0
                        
                    try:
                        _sensor.max = float(self.request.POST.get('sensor_range_max',1.0))
                    except ValueError:
                        _sensor.max = 1.0
                    
                    try:
                        _sensor.unit = self.request.POST.get('sensor_data_unit','')
                    except ValueError:
                        _sensor.unit = ''
                        
                    try:
                        _sensor.buffersize = self.request.POST.get('sensor_data_buffer_size',100)
                    except:
                        _sensor.buffersize = 100;
                        
                    _sensor.save()
                    return True
            except Exception, e:
                print "Exception(Sensor update) : ", e
        return False
                    
    
    """
    Getting sensor information from database
    """
    def getInfo(self, sensor_uid):
        if self.request.method == 'GET':
            _response = {}
            try:
                _sensor = DB.objects.filter(uid=sensor_uid)
                if _sensor.exists():
                    _response['sensor_name'] = _sensor[0].name
                    _response['sensor_uid'] = _sensor[0].uid
                    _response['sensor_range_min'] = _sensor[0].min
                    _response['sensor_range_max'] = _sensor[0].max
                    _response['sensor_data_unit'] = _sensor[0].unit
                    _response['sensor_data_buffer_size'] = _sensor[0].buffersize
                    return _response
                else:
                    print sensor_uid + " does not exist"
            except Exception, e:
                print "Exception(Sensor getInfo) : ", e
                
        return None
    
    
    