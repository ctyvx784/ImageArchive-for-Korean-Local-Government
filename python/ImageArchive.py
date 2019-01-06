# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 17:27:43 2018

@author: T
"""
import io, os
from PIL import Image                  #Imports PIL library
from PIL.ExifTags import TAGS
from google.cloud import vision        #Imports the Google Cloud client library
from konlpy.tag import Twitter         #Imports KoNLPy library
from gluoncv import model_zoo, data #Imports ObjectDetection library
from collections import Counter        #Imports CounterFunction library
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog
#from PyQt5.QtCore import *
from PyQt5 import uic
#from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
import pymysql                        #Imports the python to MySQL driver

objectCountResult = {}                #Dictionary for Counting text from objectArray
ret = {}                              #Dictionary for exif
"""Import ui"""
form_class = uic.loadUiType("ImageArchive.ui")[0]

class MainWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.line.setStyleSheet("background-color: red")
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setStyleSheet("background-color: rgb(218, 218, 218)")
        self.pushButton.clicked.connect(self.insert)
        self.pushButton_2.clicked.connect(self.closeEvent)
        self.pushButton_3.clicked.connect(self.fileOpen)
    
    """파일 찾기"""
    def fileOpen(self):
        fname = QFileDialog.getOpenFileName(self)
        self.lineEdit_11.setText(fname[0])
        self.imageFileLocation = fname[0]
        
        self.imageFileSize = self.file_size()
        self.lineEdit_12.setText(self.imageFileSize)
    
        self.get_exif()
        self.dateCreated = ret['DateTime']
        self.lineEdit_7.setText(self.dateCreated)
        self.widthSize = ret['ExifImageWidth']
        self.lineEdit_9.setText(str(self.widthSize))
        self.heightSize = ret['ExifImageHeight']
        self.lineEdit_10.setText(str(self.heightSize))
        self.imageCompressedFormat = self.imageFileLocation[-3:]
        self.lineEdit_13.setText(self.imageCompressedFormat)
        
        self.lineEdit_3.setText(" ")
        self.lineEdit_18.setText(" ")
        
        self.keywordResult = []                    #List for nouns from OCR
        
        
    """종료 버튼"""    
    def closeEvent(self):
        self.conn.close()
        sys.exit(0)
        print("프로그램 종료")
    
    """Connet to MySQL"""
    def loadConection(self):
        try:
            self.conn = pymysql.connect(host="localhost", user="root", passwd="1234", db="imagearchive", charset='utf8')
            self.cursor = self.conn.cursor()
            print("데이터베이스 연결에 성공하였습니다.")
        except:
            self.conn.show_warnings()
            print("데이터베이스 연결에 실패하였습니다.")
    """Get image file size"""
    def file_size(self):
        """
        this function will return the file size
        """
        if os.path.isfile(self.imageFileLocation):
            self.file_info = os.stat(self.imageFileLocation)
            #print(self.file_info.st_size)
            return self.convert_bytes()
    
    """Convert the file size""" 
    def convert_bytes(self):
        """
        this function will convert bytes to MB.... GB... etc
        """
        num = self.file_info.st_size
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                return "%3.1f %s" % (num, x)
            num /= 1024.0
    
    """Get exif in the image""" 
    def get_exif(self):
        i = Image.open(self.imageFileLocation)
        info = i._getexif()
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
        
    """Google OCR Function: Extract the text in the input image file"""
    def detect_text(self):
        """Detects text in the ImageFile."""
        client = vision.ImageAnnotatorClient()
    
        with io.open(self.imageFileLocation, 'rb') as image_file:
            content = image_file.read()
    
        image = vision.types.Image(content=content)
        response = client.text_detection(image=image)
        texts = response.text_annotations
        
        OCRresult = texts[0].description    
        
        """Noun extraction from the OCRresult"""
        twitter = Twitter()
        keywords = twitter.nouns(OCRresult)
        
        for nonun in keywords:
            if len(nonun) >= 2:
                self.keywordResult.append(nonun)
           

    """Object Detection Function: Extract the object in the input image file"""
    def object_detection(self):
        
        net = model_zoo.get_model('faster_rcnn_resnet101_v1d_coco', pretrained=True)
        
        x, orig_img = data.transforms.presets.rcnn.load_test(self.imageFileLocation, short=800, max_size=1300, mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))
        labels, scores, bboxes = net(x)
            
        label_text=""         
        objectArray=[]        #List for text from Object Detection
        
        for i, item in enumerate(scores[0]):
            if(item[0] > 0.99):
                label_text = net.classes[i//1000]
                objectArray.append(label_text)
        
        self.objectCountResult = Counter(objectArray)  #텍스트에서 단어의 출현횟수 세기 - Dictionary 구조로 저장됨
        
    """저장 버튼"""    
    def insert(self):
        """사용자 입력을 변수로 저장"""
        self.name = self.lineEdit.text()
        self.groupName = self.lineEdit_2.text()
        self.originalName = self.lineEdit_4.text()
        self.registrant = self.lineEdit_5.text()
        self.creator = self.lineEdit_6.text()
        self.locationCreated = self.lineEdit_8.text()
        
        self.description = self.lineEdit_14.text()
        self.category = self.lineEdit_15.text()
        self.personShownInTheImage = self.lineEdit_17.text()
        
        """ocr, 객치인식 함수 실행 """
        self.detect_text()
        self.object_detection()
        
        """Transform the Dictionary to List."""
        dicToList=[]
        for key, val in self.objectCountResult.items(): dicToList.append(key + ':' + str(val))
        
        """Transform the List to String."""
        ocrData = ', '.join(self.keywordResult)
        objectData = ', '.join(dicToList)
    
        self.lineEdit_3.setText(ocrData)
        self.lineEdit_18.setText(objectData)
        
        try:
            sql = """INSERT INTO METADATA(Name, GroupName, Keywords, OriginalName, Registrant, Creator,
                    DateCreated, LocationCreated, WidthSize, HeightSize, ImageFileLocation, ImageFileSize,
                    ImageCompressedFormat, Description, Category, PersonShownInTheImage, ObjectInTheImage)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            stmtData = (self.name, self.groupName, ocrData, self.originalName, self.registrant, self.creator, 
                        self.dateCreated, self.locationCreated, self.widthSize, self.heightSize, self.imageFileLocation, self.imageFileSize, 
                        self.imageCompressedFormat, self.description, self.category, self.personShownInTheImage, objectData)
            print(stmtData)
            self.cursor.execute(sql, stmtData)
            self.conn.commit()
            QMessageBox.about(self, "message", "사진을 성공적으로 저장하였습니다.")
        except:
            self.conn.rollback()
            self.conn.show_warnings()
            QMessageBox.about(self, "message", "사진을 저장하는데 실패하였습니다.")
        
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    ui.loadConection()
    sys.exit(app.exec_())