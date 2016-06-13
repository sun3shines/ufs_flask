# -*- coding: utf-8 -*-

import json
from ufs.client.tasks.task import Task
from ufs.utils.urls import strHello
import ufs.client.mission as mission

class Hello(Task):
    
    def getUrl(self):
        return strHello
    
    def getMethod(self):
        return 'POST'
    

if __name__ == '__main__':
    t = Hello()
    t = mission.execute(t,port=80)
    print t.status
    print t.data
