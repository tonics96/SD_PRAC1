#!/usr/bin/python
import textwrap

from pyactor.context import *

class Splitter(object):
    _tell = ['splitTextBy3']
    _ask = []

    def __init__(self):
        self.wordList = []

    def splitTextBy3(self, txt):
        if ((len(txt) % 3) == 0):
            self.wordList = textwrap.wrap(txt, len(txt)/3)
        elif((len(txt) % 3) == 1):
            self.wordList = textwrap.wrap(txt, (len(txt)+1)/3)
        else:
            self.wordList = textwrap.wrap(txt, (len(txt)+2)/3)

    def getWordList():
        return self.wordList

if __name__ == '__main__':

    set_context()

    host = create_host('http://127.0.0.1:1278/')
    mast1 = host.lookup_url('http://127.0.0.1:1277/master1', 'Master', 'master')

    txt = mast1.getTxt()

    spl1 = host.spawn('splitter1', Splitter)
    spl1.splitTextBy3(txt)

    serve_forever()
