# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(562, 428)
        MainWindow.setMinimumSize(QtCore.QSize(562, 428))
        MainWindow.setMaximumSize(QtCore.QSize(562, 428))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(6, -1, 541, 401))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lcdNumber = QtWidgets.QLCDNumber(self.tab)
        self.lcdNumber.setGeometry(QtCore.QRect(30, 10, 491, 81))
        self.lcdNumber.setSmallDecimalPoint(False)
        self.lcdNumber.setDigitCount(25)
        self.lcdNumber.setObjectName("lcdNumber")
        self.radioButton = QtWidgets.QRadioButton(self.tab)
        self.radioButton.setGeometry(QtCore.QRect(30, 130, 141, 16))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 130, 121, 16))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.tab)
        self.radioButton_3.setGeometry(QtCore.QRect(360, 130, 121, 16))
        self.radioButton_3.setObjectName("radioButton_3")
        self.frame = QtWidgets.QFrame(self.tab)
        self.frame.setGeometry(QtCore.QRect(70, 320, 461, 41))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setGeometry(QtCore.QRect(360, 10, 75, 21))
        self.pushButton_6.setObjectName("pushButton_6")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setGeometry(QtCore.QRect(50, 10, 62, 22))
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(0, 10, 41, 21))
        self.label_7.setObjectName("label_7")
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.frame)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(190, 10, 62, 21))
        self.doubleSpinBox_2.setMaximum(9999.99)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(140, 10, 41, 21))
        self.label_8.setObjectName("label_8")
        self.pushButton_7 = QtWidgets.QPushButton(self.frame)
        self.pushButton_7.setGeometry(QtCore.QRect(270, 10, 81, 21))
        self.pushButton_7.setObjectName("pushButton_7")
        self.frame_3 = QtWidgets.QFrame(self.tab)
        self.frame_3.setGeometry(QtCore.QRect(320, 310, 201, 51))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.frame_4 = QtWidgets.QFrame(self.tab)
        self.frame_4.setGeometry(QtCore.QRect(240, 310, 271, 51))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.pushButton_14 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_14.setGeometry(QtCore.QRect(190, 10, 75, 31))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 10, 131, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(10, 130, 181, 81))
        self.groupBox.setObjectName("groupBox")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setGeometry(QtCore.QRect(15, 21, 151, 41))
        self.textBrowser.setObjectName("textBrowser")
        self.frame_2 = QtWidgets.QFrame(self.tab_2)
        self.frame_2.setGeometry(QtCore.QRect(200, 10, 321, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 20))
        self.label.setObjectName("label")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(80, 8, 61, 22))
        self.spinBox.setMaximum(9999)
        self.spinBox.setSingleStep(1)
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(230, 7, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_8.setGeometry(QtCore.QRect(160, 7, 41, 23))
        self.pushButton_8.setObjectName("pushButton_8")
        self.frame_5 = QtWidgets.QFrame(self.tab_2)
        self.frame_5.setGeometry(QtCore.QRect(10, 9, 181, 111))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 54, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_5)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 54, 20))
        self.label_3.setObjectName("label_3")
        self.comboBox_2 = QtWidgets.QComboBox(self.frame_5)
        self.comboBox_2.setGeometry(QtCore.QRect(80, 38, 81, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_5)
        self.comboBox.setGeometry(QtCore.QRect(80, 8, 81, 22))
        self.comboBox.setObjectName("comboBox")
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_4.setGeometry(QtCore.QRect(90, 80, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(9, 219, 331, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 301, 111))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setGeometry(QtCore.QRect(200, 60, 321, 151))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.groupBox_3 = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(460, 290, 71, 71))
        self.groupBox_3.setObjectName("groupBox_3")
        self.dial = QtWidgets.QDial(self.groupBox_3)
        self.dial.setGeometry(QtCore.QRect(10, 10, 50, 64))
        self.dial.setMinimum(1)
        self.dial.setMaximum(5)
        self.dial.setPageStep(1)
        self.dial.setTracking(False)
        self.dial.setOrientation(QtCore.Qt.Horizontal)
        self.dial.setInvertedAppearance(False)
        self.dial.setInvertedControls(False)
        self.dial.setWrapping(False)
        self.dial.setNotchTarget(0.0)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GUI"))
        self.radioButton.setText(_translate("MainWindow", "GeneralWeighingMode"))
        self.radioButton_2.setText(_translate("MainWindow", "CountingMode"))
        self.radioButton_3.setText(_translate("MainWindow", "Pass/FailMode"))
        self.pushButton_6.setText(_translate("MainWindow", "Tare"))
        self.label_7.setText(_translate("MainWindow", "MAX???"))
        self.label_8.setText(_translate("MainWindow", "MIN???"))
        self.pushButton_7.setText(_translate("MainWindow", "SetThreshold"))
        self.pushButton_2.setText(_translate("MainWindow", "Tare"))
        self.pushButton_14.setText(_translate("MainWindow", "Tare"))
        self.pushButton_5.setText(_translate("MainWindow", "SetReferenceWeight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "DataCollector "))
        self.label.setText(_translate("MainWindow", "Standard???"))
        self.pushButton.setText(_translate("MainWindow", "calibrate"))
        self.pushButton_8.setText(_translate("MainWindow", "Count"))
        self.label_2.setText(_translate("MainWindow", "Serialport???"))
        self.label_3.setText(_translate("MainWindow", "Baudrate???"))
        self.pushButton_4.setText(_translate("MainWindow", "open"))
        self.groupBox_2.setTitle(_translate("MainWindow", "WorkFlow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Weight"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "ADC"))
        self.groupBox_3.setTitle(_translate("MainWindow", "BackLight"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "DeBug"))
