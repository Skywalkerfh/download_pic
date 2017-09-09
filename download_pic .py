#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64,json,urllib,urllib2
import os
import sys
import cookielib
import uuid

def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")

    if not os.path.exists(path):
        os.makedirs(path)
        
    return path

    
def save_file(path, file_name, data):
    if data == None:
        return
    
    mkdir(path)
    if(not path.endswith("/")):
        path=path+"/"
    file=open(path+file_name, "wb")
    file.write(data)
    file.flush()
    file.close()

def get_file_1(url):
	data = urllib.urlopen(url).read()
	return data

for line in open('id_url', 'r'):
    fields = line.strip().split('\t')
    id = fields[0]
    url = fields[1]
    term = url.strip().split('.')
    num = len(term)
    format = url.strip().split('.')[num - 1]
    img_name = "%s%s%s"%(id, ".", format)
    try:
        save_file("./img/", img_name, get_file_1(url))
    except:
        continue
