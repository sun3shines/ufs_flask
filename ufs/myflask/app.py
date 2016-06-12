#!f/usr/bin/python

from ufs.myflask.globalx import app
import ufs.interface.aviews
import ufs.interface.cviews
import ufs.interface.dviews
import ufs.interface.fviews

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=7090,debug=True)
