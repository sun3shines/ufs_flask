# -*- coding: utf-8 -*-

import json
import os

from ufs.utils.path import path2o
from ufs.interface.dst import DSt

from ufs.myflask.globalx import app
from flask import Response,request
from ufs.utils.urls import strDirCopy,strDirDelete,strDirGet,strDirMove,strDirPut

@app.route(strDirPut,methods = ['POST'])
def http_dir_put():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    d = DSt(path)
    
    if d.exists:
        return Response(status=409)
    ecode = d.put()
    return Response(status=ecode)

@app.route(strDirGet,methods = ['POST'])
def http_dir_get():

    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
        
    d = DSt(path)    
    if not d.exists:
        return Response(status=404)
    if not os.path.isdir(d.path):
        return Response(response = 'path type error',status=400)
    attrs = d.list(r)
    return Response(response = json.dumps(attrs),status=200)
    
@app.route(strDirDelete,methods = ['POST'])
def http_dir_delete():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
         
    d = DSt(path)
    ecode = d.delete(r)
    return Response(status = ecode)

@app.route(strDirCopy,methods = ['POST'])
def http_dir_copy():
    
    req = request
    param = json.loads(req.data)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = DSt(src)
    d = DSt(dst)
    ecode = s.copy(d)
    return Response(status = ecode)

@app.route(strDirMove,methods = ['POST'])
def http_dir_move():
    
    req = request
    param = json.loads(req.data)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = DSt(src)
    d = DSt(dst)
    ecode = s.move(d)
    return Response(status = ecode)


