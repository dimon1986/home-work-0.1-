# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\cube\PycharmProjects\malysh\M_Dawson_Home_Work\Chapter_3\QtPy5\challenge_QtPy3_1_2.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(838, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton_0 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_0.setObjectName("radioButton_0")
        self.gridLayout.addWidget(self.radioButton_0, 7, 0, 1, 1)
        self.label_0 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_0.setFont(font)
        self.label_0.setObjectName("label_0")
        self.gridLayout.addWidget(self.label_0, 0, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 2, 2, 1, 2)
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_1.setFont(font)
        self.pushButton_1.setObjectName("pushButton_1")
        self.gridLayout.addWidget(self.pushButton_1, 6, 0, 1, 4)
        self.img_label = QtWidgets.QLabel(self.centralwidget)
        self.img_label.setText("")
        self.img_label.setPixmap(QtGui.QPixmap("data/animals/q.png"))
        self.img_label.setObjectName("img_label")
        self.gridLayout.addWidget(self.img_label, 2, 0, 1, 2)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 9, 0, 1, 2)
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setObjectName("pushButton_0")
        self.gridLayout.addWidget(self.pushButton_0, 5, 0, 1, 4)
        self.radioButton_1 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_1.setObjectName("radioButton_1")
        self.gridLayout.addWidget(self.radioButton_1, 7, 1, 1, 1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 7, 2, 1, 1)
        self.radioButton_3 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_3.setObjectName("radioButton_3")
        self.gridLayout.addWidget(self.radioButton_3, 7, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_0.setText(_translate("MainWindow", "10 раз"))
        self.label_0.setText(_translate("MainWindow", "Произнесите вслух вопрос и нажмите на кнопку"))
        self.pushButton_1.setText(_translate("MainWindow", "Уточнить подбросив монету"))
        self.label_1.setText(_translate("MainWindow", "Вероятность события при 10 :"))
        self.pushButton_0.setText(_translate("MainWindow", "Получить Ответ"))
        self.radioButton_1.setText(_translate("MainWindow", "100 раз"))
        self.radioButton_2.setText(_translate("MainWindow", "1000 раз"))
        self.radioButton_3.setText(_translate("MainWindow", "10000 раз"))

