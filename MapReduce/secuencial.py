from datetime import datetime
from time import time

time_inici=0

import re

def studyWord(word):
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
        word=word.replace("[","")
        word=word.replace("]","")
        word=word.replace("/","")
        word=word.replace("|","")
        word=word.replace("#","")
        word=word.replace("*","")
        word=word.replace(" ","")

        return word

def mapReduce(f1): #mapper wordCount
    f=open(f1)

    dicc={}
    for line in f:
        line = re.sub('[^ a-zA-Z0-9]', ' ', line)
        words=line.split()
        for word in words:
            if(word in dicc):
                clau=dicc[word]
                dicc[word]=clau+1
            else:
                dicc[word]=1
    for v,k in dicc.items():
        print v,k
    f.close()
    return dicc


def contWords(f1):  #mapper coutingword
    f=open(f1, 'r')

    num=0
    for line in f:
        line = re.sub('[^ a-zA-Z0-9]', ' ', line)
        words=line.split()
        for word in words:
        	if (word != ''):
        		num=num+1

    print '\nEl numero de paraules es:', num
    f.close()



if __name__ == "__main__":

    f = 'file1.txt'

    nowTime = time() #time start MapReduce
    mapReduce(f)
    tempsFInalMapReduce = time()- nowTime
    print 'Temps MapReduce secuencial: ', tempsFInalMapReduce

    nowTime = time() #time start coutWord
    contWords(f)
    tempsFInalWordCount = time()- nowTime
    print 'Temps MapReduce secuencial: ', tempsFInalWordCount
