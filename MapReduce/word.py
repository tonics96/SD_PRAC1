#!bin/bash/python

from pyactor.context import set_context, create_host, serve_forever, shutdown, sleep
import time

class Word(object):
    _tell = ['map', 'reduce']
    _ref = ['map', 'reduce']

    nMappers = 0
    nTotalWords = 0
    finalDicc = {}

    def cleanWord(self, word):
        word=word.replace(".","")
        word=word.replace(",","")
        word=word.replace(":","")
        word=word.replace(";","")
        word=word.replace("-","")
        word=word.replace('"',"")
        word=word.replace("'","")
        word=word.replace("(","")
        word=word.replace(")","")
        word=word.replace("?","")
        word=word.replace("!","")
        word=word.replace("_","")
        return word

    def map(self, tIni, text, reducer, nMappers):
        dicc = {}
        for word in text:
            word = self.cleanWord(word)
            if word in dicc:
                dicc[word] += 1
            else:
                dicc[word] = 1

        reducer.reduce(dicc, tIni, nMappers)
        shutdown()

    def reduce(self, dicc, tIni, nMappers):
        for k, v in dicc.items():
            if k in self.finalDicc:
                self.finalDicc[k] += v
            else:
                self.finalDicc[k] = v

        self.nMappers += 1
        if (self.nMappers == nMappers):
            tFin = time.time()
            tTotal = tFin - tIni
            for k, v in self.finalDicc.items():
                print k, v
            print("\nTemps del mapReduce: %0.10f segons." %tTotal)

    
