#!/usr/bin/python

from pyactor.context import *

class Reducer(object):
    _tell = []
    _ask = []

    def __init__(self):
        self.words = {}

if __name__ == '__main__':

    set_context()
    host = create_server('http://127.0.0.1:1280/')

    

