#!/usr/bin/python

from pyactor.context import *

class Master(object):
    _tell = []
    _ask = ['getText']

    def __init__(self):
        f = open('file1.txt','r')
        self.txt = f.read()

    def getText(self):
        return self.txt

if __name__ == '__main__':

    set_context()
    host = create_host('http://127.0.0.1:1277/')

    mast1 = host.spawn('master1', Master)
    serve_forever()
