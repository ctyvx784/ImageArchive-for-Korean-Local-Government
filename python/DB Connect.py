# -*- coding: utf-8 -*-
"""
Created on Wed Dec 26 13:23:21 2018

@author: T
"""
import pymysql

db = pymysql.connect(host="localhost", user="root", passwd="1234", db="imagearchive", charset='utf8')

cur = db.cursor()

cur.execute("INSERT INTO METADATA VALUES(3)")

db.commit()

db.close()

