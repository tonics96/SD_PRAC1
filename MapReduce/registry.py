#!/usr/bin/python

from pyactor.context import *

class Registry(object):
    _ask = ['get_all', 'bind', 'lookup', 'unbind']
    _async = []
    _ref = ['get_all', 'bind', 'lookup']

    def __init__(self):
        self.mappers = {}

    def bind(self, name, mapper):
        print "mapper registred " mapper
        self.mappers[name] = mapper

    def getAll(self):
        return self.mappers.values()

    def unbind(self, name):
        if name in self.mappers.keys():
            del self.mappers[name]
        else:
            print "mapper can't be deleted, doesn't exists."

    def lookup(self, name):
        if name in self.mappers:
            return self.mappers[name]
        else:
            return None

if __name__ == "__main__":

    set_context()
    host = create_host('http://127.0.0.1:6000/')

    registry = host.spawn('regis', Registry)

    print 'host listening at port 6000'

    serve_forever()
