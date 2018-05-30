#!bin/bash/python

from pyactor.context import *
import time

class Word(object):
    _tell = ['mapWC', 'reduceWC', 'mapCW', 'reduceCW']
    _ref = ['mapWC', 'mapCW']

    nMappers = 0
    nTotalWords = 0
    finalDicc = {}

    def mapCW(self, tIni, text, reducer, nMappers):
        count = 0
        for word in text.split():
            count += 1
        reducer.reduceCW(count, tIni, nMappers)

    def reduceCW(self, count, tIni, nMappers):
        self.nTotalWords += count
        self.nMappers += 1

        if (self.nMappers == nMappers):
            tFin = time.time()
            tTotal = tFin - tIni
            print ("\nTotal de paraules: ")
            print self.nTotalWords
            print("\nTemps del WordCount: %0.10f segons." %tTotal)



    def mapWC(self, tIni, text, reducer, nMappers):
        dicc = {}
        for word in text.split():
            if word in dicc:
                dicc[word] += 1
            else:
                dicc[word] = 1

        reducer.reduceWC(dicc, tIni, nMappers)


    def reduceWC(self, dicc, tIni, nMappers):
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
            print("\nTemps del WordCount: %0.10f segons." %tTotal)
