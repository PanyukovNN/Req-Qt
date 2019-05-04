# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'req.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(591, 685)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dataEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.dataEdit.setGeometry(QtCore.QRect(20, 100, 171, 25))
        self.dataEdit.setObjectName("dataEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 101, 17))
        self.label.setObjectName("label")
        self.fabulaInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.fabulaInput.setGeometry(QtCore.QRect(20, 160, 551, 111))
        self.fabulaInput.setObjectName("fabulaInput")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 290, 151, 17))
        self.label_3.setObjectName("label_3")
        self.personInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.personInput.setGeometry(QtCore.QRect(20, 310, 551, 281))
        self.personInput.setObjectName("personInput")
        self.readyButton = QtWidgets.QPushButton(self.centralwidget)
        self.readyButton.setGeometry(QtCore.QRect(450, 610, 121, 31))
        self.readyButton.setObjectName("readyButton")
        self.numberEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.numberEdit.setGeometry(QtCore.QRect(210, 100, 171, 25))
        self.numberEdit.setObjectName("numberEdit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(210, 80, 101, 17))
        self.label_4.setObjectName("label_4")
        self.mpRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.mpRadioButton.setGeometry(QtCore.QRect(20, 20, 181, 23))
        self.mpRadioButton.setAcceptDrops(False)
        self.mpRadioButton.setToolTipDuration(-1)
        self.mpRadioButton.setAutoFillBackground(False)
        self.mpRadioButton.setChecked(True)
        self.mpRadioButton.setObjectName("mpRadioButton")
        self.udRadioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.udRadioButton.setGeometry(QtCore.QRect(20, 50, 181, 23))
        self.udRadioButton.setObjectName("udRadioButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 80, 161, 17))
        self.label_5.setObjectName("label_5")
        self.placeEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.placeEdit.setGeometry(QtCore.QRect(400, 100, 171, 25))
        self.placeEdit.setObjectName("placeEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 610, 291, 17))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 591, 22))
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
        self.label.setText(_translate("MainWindow", "Дата:"))
        self.label_2.setText(_translate("MainWindow", "Фабула:"))
        self.label_3.setText(_translate("MainWindow", "Данные лиц:"))
        self.personInput.setPlainText(_translate("MainWindow", "ФИО:\n"
"Адрес:"))
        self.readyButton.setText(_translate("MainWindow", "Готово"))
        self.label_4.setText(_translate("MainWindow", "Номер уд/мп:"))
        self.mpRadioButton.setText(_translate("MainWindow", "Материал проверки"))
        self.udRadioButton.setText(_translate("MainWindow", "Уголовное дело"))
        self.label_5.setText(_translate("MainWindow", "Населенный пункит:"))

