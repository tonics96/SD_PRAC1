#!/usr/bin/python

from pyactor.context import *

if __name__ == '__main__':

    set_context()
    host = create_host('http://127.0.0.1:1301/')

    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')

    registry.bind('mapper1', host)

    serve_forever()
