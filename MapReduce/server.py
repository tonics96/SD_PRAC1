#!/usr/bin/

from pyactor import *
from time import time
import textwrap

def splitText(txt):
    textList = []
    if ((len(txt) % 3) == 0):
        textList = textwrap.wrap(txt, len(txt)/3)
    elif((len(self.txt) % 3) == 1):
        textList = textwrap.wrap(txt, (len(txt)+1)/3)
    else:
        textList = textwrap.wrap(txt, (len(txt)+2)/3)

    print textList[1]

    return textList

if __name__ == '__main__':
    set_context()

    nMappers = 3

    f = open('file1.txt', 'r')

    txt = f.read()
    textList = splitText(txt)

    tIni = time()

    host = create_host('http://127.0.0.1:1277')
    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')

    remote1 = registry.lookup('mapper1')
    mapper1 = remote1.spawn('word', 'word/Word')
    remote2 = registry.lookup('mapper2')
    mapper2 = remote2.spawn('word', 'word/Word')
    remote3 = registry.lookup('mapper3')
    mapper3 = remote3.spawn('word', 'word/Word')
    remoteR = registry.lookup('reducer')
    reducer = remoteR.spawn('word', 'word/Word')

    mapper1.map(tIni, textList[0], reducer, nMappers)
    mapper2.map(tIni, textList[1], reducer, nMappers)
    mapper3.map(tIni, textList[2], reducer, nMappers)




    shutdown()
