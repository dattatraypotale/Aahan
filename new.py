# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!
from stockIn import Ui_Form
from report import  Ui_Form_Report
from saleHistory import Ui_Form3
import sqlite3
from reportlab.lib.pagesizes import letter
from num2words import num2words
from reportlab.lib.units import inch
import os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtCore, QtGui, QtWidgets
from datetime import date
from PyQt5.QtCore import QDate

class Ui_MainWindow(object):
    def __init__(self):
        f = open("E:/project/name_shop.txt", "r")
        self.shop_name = f.readline()
        self.owner_address = f.readline()
        self.owner_name = f.readline()
        self.owner_gst_tin = f.readline()
        self.owner_pan = f.readline()
        f.close()

        self.today_date = date.today()

        f = open('invoicenumber.txt', 'r')
        self.invoice_number = f.read()
        f.close()
        print("Invoice Number :", self.invoice_number)

        self.PDF_name = self.invoice_number
        print("PFD name initiated(init)")

        self.first_name = ""
        self.middle_name = ""
        self.last_name = ""
        self.customer_address = ""
        self.customer_pin = ""
        self.customer_mob = ""
        self.customer_pan = ""
        self.customer_state = ""
        self.customer_gst_tin = ""
        self.customer_vat_tin = ""
        self.customer_email = ""

        self.item_name = ""
        self.item_hsn_code = ""
        self.item_model_number = ""
        self.item_ime_number = ""
        self.item_rate = ""
        self.item_quantity = ""
        self.item_amount = ""

        self.payment_mode = ""

        self.net_amount = 0
        self.grand_total = 0
        self.state_gst_amount = 0
        self.central_gst_amount = 0
        self.product_cost = 0

    def state_changed(self):
        if self.checkBox.isChecked():
            Ui_MainWindow.gst_enable(self)
            print("CHECKED!")
        else:
            Ui_MainWindow.gst_disable(self)
            print("UNCHECKED!")

    def invoice_incrementer(self):
        invoice_number = self.invoice_number
        invoice_str = invoice_number.split("i", 2)
        print(type(int(invoice_str[1])))
        invoice_num = int(invoice_str[1])
        invoice_num = invoice_num + 1
        print("Laxmi" + invoice_str[1])
        # print("Laxmi"+str(invoice_num))
        new_invoice_number = "Laxmi" + str(invoice_num)
        print(new_invoice_number)
        f = open('invoicenumber.txt', 'w')
        f.write(new_invoice_number)
        f.close()
        return new_invoice_number

    def clickMethodR(self):
        # Method for refresh botton(Invoice number)
        print("inside clickmethodR")
        self.invoice_number = Ui_MainWindow.invoice_incrementer(self)
        self.PDF_name = self.invoice_number
        self.lineEdit.setText(self.invoice_number)

    def click_method_ok(self):
        Ui_MainWindow.customer_data(self)
        Ui_MainWindow.item_data(self)
        Ui_MainWindow.calculus(self)

    def click_method_generatebill(self):
        print("generate mobile bill PDF")
        Ui_MainWindow.create_mobile_pdf(self)
        Ui_MainWindow.open_mobile_Pdf(self)

    def click_method_stock_in(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 120, 1001, 341))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(10, 10, 981, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setLineWidth(1)
        self.frame_4.setObjectName("frame_4")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setGeometry(QtCore.QRect(16, 10, 101, 31))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit.setGeometry(QtCore.QRect(120, 10, 131, 31))
        self.lineEdit.setInputMask("")
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_2.setGeometry(QtCore.QRect(832, 10, 131, 31))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setGeometry(QtCore.QRect(790, 10, 41, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_4)
        self.pushButton.setGeometry(QtCore.QRect(260, 10, 41, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 121, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 81, 31))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 120, 121, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 120, 121, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(150, 90, 91, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 120, 121, 31))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(290, 90, 71, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 61, 31))
        self.label_7.setObjectName("label_7")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(20, 180, 161, 31))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 180, 81, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(190, 150, 31, 31))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(300, 180, 121, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(290, 150, 91, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(440, 150, 31, 31))
        self.label_10.setObjectName("label_10")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_9.setGeometry(QtCore.QRect(440, 180, 101, 31))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setGeometry(QtCore.QRect(550, 180, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.frame_2)
        self.checkBox.setGeometry(QtCore.QRect(670, 70, 41, 17))
        self.checkBox.setObjectName("checkBox")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(720, 70, 71, 31))
        self.label_11.setObjectName("label_11")
        self.label_11.hide()
        self.lineEdit_10 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_10.setGeometry(QtCore.QRect(790, 80, 121, 21))
        self.lineEdit_10.hide()
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_23 = QtWidgets.QLabel(self.frame_2)
        self.label_23.setGeometry(QtCore.QRect(720, 100, 71, 31))
        self.label_23.hide()
        self.label_23.setObjectName("label_23")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_21.setGeometry(QtCore.QRect(790, 110, 121, 21))
        self.lineEdit_21.hide()
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(790, 140, 121, 21))
        self.lineEdit_22.hide()
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_24 = QtWidgets.QLabel(self.frame_2)
        self.label_24.setGeometry(QtCore.QRect(750, 130, 41, 31))
        self.label_24.hide()
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.frame_2)
        self.label_25.setGeometry(QtCore.QRect(10, 230, 111, 21))
        self.label_25.setObjectName("label_25")
        self.tableWidget = QtWidgets.QTableWidget(self.frame_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 260, 721, 71))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(890, 270, 91, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.splitter_10 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_10.setGeometry(QtCore.QRect(760, 270, 101, 51))
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.label_35 = QtWidgets.QLabel(self.splitter_10)
        self.label_35.setObjectName("label_35")
        self.comboBox_2 = QtWidgets.QComboBox(self.splitter_10)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 1181, 101))
        self.frame.setAutoFillBackground(False)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setGeometry(QtCore.QRect(10, 10, 571, 81))
        self.frame_6.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.label_12 = QtWidgets.QLabel(self.frame_6)
        self.label_12.setGeometry(QtCore.QRect(20, 10, 531, 31))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setGeometry(QtCore.QRect(20, 40, 521, 31))
        self.label_13.setObjectName("label_13")
        self.frame_7 = QtWidgets.QFrame(self.frame)
        self.frame_7.setGeometry(QtCore.QRect(880, 10, 281, 81))
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 231, 31))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.frame_7)
        self.label_15.setGeometry(QtCore.QRect(10, 40, 231, 31))
        self.label_15.setObjectName("label_15")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(19, 469, 1001, 161))
        self.frame_3.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.splitter = QtWidgets.QSplitter(self.frame_3)
        self.splitter.setGeometry(QtCore.QRect(10, 10, 207, 21))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_26 = QtWidgets.QLabel(self.splitter)
        self.label_26.setObjectName("label_26")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.splitter_7 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_7.setGeometry(QtCore.QRect(220, 10, 411, 51))
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.splitter_5 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.label_30 = QtWidgets.QLabel(self.splitter_5)
        self.label_30.setObjectName("label_30")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.splitter_5)
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.label_31 = QtWidgets.QLabel(self.splitter_5)
        self.label_31.setObjectName("label_31")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.splitter_5)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.splitter_6 = QtWidgets.QSplitter(self.splitter_7)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.label_27 = QtWidgets.QLabel(self.splitter_6)
        self.label_27.setObjectName("label_27")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.splitter_6)
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_28 = QtWidgets.QLabel(self.splitter_6)
        self.label_28.setObjectName("label_28")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.splitter_6)
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.splitter_4 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_4.setGeometry(QtCore.QRect(670, 10, 209, 51))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.splitter_3 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_29 = QtWidgets.QLabel(self.splitter_3)
        self.label_29.setObjectName("label_29")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.splitter_3)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_4)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.label_32 = QtWidgets.QLabel(self.splitter_2)
        self.label_32.setObjectName("label_32")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.splitter_2)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.layoutWidget = QtWidgets.QWidget(self.frame_3)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 90, 200, 48))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter_8 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_33 = QtWidgets.QLabel(self.splitter_8)
        self.label_33.setObjectName("label_33")
        self.lineEdit_30 = QtWidgets.QLineEdit(self.splitter_8)
        self.lineEdit_30.setObjectName("lineEdit_30")
        self.verticalLayout.addWidget(self.splitter_8)
        self.splitter_9 = QtWidgets.QSplitter(self.layoutWidget)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.label_34 = QtWidgets.QLabel(self.splitter_9)
        self.label_34.setObjectName("label_34")
        self.lineEdit_31 = QtWidgets.QLineEdit(self.splitter_9)
        self.lineEdit_31.setObjectName("lineEdit_31")
        self.verticalLayout.addWidget(self.splitter_9)
        self.splitter_11 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_11.setGeometry(QtCore.QRect(620, 100, 371, 41))
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.pushButton_4 = QtWidgets.QPushButton(self.splitter_11)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.splitter_11)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.splitter_11)
        self.pushButton_6.setObjectName("pushButton_6")
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setGeometry(QtCore.QRect(1030, 120, 151, 511))
        self.frame_5.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.pushButton_10 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 230, 131, 67))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_11.setGeometry(QtCore.QRect(10, 430, 131, 67))
        self.pushButton_11.setObjectName("pushButton_11")
        self.splitter_12 = QtWidgets.QSplitter(self.frame_5)
        self.splitter_12.setGeometry(QtCore.QRect(10, 10, 131, 211))
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.pushButton_7 = QtWidgets.QPushButton(self.splitter_12)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.splitter_12)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.splitter_12)
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.actionProfit_loss_statemet = QtWidgets.QAction(MainWindow)
        self.actionProfit_loss_statemet.setObjectName("actionProfit_loss_statemet")
        self.menubar.addAction(self.menuFile.menuAction())

        # set font to lable in headers  like shop name,etc
        newfont = QtGui.QFont("Times", 12, QtGui.QFont.Bold)
        self.label_12.setFont(newfont)
        self.label_13.setFont(newfont)
        self.label_14.setFont(newfont)
        self.label_15.setFont(newfont)
        # set color to lable
        self.label_12.setStyleSheet('color: red')
        self.label_13.setStyleSheet('color: red')
        self.label_14.setStyleSheet('color: red')
        self.label_15.setStyleSheet('color: red')

        f = self.lineEdit_3.font()
        f.setPointSize(12)

        print("local time :", self.today_date.strftime("%d - %B - %y"))
        self.lineEdit_2.setText(str(self.today_date.strftime("%d-%b-%Y")))
        self.lineEdit.setText(str(self.invoice_number))
        self.lineEdit_2.setFont(f)
        self.lineEdit.setFont(f)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def gst_enable(self):
        self.label_11.show()
        self.label_23.show()
        self.label_24.show()
        self.lineEdit_10.show()
        self.lineEdit_21.show()
        self.lineEdit_22.show()

    def gst_disable(self):
        self.label_11.hide()
        self.label_23.hide()
        self.label_24.hide()
        self.lineEdit_10.hide()
        self.lineEdit_21.hide()
        self.lineEdit_22.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mobile GST Invoice"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Invoice Number :</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Date :</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "R"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Custmer Details :</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">First Name :</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Middle Name :</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Last Name :</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Address :</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Pin :</span></p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Mob number :</span></p></body></html>"))
        self.label_10.setText(_translate("MainWindow", "<html><head/><body><p>PAN :</p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Maharashtra 27", "27"))
        self.checkBox.setText(_translate("MainWindow", "GST"))
        self.label_11.setText(_translate("MainWindow", "<html><head/><body><p>GST TIN No :</p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "<html><head/><body><p>VAT TIN No :</p></body></html>"))
        self.label_24.setText(_translate("MainWindow", "<html><head/><body><p>Email :</p></body></html>"))
        self.label_25.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Product Details :</span></p></body></html>"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "HSN Code"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Model No."))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "IMEI No."))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Amount"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
        self.label_35.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">Payment Mode :</span></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "Cash"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "Credit Card"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "Bajaj Finance"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "Home Credit Finance"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "Capital Finance"))
        self.comboBox_2.setItemText(5, _translate("MainWindow", "TVS Finance"))
        self.comboBox_2.setItemText(6, _translate("MainWindow", "HDB Finance"))
        self.comboBox_2.setItemText(7, _translate("MainWindow", "Other"))
        self.label_12.setText(_translate("MainWindow", self.shop_name))
        self.label_13.setText(_translate("MainWindow", self.owner_address))
        self.label_14.setText(_translate("MainWindow", self.owner_name))
        self.label_15.setText(_translate("MainWindow", self.owner_gst_tin))
        self.label_26.setText(_translate("MainWindow", "<html><head/><body><p>Gross Amount :</p></body></html>"))
        self.label_30.setText(_translate("MainWindow", "<html><head/><body><p>CGST Amount :</p></body></html>"))
        self.label_31.setText(_translate("MainWindow", "<html><head/><body><p>SGST Amount :</p></body></html>"))
        self.label_27.setText(_translate("MainWindow", "<html><head/><body><p>CGST %  :</p></body></html>"))
        self.lineEdit_24.setPlaceholderText(_translate("MainWindow", "6"))
        self.label_28.setText(_translate("MainWindow", "<html><head/><body><p>SGST % :</p></body></html>"))
        self.lineEdit_25.setPlaceholderText(_translate("MainWindow", "6"))
        self.label_29.setText(_translate("MainWindow", "<html><head/><body><p>NET Amount :</p></body></html>"))
        self.label_32.setText(_translate("MainWindow", "<html><head/><body><p>Grand Amount :</p></body></html>"))
        self.label_33.setText(_translate("MainWindow", "<html><head/><body><p>Amount Pay :</p></body></html>"))
        self.label_34.setText(_translate("MainWindow", "<html><head/><body><p>Due:</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Generate Bill"))
        self.pushButton_5.setText(_translate("MainWindow", "Preview Bill"))
        self.pushButton_6.setText(_translate("MainWindow", "Save"))
        self.pushButton_10.setText(_translate("MainWindow", "Reports"))
        self.pushButton_11.setText(_translate("MainWindow", "New Bill"))
        self.pushButton_7.setText(_translate("MainWindow", "StockIn"))
        self.pushButton_8.setText(_translate("MainWindow", "Sale"))
        self.pushButton_9.setText(_translate("MainWindow", "Edit Bill"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionProfit_loss_statemet.setText(_translate("MainWindow", "profit/loss statement"))

        # pushButton Click Events
        self.pushButton.clicked.connect(self.clickMethodR)
        self.pushButton_3.clicked.connect(self.click_method_ok)
        self.pushButton_4.clicked.connect(self.click_method_generatebill)
        # checkbox state change
        self.checkBox.stateChanged.connect(self.state_changed)
        self.pushButton_7.clicked.connect(self.click_method_stock_in)
        self.pushButton_6.clicked.connect(self.save_bill)
        self.pushButton_8.clicked.connect(self.sale)
        self.pushButton_10.clicked.connect(self.reports)

    def sale(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Form3()
        self.ui.setupUi3(self.window3)
        self.window3.show()

    def reports(self):
        self.window_report = QtWidgets.QMainWindow()
        self.ui_report = Ui_Form_Report()
        self.ui_report.setupUi_Report(self.window_report)
        self.window_report.show()

    def customer_data(self):
        self.first_name = self.lineEdit_3.text()
        self.middle_name = self.lineEdit_4.text()
        self.last_name = self.lineEdit_5.text()
        self.customer_address = self.lineEdit_6.text()
        self.customer_pin = self.lineEdit_7.text()
        self.customer_mob = self.lineEdit_8.text()
        self.customer_pan = self.lineEdit_9.text()
        self.customer_state = str(self.comboBox.currentText())
        self.customer_gst_tin = self.lineEdit_10.text()
        self.customer_vat_tin = self.lineEdit_21.text()
        self.customer_email = self.lineEdit_22.text()
        self.payment_mode = str(self.comboBox_2.currentText())
        print("{} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.invoice_number, self.today_date, self.first_name,
                                                  self.middle_name, self.last_name, self.customer_address, self.customer_pin,
                                               self.customer_mob, self.customer_pan, self.customer_state,self.customer_gst_tin,
                                                           self.customer_vat_tin, self.customer_email, self.payment_mode))

    def item_data(self):
        self.item_name = self.tableWidget.item(0, 0).text()
        self.item_hsn_code = self.tableWidget.item(0, 1).text()
        self.item_model_number = self.tableWidget.item(0, 2).text()
        self.item_ime_number = self.tableWidget.item(0, 3).text()
        self.item_rate = self.tableWidget.item(0, 4).text()
        self.item_quantity = self.tableWidget.item(0, 5).text()
        self.item_amount = str(int(self.item_rate) * int(self.item_quantity))
        print("{} {} {} {} {} {} {}".format(self.item_name, self.item_hsn_code, self.item_model_number,self.item_ime_number,
                                            self.item_rate, self.item_quantity, self.item_amount))

    def calculus(self):
        self.tableWidget.setItem(0, 6, QTableWidgetItem(str(self.item_amount)))
        gross_amount = 0

        gross_amount = int(self.item_amount)
        self.state_gst_amount = (gross_amount * 6) / 100
        self.central_gst_amount = (gross_amount * 6) / 100

        # '{0:.2f}'.format(pi)
        self.product_cost = '{0:.2f}'.format(gross_amount - (self.state_gst_amount + self.central_gst_amount))
        print("\nproduct cost :", self.product_cost)
        print("State_GST_Amount 6% :", '{0:.2f}'.format(self.state_gst_amount))
        print("Central_GST_Amount 6% :", '{0:.2f}'.format(self.central_gst_amount))

        self.net_amount = '{0:.2f}'.format(gross_amount)
        #self.grand_total = '{0:.2f}'.format(gross_amount)
        self.grand_total = gross_amount

        print("Net_Amount : ", self.net_amount)
        print("Grand_Total : ", self.grand_total)
        self.lineEdit_23.setText(str(gross_amount))
        self.lineEdit_28.setText(str(self.state_gst_amount))
        self.lineEdit_27.setText(str(self.central_gst_amount))
        self.lineEdit_26.setText(str(self.net_amount))
        self.lineEdit_29.setText(str(self.grand_total))
        self.lineEdit_30.setText(str(self.grand_total))
        self.lineEdit_31.setText(str("0"))

    def open_mobile_Pdf(self):
        os.startfile(self.PDF_name + ".pdf")

    def create_mobile_pdf(self):
        from reportlab.pdfgen import canvas
        canvas = canvas.Canvas(self.PDF_name + ".pdf", pagesize=letter)
        # 8.5*11
        # canvas.rect(x, y, width, height, stroke=1, fill=0)
        canvas.rect(0.6 * inch, 2 * inch, 7.5 * inch, 8.5 * inch, stroke=1, fill=0)
        # 2nd horizontal line | header
        canvas.line(0.6 * inch, 8.2 * inch, 8.1 * inch, 8.2 * inch)
        # 1nd  line | header
        canvas.line(0.6 * inch, 8.9 * inch, 8.1 * inch, 8.9 * inch)
        # header 1st vertical line | header
        canvas.line(4.5 * inch, 8.2 * inch, 4.5 * inch, 10.5 * inch)

        canvas.setFont('Helvetica', 8)
        canvas.drawString(120, 740, "CHALLAN CUM GST INVOICE")
        canvas.setFont('Helvetica', 16)
        canvas.drawString(60, 720, "Laxmi Mobile Shoppy & Gift House")
        canvas.setFont('Helvetica', 9)
        canvas.drawString(75, 705, "Gate No 684, Wadgoan Chock, AP Alandi Devachi")
        canvas.drawString(95, 690, "Tal Khed, Dist Pune-410501")
        canvas.setFont('Helvetica', 8)
        canvas.drawString(75, 675, "Dashrath Bhandare Mob.: 7743818140,9890603047")
        canvas.drawString(85, 660, "E-Mail : DashrathBhandare65.db@gmail.com")

        canvas.setFont('Helvetica', 9)
        canvas.drawString(330, 745, "Invoice Number:")
        canvas.drawString(330, 718, "Buyer Order Number:")
        canvas.drawString(330, 690, "GST TIN Number:")
        canvas.drawString(330, 660, "State Name:")
        canvas.drawString(330, 632, "GST TIN:")
        canvas.drawString(330, 610, "PAN Number:")

        canvas.drawString(450, 745, "Date:")
        canvas.drawString(450, 718, "Payment Mode:")
        canvas.drawString(450, 690, "PAN Number:")
        canvas.drawString(450, 660, "State Code:")
        canvas.drawString(450, 632, "VAT TIN Number:")
        canvas.drawString(450, 610, "State Name:")

        canvas.setFont('Helvetica', 9)
        canvas.drawString(45, 580, "Sr")
        canvas.drawString(80, 580, "Description of Goods")
        canvas.drawString(196, 580, "HSN/SAC No.")
        canvas.drawString(270, 580, "IMEI No.")
        canvas.drawString(350, 580, "Model No.")
        canvas.drawString(415, 580, "Qty")
        canvas.drawString(445, 580, "Rate")
        canvas.drawString(515, 580, "Total Amount")

        # canvas.setFont('Helvetica', 9)
        canvas.drawString(330, 278, "Total :")
        canvas.drawString(330, 263, "CGST 6% :")
        canvas.drawString(330, 250, "SGST 6% :")
        canvas.drawString(330, 236, "Grand Total :")
        canvas.drawString(330, 221, "Paid Amount :")
        canvas.drawString(330, 207, "Remaining Dues :")

        canvas.setFont('Helvetica', 10)
        #canvas.drawString(48, 190, "Total Outstanding")
        canvas.drawString(50, 147, "Customer Sign")
        canvas.drawString(370, 147, "For Laxmi Mobile Shoppy & Gift House")

        canvas.setFont('Helvetica', 9)
        canvas.drawString(45, 630, "To")
        canvas.drawString(50, 620, "Name :")
        canvas.drawString(50, 605, "Address :")

        # declaration
        canvas.drawString(135, 178, "We Declare that this invoice shows actual ")
        canvas.drawString(135, 168, "price of the goods described and that all")
        canvas.drawString(135, 158, "perticulars are true and correct")

        # act
        canvas.setFont('Helvetica', 8)
        canvas.drawString(45, 275, "I/We here by that my/our registration certificate inder the maharashtra VAT")
        canvas.drawString(45, 265, "ACT 2002 is in force on the date on which sale of goods specified in this tax")
        canvas.drawString(45, 255, "invoice is made by me & it shall be accounted for in the turnover of sales ")
        canvas.drawString(45, 245, "while filling of return & due tax, if any.payble on the sale has been paid or")
        canvas.drawString(45, 235, "shall be paid")

        canvas.setFont('Helvetica', 9)
        canvas.drawString(135, 190, "Amount in Words :")
        canvas.drawString(210, 190, num2words(self.grand_total))

        canvas.setFont('Helvetica', 7)
        canvas.drawString(250, 130, "SUBJECT TO PUNE JURISDICTION")
        canvas.setFont('Helvetica', 6)
        canvas.drawString(260, 121, "This is Computer Generated Invoice")

        # body
        # canvas.line(4.5 * inch, 8.2 * inch, 4.5 * inch, 4 * inch)
        # sr.no
        canvas.line(0.9 * inch, 8.2 * inch, 0.9 * inch, 4 * inch)
        # total Amount
        canvas.line(7.1 * inch, 8.2 * inch, 7.1 * inch, 4 * inch)
        # Rate
        canvas.line(6.1 * inch, 8.2 * inch, 6.1 * inch, 4 * inch)
        # qty
        canvas.line(5.7 * inch, 8.2 * inch, 5.7 * inch, 4 * inch)
        # IMEI NO
        canvas.line(4.7 * inch, 8.2 * inch, 4.7 * inch, 4 * inch)
        # Model Number
        canvas.line(3.5 * inch, 8.2 * inch, 3.5 * inch, 4 * inch)
        # HSN Numbe5
        canvas.line(2.7 * inch, 8.2 * inch, 2.7 * inch, 4 * inch)

        # Name field
        canvas.line(0.6 * inch, 8 * inch, 8.1 * inch, 8 * inch)

        # second horizontal line | total
        canvas.line(0.6 * inch, 4 * inch, 8.1 * inch, 4 * inch)
        canvas.line(0.6 * inch, 4.2 * inch, 8.1 * inch, 4.2 * inch)
        # header 2st vertical line | footer
        canvas.line(4.5 * inch, 4 * inch, 4.5 * inch, 2.8 * inch)

        # third horizontal line | footer
        canvas.line(0.6 * inch, 2.8 * inch, 8.1 * inch, 2.8 * inch)
        # total in word..................
        canvas.line(1.8 * inch, 2.6 * inch, 8.1 * inch, 2.6 * inch)

        # canvas.setFont('Helvetica', 12)
        # canvas.drawString(100, 170, name)

        # Invoice number table 3 line
        canvas.line(4.5 * inch, 10.1 * inch, 8.1 * inch, 10.1 * inch)
        canvas.line(4.5 * inch, 9.7 * inch, 8.1 * inch, 9.7 * inch)
        canvas.line(4.5 * inch, 9.3 * inch, 8.1 * inch, 9.3 * inch)

        # PAN table line
        canvas.line(4.5 * inch, 8.6 * inch, 8.1 * inch, 8.6 * inch)
        # vertical line for both table
        canvas.line(6.2 * inch, 8.2 * inch, 6.2 * inch, 10.5 * inch)

        # total colom
        canvas.line(4.5 * inch, 3.8 * inch, 8.1 * inch, 3.8 * inch)
        canvas.line(4.5 * inch, 3.6 * inch, 8.1 * inch, 3.6 * inch)
        canvas.line(4.5 * inch, 3.4 * inch, 8.1 * inch, 3.4 * inch)
        canvas.line(4.5 * inch, 3.2 * inch, 8.1 * inch, 3.2 * inch)
        canvas.line(4.5 * inch, 3 * inch, 8.1 * inch, 3 * inch)
        # vertical line
        canvas.line(6.2 * inch, 4 * inch, 6.2 * inch, 2.8 * inch)
        # Custmer sign
        canvas.line(1.8 * inch, 2.8 * inch, 1.8 * inch, 2 * inch)
        # owner sign
        canvas.line(4.5 * inch, 2.6 * inch, 4.5 * inch, 2 * inch)
        print("createPDF : PDF created");

        # set vakues in PDF
        canvas.setFont('Helvetica', 11)
        canvas.drawString(333, 733, str(self.invoice_number))
        canvas.drawString(333, 705, "NA")
        canvas.drawString(333, 678, self.owner_gst_tin)
        canvas.drawString(333, 648, "Maharastra")
        canvas.drawString(333, 621, str(self.customer_gst_tin))
        canvas.drawString(333, 597, str(self.customer_pan))

        canvas.drawString(453, 733, str(self.today_date))
        canvas.drawString(453, 705, self.payment_mode)
        canvas.drawString(453, 678, self.owner_pan)
        # state code under dev
        canvas.drawString(453, 648, "27")
        canvas.drawString(453, 621, str(self.customer_vat_tin))
        #stare in progress
        canvas.drawString(453, 597, str(self.customer_state))

        # Name and address
        canvas.drawString(85, 620, self.first_name+" "+self.middle_name+" "+self.last_name)
        canvas.drawString(89, 605, str(self.customer_address))

        # body
        canvas.drawString(50, 560, "1")
        canvas.drawString(75, 560, str(self.item_name))
        canvas.drawString(197, 560, str(self.item_hsn_code))
        canvas.drawString(255, 560, str(self.item_ime_number))
        canvas.drawString(340, 560, str(self.item_model_number))
        canvas.drawString(415, 560, str(self.item_quantity))
        canvas.drawString(443, 560, str(self.item_rate))
        canvas.drawString(514, 560, str(self.product_cost))

        # cal
        canvas.drawString(450, 278, str(self.product_cost))
        canvas.drawString(450, 262, str(self.central_gst_amount))
        canvas.drawString(450, 248, str(self.state_gst_amount))
        canvas.drawString(450, 234, str(self.grand_total))
        canvas.drawString(450, 219, str(self.grand_total))
        canvas.drawString(450, 205, "0")

        canvas.save()

    def save_bill(self):
        self.first_name = self.lineEdit_3.text()
        self.middle_name = self.lineEdit_4.text()
        self.last_name = self.lineEdit_5.text()
        cust_name = str(self.first_name+" "+self.middle_name+" "+self.last_name)
        self.customer_address = self.lineEdit_6.text()
        self.customer_pin = self.lineEdit_7.text()
        self.customer_mob = self.lineEdit_8.text()
        self.customer_pan = self.lineEdit_9.text()
        self.customer_state = str(self.comboBox.currentText())
        self.customer_gst_tin = self.lineEdit_10.text()
        self.customer_vat_tin = self.lineEdit_21.text()
        self.customer_email = self.lineEdit_22.text()
        self.payment_mode = str(self.comboBox_2.currentText())
        self.item_name = self.tableWidget.item(0, 0).text()
        self.item_hsn_code = self.tableWidget.item(0, 1).text()
        self.item_model_number = self.tableWidget.item(0, 2).text()
        self.item_ime_number = self.tableWidget.item(0, 3).text()
        self.item_rate = self.tableWidget.item(0, 4).text()
        self.item_quantity = self.tableWidget.item(0, 5).text()
        self.item_amount = str(int(self.item_rate) * int(self.item_quantity))
        buy_amount = 0
        vendor = "abc"
        data = [self.invoice_number, cust_name, self.item_name, self.item_model_number, self.item_hsn_code, self.item_ime_number,
                self.item_amount, buy_amount, self.today_date, self.item_rate, self.item_quantity, self.state_gst_amount,
                self.central_gst_amount, self.grand_total, self.customer_address, self.customer_pin, self.customer_mob,
                self.payment_mode, self.customer_gst_tin, self.customer_vat_tin, self.customer_state, vendor]

        conn = sqlite3.connect('mymobileshoppy.db')
        c = conn.cursor()
        sql = "INSERT INTO sales (Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor)" \
              " VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        c.execute(sql, data)
        conn.commit()
        print("Records saved successfully")
        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('photo.jpg'))
    MainWindow = QtWidgets.QMainWindow()
    p = MainWindow.palette()
    p.setColor(MainWindow.backgroundRole(), Qt.white)
    MainWindow.setPalette(p)
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

