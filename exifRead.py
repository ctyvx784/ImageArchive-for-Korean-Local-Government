# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 17:22:33 2019

@author: T
"""
import os
from PIL import Image
from PIL.ExifTags import TAGS
 
path = "D:/test/image_568.jpg"
ret = {}

def get_exif(fn):
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    #price_list = list(ret.values())
    print(ret)
    
    print(ret['DateTime'])
    print(ret['ExifImageWidth'])
    print(ret['ExifImageHeight'])
    print(file_size(fn))
    '''
    mysize = os.path.getsize(fn)
    print("mysize :", mysize)
    '''
def file_size(file_path):
    """
    this function will return the file size
    """
    if os.path.isfile(file_path):
        file_info = os.stat(file_path)
        return convert_bytes(file_info.st_size)
    
def convert_bytes(num):
    """
    this function will convert bytes to MB.... GB... etc
    """
    for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0
        
get_exif(path)