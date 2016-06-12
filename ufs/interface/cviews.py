# -*- coding: utf-8 -*-

import json
import os

from ufs.utils.path import path2o
from ufs.interface.cst import CSt

from ufs.myflask.globalx import app
from flask import Response,request
from ufs.utils.urls import strContainerDelete,strContainerGet,strContainerHead,strContainerPost,strContainerPut

@app.route(strContainerGet,methods = ['POST'])
def http_container_get():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    tree = param.get('tree')
    if 'true' == tree:
        r = True
    else:
        r = False
        
    c = CSt(path)
    if not c.exists:
        return Response(status=404)

    attrs = c.list(r)
    return Response(response = json.dumps(attrs),status=200)

@app.route(strContainerPut,methods = ['POST'])
def http_container_put():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if c.exists:
        return Response(status=409)    

    ecode = c.put()
    return Response(status=ecode)

@app.route(strContainerDelete,methods = ['POST'])
def http_container_delete():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    ecode = c.delete()
    return Response(status=ecode)

@app.route(strContainerHead,methods = ['POST'])
def http_container_head():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    is_swift = param.get('is_swift')
 
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    attrs = c.getm()
    if 'true' == is_swift:
        return Response(status=200,headers=attrs)
    else:
        return Response(response = json.dumps(attrs),status=200)   

@app.route(strContainerPost,methods = ['POST'])
def http_container_post():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    
    c = CSt(path)
    if not c.exists:
        return Response(status=404)
    
    headers = req.headers
    attrs = headers
    ecode = c.putm(attrs)
    return Response(status = ecode)
    
    