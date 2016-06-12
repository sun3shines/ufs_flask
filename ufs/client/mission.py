
# -*- coding: utf-8 -*-

from httplib import HTTPConnection

class Mission:
    
    def __init__(self,host,port):
        
        self.host= host
        self.port = port
        self.conn = None
        self.connection_flag = False
        self.readsize = 4096
 
        self.timeout = 1000
        
    def __enter__(self):
        self.connect()
        return self 
  
    def getHttpsConn(self):
        
        return HTTPConnection(self.host,self.port,True,self.timeout)  

    def connect(self):
        
        if not self.connection_flag:
            self.conn = self.getHttpsConn()
            self.connection_flag = True
    
    def close(self):
        
        if self.connection_flag:
            self.conn.close()
            self.connection_flag = False
            
    def __exit__(self,type,value,trace):
        self.close()
        
    def http(self,t):
       
        self.conn.request(t.getMethod(),t.getUrl(),t.getBody(),t.getHeaders())
        resp = self.conn.getresponse()
        t.status = resp.status

        t.headers = {}
        for item in resp.getheaders():
            t.headers[item[0]] = item[1]

        t.data = resp.read()
        t.execute = True
        return t
   
    def download(self,t):
        try:    
            self.connect()
            self.conn.request(t.getMethod(),t.getUrl(),t.getBody(),t.getHeaders())
            resp = self.conn.getresponse()
            while True:
                data = resp.read(self.readsize)
                if data:
                    yield data
                else:
                    break
        finally:
            self.close()
 
def getMission():

    return Mission(host='127.0.0.1',port=7090)

def execute(t):
    
    with getMission() as m:
        m.http(t)
    
    return t 

def download(t):
    m = getMission()
    return m.download(t)

