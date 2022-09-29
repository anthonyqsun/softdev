# AABattery: Aaron Gershkovich, Anthony Sun
# SoftDev
# K05 - bitstream
# 2022-09-29
# time spent: 0.5 hr

'''
DISCO:
- split() separated by a delimiter
- use open("filename") to open a file
- fstrings make life easy
- strip() removes trailing whitespace
- print(*list) removes the list syntax

QCC
- do we have access to the actual krewes.txt?
- how efficient is this for larger file sizes?
'''

import random

with open("krewes.txt", "r") as f:
    filecontent = f.read().strip()
    
devolist = filecontent.split("@@@")

krewes = {}

for devo in devolist:
    details = devo.split("$$$")
    pd = details[0]
    devoinfo = (details[1], details[2])
    
    if pd in krewes:
        krewes[pd].append(devoinfo)
    else:
        krewes[pd] = [devoinfo]

#print(*krewes)
#[print(value) for value in krewes.values()]
        
def get_devo(krewes):
    pd = random.choice(list(krewes.keys()))
    return (pd, random.choice(krewes[pd]))

devo = get_devo(krewes)
print(f"{devo[1][0]} of period {devo[0]} with companion {devo[1][1]}")