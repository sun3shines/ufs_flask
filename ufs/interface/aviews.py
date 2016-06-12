# -*- coding: utf-8 -*-

import json
import os

from flask import request,Response

from ufs.utils.path import path2o
from ufs.interface.ast import ASt
from ufs.utils.urls import strAcountGet,strAcountHead,strAcountPost,strAcountPut

from ufs.myflask.globalx import app

@app.route(strAcountGet,methods = ['POST'])
def http_account_get():

    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    attrs = a.list()
    return Response(response=json.dumps(attrs),status=200)

@app.route(strAcountPut,methods = ['POST'])
def http_account_put():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    a = ASt(path)
    if a.exists:
        return Response(status=409)
    
    ecode = a.put()
    return Response(status=ecode)    

@app.route(strAcountPost,methods = ['POST'])
def http_account_post():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    
    headers = req.headers
    attrs = headers
    ecode = a.putm(attrs)
    return Response(status=ecode)

@app.route(strAcountHead,methods = ['POST'])
def http_account_head():

    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    is_swift = param.get('is_swift')

    a = ASt(path)
    if not a.exists:
        return Response(status=404)
    
    attrs = a.getm()
    if 'true' == is_swift:
        return Response(status=200,headers=attrs)
    else:
        return Response(response=json.dumps(attrs),status=200)


