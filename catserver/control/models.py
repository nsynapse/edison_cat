#-*- coding:utf-8 -*-

from django.db import models

"""
DB Model(abstract) for filepath storing
"""
class DBFile(models.Model):
    filepath = models.CharField(max_length=200, blank=False, default="")
    
    def __unicode__(self):
        return self.filepath
    class Meta:
        abstract = True
        
        
class DBImageFile(DBFile):
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return DBFile.__unicode__(self)
    class Meta:
        ordering = ["-date"]
        
        
class DBGestureFile(DBFile):
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return DBFile.__unicode__(self)
    class Meta:
        ordering = ["-date"]
        
        
class DBSystemInfo(models.Model):
    net_address = models.CharField(max_length=20, blank=False, default="")
    net_if = models.CharField(max_length=20, blank=False, default="")
    websocket_port = models.IntegerField(blank=False, default=9002)
    
    def __unicode__(self):
        return self.net_address
        
    
    
class DBLogFile(DBFile):
    def __unicode__(self):
        return DBFile.__unicode__(self)

"""
Sensor Log Database
"""    
class DBSensorLogFile(DBFile):
    def __unicode__(self):
        return DBFile.__unicode__(self)
        
        
"""
Sensor device data
"""
class DBSensor(models.Model):
    uid = models.CharField(max_length=64, blank=False, default="")
    name = models.CharField(max_length=100, blank=False, default="")
    min = models.FloatField(blank=False, default=-1.0)
    max = models.FloatField(blank=False, default=1.0)
    unit = models.CharField(max_length=20, blank=False, default="")
    length = models.IntegerField(blank=False, default=100)
    
    def __unicode__(self):
        return self.name
        
        