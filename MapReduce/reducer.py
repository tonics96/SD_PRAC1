#!/usr/bin/python

from pyactor.context import *

if __name__ == '__main__':

    set_context()
    host = create_host('http://127.0.0.1:2000/')

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')

    registry.bind('reducer', host)

    serve_forever()
