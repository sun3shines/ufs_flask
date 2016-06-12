# -*- coding: utf-8 -*-

import os.path
import os

class MSt:

    def __init__(self,subject):
        self.prefix = '/md5'
        self.subject = subject
        self.readsize = 4096 

    @property
    def path(self):
        return '/'.join([self.prefix,self.subject])

    def get(self):
        
        try:
            self.handle = file(self.path,'r')
            while True:
                data = self.handle.read(self.readsize)
                if data:
                    yield data
                else:
                    break
        finally:
            self.handle.close()

    def put(self,fileinput,length):
        
        with open(self.path,'w') as f:
            while True:
                readsize = self.readsize
                if length < self.readsize:
                    readsize = length
                data = fileinput.read(readsize)
                if data:
                    f.write(data)
                length = length - readsize
                if not length:
                    break

#        input.close()

    @property
    def exists(self):
        if not self.subject:
            return False
        if not os.path.exists(self.path):
            return False
        return True

# Mst 改造为app_iter 的方式，swift中，读取和写结束后，如何关闭？

if __name__ == '__main__':

    m = MSt('c5371ed9133353622166fe6352b91a56') 
    if m.exists:
        print 'exists'
    else:
        print 'not exists'
        m.put(file('/root/install.log'))

    for data in m.get():
        print data
        print len(data)
