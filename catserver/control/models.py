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
        return self.filepath
    class Meta:
        ordering = ["-date"]
        
        
class DBGestureFile(DBFile):
    date = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.filepath
    class Meta:
        ordering = ["-date"]
        
        