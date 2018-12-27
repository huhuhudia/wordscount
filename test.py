#/usr/bin/env python
# -*- coding: UTF-8 -*-
from pattern.en import lemma
Words = []
A2Z = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# print(A2Z)
def modify(word):
    if word[0] not in A2Z:

        return False

    for i in range(len(word)):
        if word[i] not in A2Z:
            return word[:i]
    return word

def filt(words, modify):
    res = []
    for item in words:
        
        t = modify(item)
        if t:
            res.append(t)
    return res
def readwords(path):
    Words = []
    print(path)
    with open(path) as f:
        for line in f.readlines():
            items = line.split(' ') 
            items = filt(items, modify)
            Words += items
    return Words

pathpattern = '/home/yyy/ML/dataset/data%d.txt'
wordspaths = [pathpattern%i for i in range(7)]
print(wordspaths)
exceptpath = '/home/yyy/ML/dataset/except.txt'
Words = []
for path in wordspaths:
    print(path)
    Words += readwords(path)
COUNTN = len(Words)
Except = readwords(exceptpath)
Words = [w.lower() for w in Words if w.lower() not in Except ]
Words = [lemma(w) for w in Words if lemma(w) not in Except]
res = []

count = {}
for word in Words:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
# print(count)
max_count = 0
for key in count:
    if max_count < count[key]:
        max_count = count[key]
# print(max_count)

Rank = [ [] for i in range(max_count+1)]

for key in count:
    Rank[count[key]].append(key)

for i in range(len(Rank)):
    if len(Rank[max_count-i]):
    
        print('times: ', max_count-i, Rank[max_count-i])

def make_trans_table(data):
    res = '| index | words | url |\n| ------------ | ------------ | ------------ |\n'
    lines = ''
    count = 0
    for word in data:
        lines += '| ' + str(count)+'| ' +word + ' | ' + 'https://fanyi.baidu.com/#en/zh/'+word + ' |\n'
        count+=1
    
    return res+lines+'\n\n\n'+ DIVIDING
DIVIDING = '\n------------\n'

# print(make_trans_table(Rank[1]))
with open('frequency.md','w+') as f:
    res = ''
    for i in range(len(Rank)):
        if len(Rank[i]) == 0:
            continue
        content = "### Times: " + str(i) + '\n' + make_trans_table(Rank[i])
        with open('details/frequency-%d.md'%i, 'w+') as _f:
            _f.write(content)
        res += content

    res = u'## from 1980-2018 Graduate English 1 test filter though 4500 most frequently used words \n### total words: %d \n'%COUNTN+ res
    f.write(res)
