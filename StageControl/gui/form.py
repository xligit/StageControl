# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1045, 748)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_2)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label_2)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setMinimumWidth(600)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        
        self.scrollArea = QtWidgets.QTextBrowser(self.centralwidget)
        self.scrollArea.setObjectName("scrollArea")
        

        self.scrollArea.setTextBackgroundColor(QtGui.QColor(5,5,5))
        self.scrollArea.setTextColor(QtGui.QColor(0, 255, 0))
        self.scrollArea.setStyleSheet("background-color: black;")
        self.scrollArea.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignBottom)
        self.scrollArea.insertPlainText("0gi\n")
        self.scrollArea.insertPlainText("0PO12931223\n")


        self.verticalLayout.addWidget(self.scrollArea)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1045, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.centralwidget)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("self.centralwidget", "self.centralwidget"))
        self.comboBox.setItemText(0, _translate("self.centralwidget", "510 nm"))
        self.comboBox.setItemText(1, _translate("self.centralwidget", "405 nm"))
        self.comboBox.setItemText(2, _translate("self.centralwidget", "365 nm"))
        self.comboBox.setItemText(3, _translate("self.centralwidget", "280 nm"))
        self.pushButton_2.setText(_translate("self.centralwidget", "Set Position"))
        what = "Set by λ"
        self.pushButton.setText(_translate("self.centralwidget", what))
        self.label.setText(_translate("self.centralwidget", "Position:"))
        self.label_2.setText(_translate("self.centralwidget", "0.00 mm"))
        self.pushButton_3.setText(_translate("Widget", "Insert"))