# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(836, 596)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 111, 31))
        self.label.setObjectName("label")
        self.picture_label = QtWidgets.QLabel(self.centralwidget)
        self.picture_label.setGeometry(QtCore.QRect(10, 60, 400, 500))
        self.picture_label.setObjectName("picture_label")
        self.capture_btn = QtWidgets.QPushButton(self.centralwidget)
        self.capture_btn.setGeometry(QtCore.QRect(120, 20, 93, 28))
        self.capture_btn.setStyleSheet("border: 0;\n"
"background:#fff;\n"
"border-radius:10px;")
        self.capture_btn.setObjectName("capture_btn")
        self.text_edit = QtWidgets.QTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(420, 60, 400, 500))
        self.text_edit.setReadOnly(True)
        self.text_edit.setObjectName("text_edit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(420, 30, 72, 15))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 836, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.capture_btn.clicked.connect(MainWindow.capture_btn_clicked)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "furry-Toolkit"))
        self.label.setText(_translate("MainWindow", "??????"))
        self.picture_label.setText(_translate("MainWindow", "TextLabel"))
        self.capture_btn.setText(_translate("MainWindow", "??????"))
        self.label_3.setText(_translate("MainWindow", "??????"))
import res.testRes_rc
