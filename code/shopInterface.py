# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\PharmaProject\Ebay.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1323, 867)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1321, 811))
        self.tabWidget.setStyleSheet(_fromUtf8("background-color: black;"))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 321, 231))
        self.groupBox.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font:bold;\n"
"color:white;\n"
"font: 9pt \"Impact\";\n"
""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.webFetch = QtGui.QComboBox(self.groupBox)
        self.webFetch.setGeometry(QtCore.QRect(10, 40, 211, 22))
        self.webFetch.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.webFetch.setObjectName(_fromUtf8("webFetch"))
        self.webFetch.addItem(_fromUtf8(""))
        self.webFetch.addItem(_fromUtf8(""))
        self.webFetch.addItem(_fromUtf8(""))
        self.webFetch.addItem(_fromUtf8(""))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 90, 53, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.P1 = QtGui.QComboBox(self.groupBox)
        self.P1.setGeometry(QtCore.QRect(60, 90, 61, 22))
        self.P1.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.P1.setObjectName(_fromUtf8("P1"))
        self.P2 = QtGui.QComboBox(self.groupBox)
        self.P2.setGeometry(QtCore.QRect(160, 90, 61, 22))
        self.P2.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.P2.setObjectName(_fromUtf8("P2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(130, 90, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 150, 53, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Rating = QtGui.QRadioButton(self.groupBox)
        self.Rating.setGeometry(QtCore.QRect(70, 150, 71, 20))
        self.Rating.setObjectName(_fromUtf8("Rating"))
        self.Price = QtGui.QRadioButton(self.groupBox)
        self.Price.setGeometry(QtCore.QRect(160, 150, 61, 20))
        self.Price.setObjectName(_fromUtf8("Price"))
        self.Scrap = QtGui.QPushButton(self.groupBox)
        self.Scrap.setGeometry(QtCore.QRect(10, 190, 291, 28))
        self.Scrap.setStyleSheet(_fromUtf8("background:black;"))
        self.Scrap.setObjectName(_fromUtf8("Scrap"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 20, 321, 231))
        self.groupBox_2.setStyleSheet(_fromUtf8("font:bold;\n"
"color:white;\n"
"font: 9pt \"Impact\";\n"
"background:rgb(152, 0, 0);\n"
""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 53, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.From = QtGui.QComboBox(self.groupBox_2)
        self.From.setGeometry(QtCore.QRect(80, 40, 201, 22))
        self.From.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.From.setObjectName(_fromUtf8("From"))
        self.From.addItem(_fromUtf8(""))
        self.From.addItem(_fromUtf8(""))
        self.From.addItem(_fromUtf8(""))
        self.From.addItem(_fromUtf8(""))
        self.From.addItem(_fromUtf8(""))
        self.From.addItem(_fromUtf8(""))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(20, 90, 53, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.Number = QtGui.QComboBox(self.groupBox_2)
        self.Number.setGeometry(QtCore.QRect(80, 90, 201, 22))
        self.Number.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.Number.setObjectName(_fromUtf8("Number"))
        self.Number.addItem(_fromUtf8(""))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 190, 301, 28))
        self.pushButton_2.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.mainTable = QtGui.QTableWidget(self.tab)
        self.mainTable.setGeometry(QtCore.QRect(30, 280, 1261, 491))
        self.mainTable.setStyleSheet(_fromUtf8("background:red;\n"
"font:bold;\n"
"background:rgb(152, 0, 0);\n"
""))
        self.mainTable.setObjectName(_fromUtf8("mainTable"))
        self.mainTable.setColumnCount(9)
        self.mainTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.mainTable.setHorizontalHeaderItem(8, item)
        self.mainTable.horizontalHeader().setCascadingSectionResizes(False)
        self.mainTable.horizontalHeader().setSortIndicatorShown(False)
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(968, 20, 321, 231))
        self.groupBox_3.setStyleSheet(_fromUtf8("background:red;\n"
"font:bold;\n"
"color:white;\n"
"background:rgb(152, 0, 0);\n"
""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Export = QtGui.QPushButton(self.groupBox_3)
        self.Export.setGeometry(QtCore.QRect(10, 190, 291, 28))
        self.Export.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;"))
        self.Export.setObjectName(_fromUtf8("Export"))
        self.Export1 = QtGui.QRadioButton(self.groupBox_3)
        self.Export1.setGeometry(QtCore.QRect(20, 30, 95, 20))
        self.Export1.setObjectName(_fromUtf8("Export1"))
        self.Export2 = QtGui.QRadioButton(self.groupBox_3)
        self.Export2.setGeometry(QtCore.QRect(20, 80, 161, 20))
        self.Export2.setObjectName(_fromUtf8("Export2"))
        self.ExportFrom = QtGui.QComboBox(self.groupBox_3)
        self.ExportFrom.setGeometry(QtCore.QRect(90, 120, 101, 22))
        self.ExportFrom.setStyleSheet(_fromUtf8("background:black;\n"
"color:white;\n"
""))
        self.ExportFrom.setObjectName(_fromUtf8("ExportFrom"))
        self.ExportFrom.addItem(_fromUtf8(""))
        self.ExportFrom.addItem(_fromUtf8(""))
        self.ExportFrom.addItem(_fromUtf8(""))
        self.ExportFrom.addItem(_fromUtf8(""))
        self.ExportFrom.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 41, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.textConvert = QtGui.QTextEdit(self.tab_2)
        self.textConvert.setGeometry(QtCore.QRect(210, 50, 851, 581))
        self.textConvert.setStyleSheet(_fromUtf8("background:red;\n"
"font:bold;\n"
"background:rgb(152, 0, 0);\n"
"color:white;\n"
""))
        self.textConvert.setObjectName(_fromUtf8("textConvert"))
        self.convert = QtGui.QPushButton(self.tab_2)
        self.convert.setGeometry(QtCore.QRect(530, 660, 291, 28))
        self.convert.setStyleSheet(_fromUtf8("background:red;\n"
"font:bold;\n"
"background:rgb(152, 0, 0);\n"
"color:white;"))
        self.convert.setObjectName(_fromUtf8("convert"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 30, 401, 721))
        self.groupBox_4.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font:bold;\n"
"color:white;\n"
"font: 9pt \"Impact\";\n"
""))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(450, 30, 401, 721))
        self.groupBox_6.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font:bold;\n"
"color:white;\n"
"font: 9pt \"Impact\";\n"
""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(880, 30, 401, 721))
        self.groupBox_5.setStyleSheet(_fromUtf8("background:rgb(152, 0, 0);\n"
"font:bold;\n"
"color:white;\n"
"font: 9pt \"Impact\";\n"
""))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1323, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "Website", None))
        self.webFetch.setItemText(0, _translate("MainWindow", "Kinguin", None))
        self.webFetch.setItemText(1, _translate("MainWindow", "Allkeyshop", None))
        self.webFetch.setItemText(2, _translate("MainWindow", "G2a", None))
        self.webFetch.setItemText(3, _translate("MainWindow", "CdKeys", None))
        self.label.setText(_translate("MainWindow", "Pages", None))
        self.label_2.setText(_translate("MainWindow", "To", None))
        self.label_3.setText(_translate("MainWindow", "Sort by", None))
        self.Rating.setText(_translate("MainWindow", "Rating", None))
        self.Price.setText(_translate("MainWindow", "Price", None))
        self.Scrap.setText(_translate("MainWindow", "Scrap", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Update Prices", None))
        self.label_4.setText(_translate("MainWindow", "From : ", None))
        self.From.setItemText(0, _translate("MainWindow", "Their own website", None))
        self.From.setItemText(1, _translate("MainWindow", "Kinguin", None))
        self.From.setItemText(2, _translate("MainWindow", "Allkeyshop", None))
        self.From.setItemText(3, _translate("MainWindow", "G2a", None))
        self.From.setItemText(4, _translate("MainWindow", "Cdkeys", None))
        self.From.setItemText(5, _translate("MainWindow", "Compare them all ( slow ) ", None))
        self.label_5.setText(_translate("MainWindow", "Number :", None))
        self.Number.setItemText(0, _translate("MainWindow", "All of them", None))
        self.pushButton_2.setText(_translate("MainWindow", "Update", None))
        item = self.mainTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Id", None))
        item = self.mainTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Name", None))
        item = self.mainTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Old price", None))
        item = self.mainTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "New price", None))
        item = self.mainTable.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Date", None))
        item = self.mainTable.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Images", None))
        item = self.mainTable.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Url", None))
        item = self.mainTable.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Page", None))
        item = self.mainTable.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Statut", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Export to csv", None))
        self.Export.setText(_translate("MainWindow", "Export", None))
        self.Export1.setText(_translate("MainWindow", "All products", None))
        self.Export2.setText(_translate("MainWindow", "Not exported products", None))
        self.ExportFrom.setItemText(0, _translate("MainWindow", "All", None))
        self.ExportFrom.setItemText(1, _translate("MainWindow", "Kinguin", None))
        self.ExportFrom.setItemText(2, _translate("MainWindow", "Allkeyshop", None))
        self.ExportFrom.setItemText(3, _translate("MainWindow", "G2a", None))
        self.ExportFrom.setItemText(4, _translate("MainWindow", "CdKeys", None))
        self.label_6.setText(_translate("MainWindow", "From : ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Scrap", None))
        self.convert.setText(_translate("MainWindow", "Convert", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Ebay push", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Youtube", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Fb", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Instagram", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Advertise", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

