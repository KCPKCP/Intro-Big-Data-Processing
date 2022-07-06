# -*- coding: utf-8 -*-
"""
Keiland Pullen

Spring 2022
CSC 555: Big Data Processing
Assignment #1
"""

''' 

Part 2

'''
###################
##  a)
###################

#Name of text file
filename = "HadoopBlurb1.txt";

f = open(filename, 'r')

blurb = f.read().split()

wordcount = {}

for word in blurb:
    if word not in wordcount:
        wordcount[word]= 1
    else:
        wordcount[word] += 1
    
#for key, val in wordcount.items():
#    print (key, val)

print('\n')
print('The number of dictionary keys is ',len(wordcount.keys()))



###################
##  b)
###################

#Name of text file
filename = "HadoopBlurb1.txt";

f = open(filename, 'r')

blurb = f.read().split()

import random

ranDict = {}
wordcount_1 = {}
wordcount_2 = {}

for word in blurb:
    a = [wordcount_1, wordcount_2]
    
    ranDict = random.choice(a)
    #print(type(ranDict))
    #print(ranDict)
    if word not in ranDict:
        ranDict[word] = 1

    else:
        ranDict[word] += 1

# print (wordcount_1)
# print (wordcount_2)

print('\n')
print('The number of dictionary keys in 1st dict is ',len(wordcount_1.keys()))
print('The number of dictionary keys in 2nd dict is ',len(wordcount_2.keys()))



###################
##  c)
###################

#Name of text file
filename = "HadoopBlurb1.txt";

f = open(filename, 'r')

blurb = f.read().split()

import random

ranDict = {}
wordcount_1 = {}
wordcount_2 = {}

for word in blurb:
    a = [wordcount_1, wordcount_2]
    
    ranDict = random.choice(a)
    #print(type(ranDict))
    #print(ranDict)
    if word not in ranDict:
        ranDict[word] = 1

    else:
        ranDict[word] += 1

    
#for key, val in wordcount.items():
#    print (key, val)

print (wordcount_1)
print('\n')
print (wordcount_2)

print('\n')
print('The number of dictionary keys in 1st dict is ',len(wordcount_1.keys()))
print('The number of dictionary keys in 2nd dict is ',len(wordcount_2.keys()))


wordcount_3 = {}

for key in wordcount_1:
    if key in wordcount_2:
        wordcount_1[key] = wordcount_1[key] + wordcount_2[key]
    else:
        pass
        #wordcount_3[key] = wordcount_1[key]

wordcount_3 = wordcount_2| wordcount_1        
    
print('\n')
#print('Wordcount 3')
print(wordcount_3)
print('The number of dictionary keys in the combined dict is ',len(wordcount_3.keys()))
print('\n')


###################
##  d)
###################

#Name of text file
filename = "HadoopBlurb1.txt";

f = open(filename, 'r')

blurb = f.read().split()

wordcount_1 = {}
wordcount_2 = {}


for word in blurb:
    hashWord = hash(word)
    #a = [wordcount_1, wordcount_2]
    print(hashWord)
    val = hashWord % 2
    print(val)
    print(word)
    if val == 0:
        if word not in wordcount_1:
            wordcount_1[word] = 1
        else:
            wordcount_1[word] += 1
        
    if val == 1:
        if word not in wordcount_2:
            wordcount_2[word] = 1
        else:
            wordcount_2[word] += 1
        

print (wordcount_1)
print('\n')
print (wordcount_2)

print('\n')
print('The number of dictionary keys in 1st dict is ',len(wordcount_1.keys()))
print('The number of dictionary keys in 2nd dict is ',len(wordcount_2.keys()))


###############################################################################


''' 

Part 3

'''

###################
##  a) 1)
###################

import urllib
import time
import os

file1 = "HadoopBlurb1.txt";

startTime = time.time()

orginFile = open(file1, 'r')
blurb = orginFile.read()

f = open("csc555_document_1.txt", "w", encoding="utf-8")

f.write(blurb)
          
f.close()

endTime = time.time()

file_size = os.path.getsize('HadoopBlurb1.txt')

print(' The filesize is ', file_size/1000000,' MB.')
print (' The time is ', (endTime - startTime) ,' seconds.')
print (' The rate is ', file_size/(endTime-startTime), ' mbps')



###################
##  a) 2)
###################


import urllib
import time
import os

file2 = "sample_text.txt";

startTime = time.time()

orginFile2 = open(file2, 'r', encoding='utf-8')
blurb = orginFile2.read()

f = open("csc555_document_2.txt", "w", encoding="utf-8")

f.write(blurb)
          
f.close()

endTime = time.time()

file_size = os.path.getsize('twtter_errors.txt')
print(' The filesize is ', file_size/1000000,' MB.')
print (' The time is ', (endTime - startTime) ,' seconds.')
print (' The rate is ', file_size/(endTime-startTime), ' mbps')



###################
##  b)
###################


import urllib
import time
import os

# webFD = urllib.request.urlopen('http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt') 

startTime = time.time()

webFD = urllib.request.urlopen('http://www.textfiles.com/sf/aliensfaq.txt') 

fileLines = webFD.read()
#print(fileLines)
endTime = time.time()

print (' The time is ', (endTime - startTime) ,' seconds.')



###################
##  c)
###################


import urllib
import time
import os

# webFD = urllib.request.urlopen('http://dbgroup.cdm.depaul.edu/DSC450/OneDayOfTweets.txt') 
webFD = urllib.request.urlopen('http://www.textfiles.com/sf/aliensfaq.txt') 

startTime = time.time()

fileLines = webFD.read()

# print(fileLines)
# print(type(fileLines))
f = open("csc555_document_3.txt", "w", encoding="utf-8")

f.write(str(fileLines))
          
f.close()

endTime = time.time()

file_size = os.path.getsize('csc555_document_3.txt')

print(' The filesize is ', file_size/1000000,' MB.')
print (' The time is ', (endTime - startTime) ,' seconds.')
print (' The rate is ', file_size/(endTime-startTime), ' mbps')



###################
##  d)
###################


import urllib
import time
import os

file1 = "HadoopBlurb1.txt";

startTime = time.time()

orginFile = open(file1, 'r')
blurb = orginFile.read()

f = open("csc555_document_1.txt", "w", encoding="utf-8")

f.write(blurb)
          
f.close()

print(blurb)

endTime = time.time()

file_size = os.path.getsize('HadoopBlurb1.txt')

print(' The filesize is ', file_size/1000000,' MB.')
print (' The time is ', (endTime - startTime) ,' seconds.')
print (' The rate is ', file_size/(endTime-startTime), ' mbps')





