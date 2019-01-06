# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 13:25:08 2019

@author: T
"""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("운전자 졸음 감지 모델_V1.0")
        MainWindow.resize(1600, 900)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 5, 1580, 880))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")

        #######################################
        #메인윈도우 동영상, 특징추출, 결과
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
            #######################################
            #동영상
        self.verticalLayout_Play = QtWidgets.QVBoxLayout()
        self.verticalLayout_Play.setObjectName("verticalLayout_Play")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setText("원본 영상")
        font = self.lineEdit_2.font()  # lineedit current font
        font.setPointSize(30)  # change it's size
        self.lineEdit_2.setFont(font)  # set font
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.verticalLayout_Play.addWidget(self.lineEdit_2)
        self.MainVideo_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.MainVideo_label.setObjectName("label_4")
        self.verticalLayout_Play.addWidget(self.MainVideo_label)
        self.horizontalLayout.addLayout(self.verticalLayout_Play,3)
            #######################################
            #구분선
        self.line_2 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout.addWidget(self.line_2)
            #######################################
            #특징 추출
        self.verticalLayout_Feat = QtWidgets.QVBoxLayout()
        self.verticalLayout_Feat.setObjectName("verticalLayout_Feat")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setText("특징 눈")
        font = self.lineEdit.font()  # lineedit current font
        font.setPointSize(22)  # change it's size
        self.lineEdit.setFont(font)  # set font
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.verticalLayout_Feat.addWidget(self.lineEdit)
                #######################################
        self.Eye_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Eye_image_label.setObjectName("label")
        self.verticalLayout_Feat.addWidget(self.Eye_image_label)
                #######################################
        self.line_4 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_Feat.addWidget(self.line_4)
                #######################################
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_4.setText("특징 입")
        font = self.lineEdit_4.font()  # lineedit current font
        font.setPointSize(22)  # change it's size
        self.lineEdit_4.setFont(font)  # set font
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.verticalLayout_Feat.addWidget(self.lineEdit_4)
                #######################################
        self.Mouth_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Mouth_image_label.setObjectName("label_2")
        self.verticalLayout_Feat.addWidget(self.Mouth_image_label)
                #######################################
        self.line_5 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout_Feat.addWidget(self.line_5)
                #######################################
        self.lineEdit_5 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_5.setText("특징 PPG")
        font = self.lineEdit_5.font()  # lineedit current font
        font.setPointSize(22)  # change it's size
        self.lineEdit_5.setFont(font)  # set font
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setReadOnly(True)
        self.verticalLayout_Feat.addWidget(self.lineEdit_5)
                #######################################
        self.PPG_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.PPG_image_label.setObjectName("label_3")
        self.verticalLayout_Feat.addWidget(self.PPG_image_label)
        self.horizontalLayout.addLayout(self.verticalLayout_Feat,1)
            #######################################
            # 구분선
        self.line_3 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.horizontalLayout.addWidget(self.line_3)
            #######################################
            #결과출력
        self.verticalLayout_result = QtWidgets.QVBoxLayout()
        self.verticalLayout_result.setObjectName("verticalLayout_result")
                #######################################
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_6.setText("예측")
        font = self.lineEdit_6.font()  # lineedit current font
        font.setPointSize(19)  # change it's size
        self.lineEdit_6.setFont(font)  # set font
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setReadOnly(True)
        self.verticalLayout_2.addWidget(self.lineEdit_6)
        self.Prediction_Label_Normal_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Prediction_Label_Normal_image_label.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.Prediction_Label_Normal_image_label)
        self.Prediction_Label_Light_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Prediction_Label_Light_image_label.setObjectName("label_pre_Light")
        self.verticalLayout_2.addWidget(self.Prediction_Label_Light_image_label)
        self.Prediction_Label_Deep_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.Prediction_Label_Deep_image_label.setObjectName("label_pre_Deep")
        self.verticalLayout_2.addWidget(self.Prediction_Label_Deep_image_label)

        self.horizontalLayout_3.addLayout(self.verticalLayout_2,3)
                #######################################
        self.line_6 = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.horizontalLayout_3.addWidget(self.line_6)
                #######################################
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_7.setText("실제 결과")
        font = self.lineEdit_7.font()  # lineedit current font
        font.setPointSize(25)  # change it's size
        self.lineEdit_7.setFont(font)  # set font
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setReadOnly(True)
        self.verticalLayout_3.addWidget(self.lineEdit_7)

        self.True_Label_Normal_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.True_Label_Normal_image_label.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.True_Label_Normal_image_label)
        self.True_Label_Light_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.True_Label_Light_image_label.setObjectName("label_Light")
        self.verticalLayout_3.addWidget(self.True_Label_Light_image_label)
        self.True_Label_Deep_image_label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.True_Label_Deep_image_label.setObjectName("label_depp")
        self.verticalLayout_3.addWidget(self.True_Label_Deep_image_label)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3,3)
                #######################################
        self.verticalLayout_result.addLayout(self.horizontalLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_result,2)
            #######################################
        self.verticalLayout.addLayout(self.horizontalLayout)
        #######################################
        #메인 윈도우 버티컬 구분선
        self.line = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        #######################################
        #메인 윈도우 로그창 및 버튼
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.thread_run)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        #######################################
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1338, 21))
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
        # 초기화 이미지 파일
        pixmap = QtGui.QPixmap('./wt.png')

        self.label_7.setText(_translate("MainWindow", "SYSTEM LOG"))
        self.pushButton.setText(_translate("MainWindow", "실행"))

        self.MainVideo_label.setPixmap(pixmap)
        self.MainVideo_label.setAlignment(QtCore.Qt.AlignCenter)
        self.MainVideo_label.setScaledContents(True)
        self.Eye_image_label.setPixmap(pixmap)
        self.Eye_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.Eye_image_label.setScaledContents(True)
        self.Mouth_image_label.setPixmap(pixmap)
        self.Mouth_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.Mouth_image_label.setScaledContents(True)
        self.PPG_image_label.setPixmap(pixmap)
        self.PPG_image_label.setAlignment(QtCore.Qt.AlignCenter)
        self.PPG_image_label.setStyleSheet(
            "background-color:#f7f7f7; color:#8e8e8e;font-size:80px;")

        #self.PPG_image_label.setScaledContents(True)
        self.Prediction_Label_Normal_image_label.setPixmap(pixmap)
        self.Prediction_Label_Normal_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.Prediction_Label_Normal_image_label.setScaledContents(True)
        self.Prediction_Label_Light_image_label.setPixmap(pixmap)
        self.Prediction_Label_Light_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.Prediction_Label_Light_image_label.setScaledContents(True)
        self.Prediction_Label_Deep_image_label.setPixmap(pixmap)
        self.Prediction_Label_Deep_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.Prediction_Label_Deep_image_label.setScaledContents(True)
        self.True_Label_Normal_image_label.setPixmap(pixmap)
        self.True_Label_Normal_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.True_Label_Normal_image_label.setScaledContents(True)
        self.True_Label_Light_image_label.setPixmap(pixmap)
        self.True_Label_Light_image_label.setAlignment(QtCore.Qt.AlignCenter)
        #self.True_Label_Light_image_label.setScaledContents(True)
        self.True_Label_Deep_image_label.setPixmap(pixmap)
        self.True_Label_Deep_image_label.setAlignment(QtCore.Qt.AlignCenter)