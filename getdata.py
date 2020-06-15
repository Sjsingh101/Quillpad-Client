#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 00:09:31 2020

@author: sjsingh
"""
import requests 
import json
import re
import string

def has_latin(name):
    char_set = string.ascii_letters
    return all((True if x in char_set else False for x in name))

URL = "http://172.17.0.2:8090/processWordJSON"
lang = "hindi"


with open('bigdict.json') as fjson:
    bdict = json.load(fjson)
#keys = [word for word in set() if word.isalpha() ]
keys = [w for w in bdict.keys() if has_latin(w)]

print(len(keys))

etoh_dict = {}
count =0
for word in keys:
    PARAMS = {'inString': word,'lang': lang}
    try: 
        data = requests.get(url = URL, params = PARAMS).json()
        etoh_dict[word] = data['twords'][0]['options']
    except:
        print(word," ",count)
    count+=1    

with open('final-multi.json','w') as fjson:
    json.dump(etoh_dict,fjson,ensure_ascii=False,indent=4)

final = {}
for key in etoh_dict.keys():
    final[key] = etoh_dict[key][0]

with open('final.json','w') as fjson:
    json.dump(final,fjson,ensure_ascii=False,indent=4)


