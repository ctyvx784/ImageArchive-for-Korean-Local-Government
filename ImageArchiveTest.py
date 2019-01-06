# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 17:34:00 2018

@author: T
"""
import os
import io
import pymysql #Imports the python to MySQL driver
from google.cloud import vision #Imports the Google Cloud client library
from konlpy.tag import Twitter #Imports KoNLPy library
from gluoncv import model_zoo, data, utils #Imports ObjectDetection library
from collections import Counter #Imports CounterFunction library

keywordList = []    #List for nouns from OCR
countResult={}      #Dictionary for Counting text from objectArray

'''
1. Google OCR Function: Extract the text from the input image file
'''

def detect_text(path):
    """Detects text in the ImageFile."""
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    
    OCRresult = texts[0].description    
    
    """Noun extraction in the OCRresult."""
    twitter = Twitter()
    keywords = twitter.nouns(OCRresult)
    
    for nonun in keywords:
        if len(nonun) >= 2:
            keywordList.append(nonun)
           
'''
2. Object Detection Function: Extract the object from the input image file
'''

def object_detection(path):
    
    net = model_zoo.get_model('faster_rcnn_resnet101_v1d_coco', pretrained=True)
    
    x, orig_img = data.transforms.presets.rcnn.load_test(path, short=800, max_size=1300, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
    labels, scores, bboxes = net(x)
        
    text=""
    objectArray=[]  #List for text from Object Detection
    
    for i, item in enumerate(scores[0]):
        if(item[0] > 0.99):
            text = net.classes[i//1000]
            objectArray.append(text)
    
    countResult = Counter(objectArray)  #텍스트에서 단어의 출현횟수 세기 - Dictionary 구조로 저장됨

'''
3. Insert Metadata Function: Insert the metadata(keywordList - text, countResult - object) to MySQL
'''

def process_OCRMetadata(List, Dictionary):
    conn = pymysql.connect(host="localhost", user="root", passwd="1234", db="imagearchive", charset='utf8')
    '''
    #For insert the ocrResult, objectDetectionResult to MySQL, have to make a String Variable
    #So, if variable is dictionaty, transform the Dictionary to List
    #And transfrom the List to String using join function
    '''
    dicToList=[]    
    
    """Transform the Dictionary to List."""
    for key, val in Dictionary.items():
        dicToList.append(key + ':' + str(val))
    
    """Transform the List to String."""
    ocrData = ', '.join(List)
    objectData = ', '.join(dicToList)
    stmtData = (ocrData, objectData)

    """Insert the String values to MySQL"""   
    try:
        with conn.cursor() as cursor:
            sql = 'INSERT INTO METADATA(Keywords, ObjectintheImage) VALUES (%s, %s)'
            cursor.execute(sql, stmtData)
        conn.commit()
    except:
        conn.rollback()
    finally:
        conn.close()
    
detect_text('D:/test/image_228.jpg') 
#object_detection('D:/test/image_228.jpg')
countResult={'person': 6, 'truck': 1}
process_OCRMetadata(keywordList, countResult)