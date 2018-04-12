#!/usr/bin/python

from pyactor.context import *

class Mapper(object):
    _tell = ['setMap', 'wordCount']
    _ask = ['getWordCount']
    _ref = ['setMap']

    def __init__(self):
    	self.txt = ""
    	self.wordCount = {}

    def setMap(self, n, spl):    	
    	self.txt = spl.getWordList[n]

    def wordCount(self):
    	for word in self.txt.split():
	    	if word not in self.wordCount:
	       		self.wordCount[word] = 1
	    	else:
	        	self.wordCount[word] += 1

	def getWordCount(self):
		return self.wordCount

if __name__ == '__main__':

    set_context()
    host = create_host('http://127.0.0.1:1279/')
    #spl1 = host.lookup_url('http://127.0.0.1:1278/splitter1', 'Splitter', 'splitter')
    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')

    m1 = host.spawn('map1', Mapper)
    m2 = host.spawn('map2', Mapper)
    m3 = host.spawn('map3', Mapper)

    registry.bind('map1', m1)
    registry.bind('map2', m2)
    registry.bind('map3', m3)

    

    m1.setMap(0, spl1)    
    m2.setMap(1, spl1)
    m3.setMap(2, spl1)

    m1.wordCount()
    m2.wordCount()
    m3.wordCount()

    serve_forever()
