# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:34:31 2018

@author: T
"""
import os
import io
# Imports the Google Cloud client library

from google.cloud import vision
from google.cloud.vision import types
from google.oauth2 import service_account
from konlpy.tag import Kkma, Hannanum, Komoran, Mecab, Twitter
from konlpy.utils import pprint

'''
credentials = service_account.Credentials.from_service_account_file(
    'F:/cnuocr-10d89618fe72.json')
    credentials=credentials
'''
def detect_text(path):
    """Detects text in the file."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')
    
    OCRresult = texts[0].description    
    print(OCRresult)
    print("000000000000000000000000000000000000000000000")

    #kkma = Kkma()
    twitter = Twitter()
    
    #keywords = kkma.nouns(OCRresult)
    keywords = twitter.nouns(OCRresult)
    
    for nonun in keywords:
        if len(nonun) >= 2:
            print(nonun)
            '''
            i = int(filter(str.isdigit,nonun))
            if type(i) != int:
        #print(len(keywords))
        '''
    '''
    for nonun in keywords:
        if len(keywords[nonun]) > 2:
            print(nonun)
    '''            
    
    '''
    for text in texts:
        #print(text.description)
        print('\n"{}"'.format(text.description))
        
        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))
        '''


detect_text('D:/test/image_304.jpg')

