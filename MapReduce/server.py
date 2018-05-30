#!/usr/bin/

from pyactor.context import *
from time import time
import requests
import re
import textwrap

def splitText(txt):
    textList = []
    if((len(txt) % 4) == 0):
        textList = textwrap.wrap(txt, len(txt)/4)
    elif((len(txt) % 4) == 1):
        textList = textwrap.wrap(txt, (len(txt)+1)/4)
    elif((len(txt) % 4) == 2):
        textList = textwrap.wrap(txt, (len(txt)+2)/4)
    else:
        textList = textwrap.wrap(txt, (len(txt)+3)/4)
    return textList

if __name__ == '__main__':
    set_context()

    mode = 0
    fitxer = 0
    txt = ''

    while ((mode != '1') and (mode != '2')):
        mode = raw_input('\nQuin programa vols:\n1- WordCount\n2- CountWord\n')
    
    while ((fitxer != '1') and (fitxer != '2') and (fitxer != '3')):
        fitxer = raw_input('\nQuin fitxer vols:\n1- Sherlock Holmes\n2- El Quijote\n3- The Bible\n')

    if(fitxer == '1'):
        txt = requests.get("http://127.0.0.1:8000/big.txt").text
    if(fitxer == '2'):
        txt = requests.get("http://127.0.0.1:8000/pg2000.txt").text
    if(fitxer == '3'):
        txt = requests.get("http://127.0.0.1:8000/pg10.txt").text

    nMappers = 4

    txt = requests.get("http://127.0.0.1:8000/file1.txt").text
    txt2 = re.sub('[^ a-zA-Z0-9]', ' ', txt)
    textList = splitText(txt2)

    tIni = time()

    host = create_host('http://127.0.0.1:1277')
    registry = host.lookup_url('http://127.0.0.1:6000/regis', 'Registry', 'registry')


    remote1 = registry.lookup('mapper1')
    mapper1 = remote1.spawn('word', 'word/Word')
    remote2 = registry.lookup('mapper2')
    mapper2 = remote2.spawn('word', 'word/Word')
    remote3 = registry.lookup('mapper3')
    mapper3 = remote3.spawn('word', 'word/Word')
    remote4 = registry.lookup('mapper4')
    mapper4 = remote4.spawn('word', 'word/Word')
    remoteR = registry.lookup('reducer')
    reducer = remoteR.spawn('word', 'word/Word')

    if(mode == '1'):
        mapper1.mapWC(tIni, textList[0], reducer, nMappers)
        mapper2.mapWC(tIni, textList[1], reducer, nMappers)
        mapper3.mapWC(tIni, textList[2], reducer, nMappers)
        mapper4.mapWC(tIni, textList[3], reducer, nMappers)
    else:
        mapper1.mapCW(tIni, textList[0], reducer, nMappers)
        mapper2.mapCW(tIni, textList[1], reducer, nMappers)
        mapper3.mapCW(tIni, textList[2], reducer, nMappers)
        mapper4.mapCW(tIni, textList[3], reducer, nMappers)

