# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'saleHistory.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from datetime import date
from PyQt5.QtCore import QDate, Qt
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form3(object):
    def setupUi3(self, Form):
        Form.setObjectName("Form")
        Form.resize(1004, 594)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(15, 161, 981, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(23)
        self.tableWidget.setRowCount(0)
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
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(22, item)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 30, 296, 120))
        self.frame.setFrameShape(QtWidgets.QFrame.Panel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 0, 0, 1, 1)
        self.dateEdit = QtWidgets.QDateEdit(self.frame)
        self.dateEdit.setObjectName("dateEdit")
        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_3.setObjectName("checkBox_3")
        self.gridLayout.addWidget(self.checkBox_3, 0, 3, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout.addWidget(self.checkBox_2, 1, 0, 1, 3)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 3, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.verticalLayout.addWidget(self.dateEdit_2)
        self.dateEdit_3 = QtWidgets.QDateEdit(self.frame)
        self.dateEdit_3.setObjectName("dateEdit_3")
        self.verticalLayout.addWidget(self.dateEdit_3)
        self.gridLayout.addLayout(self.verticalLayout, 2, 2, 2, 1)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 3, 2, 1)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(480, 10, 61, 20))
        self.label.setObjectName("label")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 500, 991, 91))
        self.frame_2.setFrameShape(QtWidgets.QFrame.Box)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.splitter_10 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_10.setGeometry(QtCore.QRect(20, 10, 193, 51))
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.label_8 = QtWidgets.QLabel(self.splitter_11)
        self.label_8.setObjectName("label_8")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.splitter_11)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_12.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_12.setObjectName("splitter_12")
        self.label_9 = QtWidgets.QLabel(self.splitter_12)
        self.label_9.setObjectName("label_9")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.splitter_12)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.splitter_13 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_13.setGeometry(QtCore.QRect(470, 10, 193, 51))
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")
        self.splitter_14 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_14.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_14.setObjectName("splitter_14")
        self.label_10 = QtWidgets.QLabel(self.splitter_14)
        self.label_10.setObjectName("label_10")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.splitter_14)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.splitter_15 = QtWidgets.QSplitter(self.splitter_13)
        self.splitter_15.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_15.setObjectName("splitter_15")
        self.label_11 = QtWidgets.QLabel(self.splitter_15)
        self.label_11.setObjectName("label_11")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.splitter_15)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.splitter_9 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_9.setGeometry(QtCore.QRect(240, 10, 193, 51))
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_8.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_8.setObjectName("splitter_8")
        self.label_6 = QtWidgets.QLabel(self.splitter_8)
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.splitter_8)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_7.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_7.setObjectName("splitter_7")
        self.label_7 = QtWidgets.QLabel(self.splitter_7)
        self.label_7.setObjectName("label_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.splitter_7)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.splitter = QtWidgets.QSplitter(self.frame_2)
        self.splitter.setGeometry(QtCore.QRect(730, 19, 191, 41))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.splitter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Invoice Number"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Customer Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Model Number"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "HSR code"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "IMEI Number"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Sale Amount"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Buy Amount"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Date"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Rate"))
        item = self.tableWidget.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Quantity"))
        item = self.tableWidget.horizontalHeaderItem(11)
        item.setText(_translate("Form", "SGST Amount"))
        item = self.tableWidget.horizontalHeaderItem(12)
        item.setText(_translate("Form", "CGST Amount"))
        item = self.tableWidget.horizontalHeaderItem(13)
        item.setText(_translate("Form", "Grand Amount"))
        item = self.tableWidget.horizontalHeaderItem(14)
        item.setText(_translate("Form", "Address"))
        item = self.tableWidget.horizontalHeaderItem(15)
        item.setText(_translate("Form", "PIN"))
        item = self.tableWidget.horizontalHeaderItem(16)
        item.setText(_translate("Form", "Phone Number"))
        item = self.tableWidget.horizontalHeaderItem(17)
        item.setText(_translate("Form", "Payment Mode"))
        item = self.tableWidget.horizontalHeaderItem(18)
        item.setText(_translate("Form", "GST TIN Number"))
        item = self.tableWidget.horizontalHeaderItem(19)
        item.setText(_translate("Form", "VAT TIN Number"))
        item = self.tableWidget.horizontalHeaderItem(20)
        item.setText(_translate("Form", "State"))
        item = self.tableWidget.horizontalHeaderItem(21)
        item.setText(_translate("Form", "Vendor"))
        item = self.tableWidget.horizontalHeaderItem(22)
        item.setText(_translate("Form", "checked"))
        self.checkBox.setText(_translate("Form", "Day"))
        self.checkBox_3.setText(_translate("Form", "Vendor"))
        self.checkBox_2.setText(_translate("Form", " In Between"))
        self.label_2.setText(_translate("Form", "From "))
        self.pushButton.setText(_translate("Form", "Search"))
        self.label_3.setText(_translate("Form", "To "))
        self.label.setText(_translate("Form", "Sale History"))
        self.label_8.setText(_translate("Form", "Total Cost :"))
        self.label_9.setText(_translate("Form", "Total Sale :"))
        self.label_10.setText(_translate("Form", "Quantity :"))
        self.label_11.setText(_translate("Form", "Grand Sale"))
        self.label_6.setText(_translate("Form", "Total SGST :"))
        self.label_7.setText(_translate("Form", "Total CGST :"))
        self.label_4.setText(_translate("Form", "Profit/Loss :"))

        now = QDate.currentDate()
        self.dateEdit.setDate(now)
        self.dateEdit_2.setDate(now)
        self.dateEdit_3.setDate(now)

        self.dateEdit.setCalendarPopup(True)
        self.dateEdit_2.setCalendarPopup(True)
        self.dateEdit_3.setCalendarPopup(True)

        self.checkBox.stateChanged.connect(self.make_selection)
        self.checkBox_2.stateChanged.connect(self.make_selection2)
        self.checkBox_3.stateChanged.connect(self.make_selection3)
        # self.pushButton.clicked.connect(self.search_query)
        # self.pushButton.clicked.connect(self.search_query2)
        # self.pushButton.clicked.connect(self.search_query3)
        self.pushButton.clicked.connect(self.search_sale_query)

    def make_selection(self):
        if self.checkBox.isChecked():
            print("date")
            self.checkBox_2.setChecked(False)

    def make_selection2(self):
        if self.checkBox_2.isChecked():
            print("inbetween")
            self.checkBox.setChecked(False)

    def make_selection3(self):
        if self.checkBox_3.isChecked():
            print("In vendor")

    def search_query(self):
        if self.checkBox_3.isChecked():
            vendor = self.lineEdit.text()
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Vendor = ?"
            result = c.execute(query, (vendor,))
            print(enumerate(result))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

    def search_query2(self):
        if self.checkBox.isChecked():
            today_date = self.dateEdit.date()
            selected_date = today_date.toPyDate()
            print(selected_date)
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date = ?"
            result = c.execute(query, (selected_date,))
            self.tableWidget.setRowCount(0) # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

    def search_query3(self):
        if self.checkBox_2.isChecked():
            from_date = self.dateEdit_2.date()
            to_date = self.dateEdit_3.date()
            from_selected_date = from_date.toPyDate()
            to_selected_date = to_date.toPyDate()
            print(from_selected_date)
            print(to_selected_date)

            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date >= ? and Purchse_Date <= ?"
            result = c.execute(query, (from_selected_date, to_selected_date,))
            self.tableWidget.setRowCount(0) # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

    def search_query4(self):
        if self.checkBox.isChecked() and self.checkBox_3.isChecked():
            today_date = self.dateEdit.date()
            selected_date = today_date.toPyDate()
            vendor = self.lineEdit.text()
            print(selected_date)
            print(vendor)
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date = ? and Vendor = ?"
            result = c.execute(query, (selected_date, vendor,))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

    def search_sale_query(self):
        total_cost = 0

        if self.checkBox_3.isChecked():
            vendor = self.lineEdit.text()
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Vendor = ?"
            result = c.execute(query, (vendor,))
            print(enumerate(result))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

        if self.checkBox.isChecked():
            today_date = self.dateEdit.date()
            selected_date = today_date.toPyDate()
            print(selected_date)
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date = ?"
            result = c.execute(query, (selected_date,))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

        if self.checkBox_2.isChecked():
            from_date = self.dateEdit_2.date()
            to_date = self.dateEdit_3.date()
            from_selected_date = from_date.toPyDate()
            to_selected_date = to_date.toPyDate()
            print(from_selected_date)
            print(to_selected_date)

            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date >= ? and Purchse_Date <= ?"
            result = c.execute(query, (from_selected_date, to_selected_date,))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

        if self.checkBox.isChecked() and self.checkBox_3.isChecked():
            today_date = self.dateEdit.date()
            selected_date = today_date.toPyDate()
            vendor = self.lineEdit.text()
            print(selected_date)
            print(vendor)
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date = ? and Vendor = ?"
            result = c.execute(query, (selected_date, vendor,))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

        if self.checkBox_2.isChecked() and self.checkBox_3.isChecked():
            from_date = self.dateEdit_2.date()
            to_date = self.dateEdit_3.date()
            from_selected_date = from_date.toPyDate()
            to_selected_date = to_date.toPyDate()
            vendor = self.lineEdit.text()
            print(from_selected_date)
            print(to_selected_date)
            print(vendor)
            conn = sqlite3.connect('mymobileshoppy.db')
            c = conn.cursor()
            query = "select Invoice_number,Cust_name, Prod_name, Model_number, HSR_code, IMEI_number, Sale_amount, Buy_amount, Purchse_Date, Rate, Quantity, SGST_amount, CGST_amount, Grand_amount, Address, PIN, Phone_number, Payment_mode, GST_TIN, VAT_TIN, Cust_State, Vendor from sales WHERE Purchse_Date >= ? and Purchse_Date <= ? and Vendor = ?"
            result = c.execute(query, (from_selected_date, to_selected_date, vendor,))
            self.tableWidget.setRowCount(0)  # clear table
            for row_number, row_data in enumerate(result):
                self.tableWidget.insertRow(row_number)
                for colomn_number, data in enumerate(row_data):
                    self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

            conn.close()

        Ui_Form3.calculate(self)

    def calculate(self):
        row_count = self.tableWidget.rowCount()
        print(row_count)
        total_sale = 0
        total_cost = 0
        total_SGST = 0
        total_CGST = 0
        grand_sale = 0
        qty = 0
        for num in range(row_count):
            print("ror {} : sale amount : {}".format(num, self.tableWidget.item(num, 6).text()))
            total_cost = total_cost + int(self.tableWidget.item(num, 7).text())
            total_sale = total_sale + int(self.tableWidget.item(num, 6).text())
            total_SGST = total_SGST + int(self.tableWidget.item(num, 11).text())
            total_CGST = total_CGST + int(self.tableWidget.item(num, 12).text())
            grand_sale = grand_sale + int(self.tableWidget.item(num, 13).text())
            qty = qty + int(self.tableWidget.item(num, 10).text())

        print(total_cost)
        print(total_sale)
        print(total_SGST)
        print(total_CGST)
        print(grand_sale)
        print(qty)

        profit = 0
        profit = grand_sale - total_cost

        self.lineEdit_8.setText(str(qty))
        self.lineEdit_6.setText(str(total_cost))
        self.lineEdit_7.setText(str(total_sale))
        self.lineEdit_4.setText(str(total_SGST))
        self.lineEdit_5.setText(str(total_CGST))
        self.lineEdit_9.setText(str(grand_sale))
        self.lineEdit_2.setText(str(profit))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form3()
    ui.setupUi3(Form)
    Form.show()
    sys.exit(app.exec_())

