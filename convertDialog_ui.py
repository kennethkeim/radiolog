# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'convertDialog.ui'
#
# Created: Thu Apr  9 19:40:38 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_convertDialog(object):
    def setupUi(self, convertDialog):
        convertDialog.setObjectName("convertDialog")
        convertDialog.setEnabled(True)
        convertDialog.resize(582, 322)
        self.convertedCoordsField = QtWidgets.QLineEdit(convertDialog)
        self.convertedCoordsField.setEnabled(True)
        self.convertedCoordsField.setGeometry(QtCore.QRect(40, 260, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(18)
        self.convertedCoordsField.setFont(font)
        self.convertedCoordsField.setFocusPolicy(QtCore.Qt.NoFocus)
        self.convertedCoordsField.setReadOnly(True)
        self.convertedCoordsField.setClearButtonEnabled(False)
        self.convertedCoordsField.setObjectName("convertedCoordsField")
        self.groupBox_2 = QtWidgets.QGroupBox(convertDialog)
        self.groupBox_2.setEnabled(True)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 40, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.origDatumFormatLabel = QtWidgets.QLabel(self.groupBox_2)
        self.origDatumFormatLabel.setEnabled(False)
        self.origDatumFormatLabel.setGeometry(QtCore.QRect(260, 70, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.origDatumFormatLabel.setFont(font)
        self.origDatumFormatLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.origDatumFormatLabel.setObjectName("origDatumFormatLabel")
        self.origCoordsField = QtWidgets.QLineEdit(self.groupBox_2)
        self.origCoordsField.setEnabled(False)
        self.origCoordsField.setGeometry(QtCore.QRect(260, 40, 271, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.origCoordsField.setFont(font)
        self.origCoordsField.setObjectName("origCoordsField")
        self.useCoordsInMessageButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.useCoordsInMessageButton.setGeometry(QtCore.QRect(20, 30, 241, 31))
        self.useCoordsInMessageButton.setObjectName("useCoordsInMessageButton")
        self.buttonGroup = QtWidgets.QButtonGroup(convertDialog)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.useCoordsInMessageButton)
        self.line = QtWidgets.QFrame(self.groupBox_2)
        self.line.setGeometry(QtCore.QRect(250, 30, 3, 61))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.useRadioLocButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.useRadioLocButton.setGeometry(QtCore.QRect(20, 60, 201, 31))
        self.useRadioLocButton.setObjectName("useRadioLocButton")
        self.buttonGroup.addButton(self.useRadioLocButton)
        self.groupBox = QtWidgets.QGroupBox(convertDialog)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 150, 541, 101))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.datumComboBox = QtWidgets.QComboBox(self.groupBox)
        self.datumComboBox.setGeometry(QtCore.QRect(20, 40, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.datumComboBox.setFont(font)
        self.datumComboBox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.datumComboBox.setObjectName("datumComboBox")
        self.datumComboBox.addItem("")
        self.datumComboBox.addItem("")
        self.formatComboBox = QtWidgets.QComboBox(self.groupBox)
        self.formatComboBox.setGeometry(QtCore.QRect(250, 40, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        self.formatComboBox.setFont(font)
        self.formatComboBox.setObjectName("formatComboBox")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.formatComboBox.addItem("")
        self.goButton = QtWidgets.QPushButton(self.groupBox)
        self.goButton.setGeometry(QtCore.QRect(430, 40, 91, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.goButton.setFont(font)
        self.goButton.setObjectName("goButton")
        self.msgField = QtWidgets.QLineEdit(convertDialog)
        self.msgField.setEnabled(False)
        self.msgField.setGeometry(QtCore.QRect(40, 10, 501, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        self.msgField.setFont(font)
        self.msgField.setFrame(False)
        self.msgField.setReadOnly(False)
        self.msgField.setPlaceholderText("")
        self.msgField.setClearButtonEnabled(False)
        self.msgField.setObjectName("msgField")

        self.retranslateUi(convertDialog)
        QtCore.QMetaObject.connectSlotsByName(convertDialog)

    def retranslateUi(self, convertDialog):
        _translate = QtCore.QCoreApplication.translate
        convertDialog.setWindowTitle(_translate("convertDialog", "Convert Coordinates"))
        self.groupBox_2.setTitle(_translate("convertDialog", "Original"))
        self.origDatumFormatLabel.setText(_translate("convertDialog", "DATUM / FORMAT"))
        self.useCoordsInMessageButton.setText(_translate("convertDialog", "Use Coords in Message"))
        self.useRadioLocButton.setText(_translate("convertDialog", "Use Radio Location"))
        self.groupBox.setTitle(_translate("convertDialog", "Convert To"))
        self.datumComboBox.setItemText(0, _translate("convertDialog", "NAD27 CONUS"))
        self.datumComboBox.setItemText(1, _translate("convertDialog", "WGS84"))
        self.formatComboBox.setItemText(0, _translate("convertDialog", "UTM"))
        self.formatComboBox.setItemText(1, _translate("convertDialog", "D.dº"))
        self.formatComboBox.setItemText(2, _translate("convertDialog", "Dº M.m\'"))
        self.formatComboBox.setItemText(3, _translate("convertDialog", "Dº M\' S.s\""))
        self.goButton.setText(_translate("convertDialog", "Go"))
        self.msgField.setText(_translate("convertDialog", "TIME/TF/TEAM : MSG"))

