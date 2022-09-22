'''
Flame-Broiled Corgis: Nicholas Tarsis, Anthony Sun, Brian Chen
Soft Dev
#4
22-09-22
'''

'''
DISCO:
* set of dictionary keys is an iterable but cannot be indexed; another list must be generated with the contents of key set
* random.randrange() takes inclusive/exclusive, random.randint() takes inclusive/inclusive
* list(I) converts iterable I into a list
* 
QCC:
* What kind of object does krewes.keys() return?

OPS SUMMARY:
* Pretty simple procedure to follow
* Brian searched for functionality online, Nicholas as navigator, Anthony as driver
'''

import random

def get_devo(krewes):
    period = random.randrange(len(krewes))
    classlist = krewes[list(krewes.keys())[period]]
    return classlist[random.randrange(0,len(classlist))]

krewes = {2: ["a","b","c"], 7:["d","e","f"], 8: ["g","h","i"]}
print(get_devo(krewes))