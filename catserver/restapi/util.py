#-*- coding:utf-8 -*-

import platform
import socket
#import multiprocessing
import psutil
import os
import commands

class Host(object):
    
    def __init__(self):
        self.system_info = {}
    
    def __del__(self):
        pass
    
    def getIPAddress(self, adapter):
        try:
            if platform.system() == 'Windows':
                return socket.gethostbyname(socket.gethostname())
            else:
                return commands.getoutput("ifconfig %s"%adapter).split("\n")[1].split()[1][5:]
        except Exception, e:
            print "Exception : ",e
            return "0.0.0.0"
            

    
    def getSystemInfo(self):
        self.system_info['python_version'] = platform.python_version()
        self.system_info['python_compiler'] = platform.python_compiler()
        self.system_info['python_build'] = platform.python_build()
        
        #self.system_info['platform_cores'] = multiprocessing.cpu_count()
        self.system_info['platform_memory_capacity'] = str(psutil.virtual_memory().total/1.073741824e9)+" GByte"
        self.system_info['platform_memory_percent'] = psutil.virtual_memory().percent
        self.system_info['platform_memory_used'] = str(psutil.virtual_memory().total*psutil.virtual_memory().percent/100/1.073741824e9)+" GByte"
        self.system_info['platform_memory_available'] = str(psutil.virtual_memory().total*(100-psutil.virtual_memory().percent)/100/1.073741824e9)+" GByte"
        
        self.system_info['platform_cpu_percent'] = psutil.cpu_percent(interval=None)
        self.system_info['platform_cpu_count'] = psutil.cpu_count()
        
        if platform.system() == 'Windows':
            self.system_info['platform_disk_capacity'] = "Not Implemented"
            self.system_info['platform_disk_available'] = "Not Implemented"
            self.system_info['platform_disk_used'] = "Not Implemented"
            self.system_info['platform_disk_percent'] = "Not Implemented"
        else:
            disk = os.statvfs("/")
            self.system_info['platform_disk_capacity'] = str(disk.f_bsize * disk.f_blocks / 1.073741824e9)+" GBytes"
            self.system_info['platform_disk_available'] = str(disk.f_bsize * disk.f_bavail / 1.073741824e9)+" GBytes"
            self.system_info['platform_disk_used'] = str(disk.f_bsize * (disk.f_blocks - disk.f_bavail) / 1.073741824e9)+" GBytes"
            self.system_info['platform_disk_percent'] = "%0.4s%%"%((disk.f_bsize * (disk.f_blocks - disk.f_bavail) / 1.073741824e9)/(disk.f_bsize * disk.f_blocks / 1.073741824e9)*100)
        

        self.system_info['os'] = platform.platform(aliased=True)
        self.system_info['os_system'] = platform.system()
        self.system_info['os_node'] = platform.node()
        self.system_info['os_release'] = platform.release()
        self.system_info['os_version'] = platform.version()
        self.system_info['os_machine'] = platform.machine()
        self.system_info['os_processor'] = platform.processor()
        
        self.system_info['host_name'] = socket.gethostname()
        
        return self.system_info

    
    