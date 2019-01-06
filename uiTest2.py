# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 17:01:26 2019

@author: T
"""

from PyQt5       import QtCore, QtGui, QtWidgets
#from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import pymysql   as mysql #Imports the python to MySQL driver
#import MySQLdb   as mysql                  # pip install mysqlclient        


def convert(in_data):
    def cvt(data):
        try:
            return ast.literal_eval(data)
        except Exception:
            return str(data)
    return tuple(map(cvt, in_data))

class Ui_MainWindow(object):

    def loadconection(self):
        #                        HostName     UserName           Password      DatabaseName
        conn = pymysql.connect(host="localhost", user="root", passwd="1234", db="imagearchive", charset='utf8')
        with conn.cursor() as cursor:
            #                             table vvvvvvvvv         
            rows = cursor.execute("""select * from METADATA""")
            data = cursor.fetchall()

            for row in data:
                self.add_table(convert(row))

            cursor.close()

    def add_table(self, columns):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)         
        for i, column in enumerate(columns):
            self.tableWidget.setItem(rowPosition, i, QtWidgets.QTableWidgetItem(str(column)))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 520)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(35, 21, 731, 401))
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['Id', 'Name', 'Email', 'Phone', 'Note'])
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.btn_abrirbd2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_abrirbd2.setGeometry(QtCore.QRect(340, 460, 75, 23))
        self.btn_abrirbd2.setObjectName("btn_abrirbd2")
        self.btn_abrirbd2.clicked.connect(self.loadconection)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_abrirbd2.setText(_translate("MainWindow", "SELECT mysql"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())