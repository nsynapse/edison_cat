#-*- coding:utf-8 -*-

"""
async serial communication based on pySerial
"""
import threading, time
import os
from Queue import Queue, Empty



class AsyncSerial(threading.Thread):
    
    def __init__(self, device):
        self.close = False
        self.device = device
        self.q = Queue() # for thread safety
        
        print "[*] device : {0}".format(self.device.name)

        if self.device.isOpen():
            self.device.flushInput()
            self.device.flushOutput()
            self.device.flush()
            print "[*] {0} device is opened.".format(self.device.name)
            threading.Thread.__init__(self)
        else:
            print "[*] {0} cannot open. module will be terminated.".format(self.dev_serial.name)
            os._exit(0)
    
    
    
    def __del__(self):
        if self.device.isOpen():
            self.device.flushInput()
            self.device.flushOutput()
            self.device.flush()
            
        if threading.Thread.isAlive() == True:
            threading.Thread.__delete()
        self.device.close()
        del self.device
        print "[*] Closed Serial Device"

    
    def run(self):
        self.__read()
    
    
    def __read(self):
        """ read data from the device
        """
        while not self.close:
            time.sleep(0)
            readed = self.device.read(1)
            if len(readed)>0:
                self.q.put(readed)
            
            
    def stop(self):
        self.close = True
        
    def readBuffer(self):
        """ get one frame from the byte buffer after packet verification
        Queue에 put한 unit size만큼 get에서 가져오게 됨을 주의.
        """
        try:
            buffer_data = ''
            for i in range(self.q.qsize()):
                buffer_data += self.q.get_nowait()
            
            #if len(buffer_data)>0:
            #    print "[*] Read {0}Bytes from the Buffer (remained {1} Bytes)".format(len(buffer_data), self.q.qsize())
            return buffer_data
        except Empty:
            return ''
        
        
        
        
        