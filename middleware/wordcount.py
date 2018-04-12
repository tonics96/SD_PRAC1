#!/usr/bin/python
file=open("big.txt","r+")
wordcount={}
count = 0
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
    count = count + 1
for k,v in wordcount.items():
    print k, v
print count, " words."
