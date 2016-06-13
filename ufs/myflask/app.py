#!f/usr/bin/python

from ufs.myflask.globalx import app
import ufs.interface.aviews
import ufs.interface.cviews
import ufs.interface.dviews
import ufs.interface.fviews

from ufs.utils.urls import strHello
 
@app.route(strHello,methods=['POST'])
def hello_world():
    return "Hello World!"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7090,debug=True)

