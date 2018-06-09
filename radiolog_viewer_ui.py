# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radiolog_viewer.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_radiolog_viewer(object):
    def setupUi(self, radiolog_viewer):
        radiolog_viewer.setObjectName("radiolog_viewer")
        radiolog_viewer.resize(899, 561)
        self.logField = QtWidgets.QTextEdit(radiolog_viewer)
        self.logField.setGeometry(QtCore.QRect(187, 238, 525, 199))
        self.logField.setObjectName("logField")
        self.rescanButton = QtWidgets.QPushButton(radiolog_viewer)
        self.rescanButton.setGeometry(QtCore.QRect(302, 35, 93, 28))
        self.rescanButton.setObjectName("rescanButton")
        self.watchedDirField = QtWidgets.QLineEdit(radiolog_viewer)
        self.watchedDirField.setGeometry(QtCore.QRect(189, 85, 290, 22))
        self.watchedDirField.setObjectName("watchedDirField")
        self.watchedFileField = QtWidgets.QLineEdit(radiolog_viewer)
        self.watchedFileField.setGeometry(QtCore.QRect(190, 123, 290, 22))
        self.watchedFileField.setObjectName("watchedFileField")
        self.label = QtWidgets.QLabel(radiolog_viewer)
        self.label.setGeometry(QtCore.QRect(87, 87, 80, 20))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(radiolog_viewer)
        self.label_2.setGeometry(QtCore.QRect(88, 120, 80, 20))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(radiolog_viewer)
        self.rescanButton.clicked.connect(radiolog_viewer.rescan)
        QtCore.QMetaObject.connectSlotsByName(radiolog_viewer)

    def retranslateUi(self, radiolog_viewer):
        _translate = QtCore.QCoreApplication.translate
        radiolog_viewer.setWindowTitle(_translate("radiolog_viewer", "Dialog"))
        self.rescanButton.setText(_translate("radiolog_viewer", "Re-scan"))
        self.label.setText(_translate("radiolog_viewer", "Watched Dir"))
        self.label_2.setText(_translate("radiolog_viewer", "Watched File"))

