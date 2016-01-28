#-*- coding:utf-8 -*-

from django.db import models

"""
DB Model(abstract) for filepath storing
"""
class File(models.Model):
    filepath = models.CharField(max_length=100, blank=False, default="")
    
    def __unicode__(self):
        return self.filepath
    class Meta:
        abstract = True
        
        
class ImageFile(File):
    date = models.DateTimeField(null=True, blank=True)
    
    def __unicode__(self):
        return self.filepath
    class Meta:
        ordering = ["-filepath"]