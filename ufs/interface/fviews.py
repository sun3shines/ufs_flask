# -*- coding: utf-8 -*-

import json

from ufs.utils.path import path2o
from ufs.interface.fst import FSt

from ufs.myflask.globalx import app
from flask import Response,request
from ufs.utils.urls import strFileCopy,strFileDelete,strFileGet,\
    strFileHead,strFileMove,strFileMove,strFilePost,strFilePut
    
@app.route(strFileGet,methods = ['POST'])
def get():
    req = request
    param = json.loads(req.data)
    
    path = path2o(param.get('path'))
    s = FSt(path)
    if not s.exists:
        return Response(status=404)

    app_iter = s.get()
    response = Response(response=app_iter)
#    return req.get_response(response)
    return response


@app.route(strFilePut,methods = ['POST'])
def put():
    req = request
    param = req.headers
    path = path2o(param.get('path'))
    s = FSt(path)
    
    md5 = req.headers.get('md5')
    datatype = req.headers.get('datatype') 
    fileinput = req.environ['wsgi.input']
    ecode = s.put(md5,datatype,fileinput,req.content_length)
    
    return Response(status=ecode)

@app.route(strFilePost,methods = ['POST'])
def post():
    
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path'))
    
    s = FSt(path)
    if not s.exists:
        return Response(status = 404)
    attrs = req.headers
    ecode = s.setm(attrs)    
    return Response(status=ecode)

@app.route(strFileHead,methods = ['POST'])
def head():

    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path')) 
    is_swift = param.get('is_swift')
    s = FSt(path)
    ecode = 200 
    if not s.exists:
        ecode = 404
        return Response(ecode)
    data = s.getm()
    if 'true' == is_swift:
        return Response(status=ecode,headers=data)
    else:
        return Response(response = json.dumps(data),status=ecode)

@app.route(strFileCopy,methods = ['POST'])
def copy():

    req = request
    param = json.loads(req.data)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    s = FSt(src)
    d = FSt(dst)
    if not s.exists:
        return Response(status=404)

    ecode = s.copy(d)
    return Response(status = ecode)

@app.route(strFileMove,methods = ['POST'])
def move():

    req = request
    param = json.loads(req.data)
    src = path2o(param.get('src'))
    dst = path2o(param.get('dst'))
    
    s = FSt(src)
    d = FSt(dst)
    
    if not s.exists:
        return Response(status=404)
        
    ecode = s.move(d)
    return Response(status=ecode)

@app.route(strFileDelete,methods = ['POST'])
def delete():
   
    req = request
    param = json.loads(req.data)
    path = path2o(param.get('path')) 
    
    s = FSt(path)
    if not s.exists:
        return Response(status=404)
    ecode = s.delete()
    
    return Response(status=ecode) 

