
import wordfreq
import string
import re
import subprocess


Nwords = 5000 #Number of words to use when looking for two word solutions
Nwords3 = 500 #Number of words to use when looking for three word solutions

s = input('Input letters grouped by side and each side spaced by spaces> ')

#Useful in development 
if len(s)==0:
    s = 'enr tbl ioa sxp'
    print(f'Got a zero length string using \'{s}\'')

sides = s.split()
sides = list( map(set,sides))
assert(len(sides)==4)

letters = set()
whichside = {}
for (i,side) in enumerate(sides):
    letters = letters | side
    for ch in side:
        whichside[ch] = i
print('\n Solving letterboxed problem:')
print(sides)


    
words = []


for word in wordfreq.iter_wordlist('en'):
    if all([ ch in letters for ch in word]):
        validword = True
        for k in range(1,len(word)):
            if whichside[word[k]]==whichside[word[k-1]]:
                validword = False
                break
        if validword:
            words.append(word)
        
    if len(words) > Nwords:
        break




def lookforsoln(startletter,lettersleft,words,wordsused,depth):
    for w in words:
        if w[0]==startletter:
            if lettersleft-set(w)==set():
                #we've found a solution
#                [print(x+', ',end='') for x in wordsused]
#                print(w)
                solutions.append(wordsused+[w])
            if(depth>0):
                lookforsoln(w[-1],
                            lettersleft-set(w),
                            words,
                            wordsused+[w],
                            depth-1)

def soln_metric(wordlist):
    return sum([len(w) for w in wordlist]) - len(wordlist) + 1



solutions= []
print("\nSome two word solutions")            
for ch in letters:
    lookforsoln(ch,letters,words,[],1)

solutions.sort(key=soln_metric)

if len(solutions)==0:
    print('none')
for k in solutions[:50]:
    print(k)


words  = words[:Nwords3]

solutions= []
print("\nSome three word solutions")            
for ch in letters:
    lookforsoln(ch,letters,words,[],2)

solutions.sort(key=soln_metric)

if len(solutions)==0:
    print('none')
for k in solutions[:50]:
    print(k)
    
