# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'report.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form_Report(object):
    def setupUi_Report(self, Form):
        Form.setObjectName("Form")
        Form.resize(752, 591)
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 10, 731, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
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
        self.gridLayout.addWidget(self.tableWidget, 1, 0, 1, 2)

        self.retranslateUi_Report(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi_Report(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Availablity"))
        self.pushButton_2.setText(_translate("Form", "download"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "product_name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "product_model_number"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "product_hsn_code"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "product_imei_number"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "product_price"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "vendor"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "stock_in_date"))

        self.pushButton.clicked.connect(self.available_stock)

    def available_stock(self):
        conn = sqlite3.connect('mymobileshoppy.db')
        c = conn.cursor()
        query = "select * from available"
        result = c.execute(query)
        # print(enumerate(result))
        self.tableWidget.setRowCount(0)  # clear table
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for colomn_number, data in enumerate(row_data):
                self.tableWidget.setItem(row_number, colomn_number, QtWidgets.QTableWidgetItem(str(data)))

        conn.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form_Report()
    ui.setupUi_Report(Form)
    Form.show()
    sys.exit(app.exec_())

