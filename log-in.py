# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log-in.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 427)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 110, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 150, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 110, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(120, 150, 256, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(120, 30, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(250, 200, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.commandLinkButton_2 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_2.setGeometry(QtCore.QRect(150, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.commandLinkButton_2.setFont(font)
        self.commandLinkButton_2.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_2.setCheckable(False)
        self.commandLinkButton_2.setDescription("")
        self.commandLinkButton_2.setObjectName("commandLinkButton_2")
        self.commandLinkButton_3 = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton_3.setGeometry(QtCore.QRect(280, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.commandLinkButton_3.setFont(font)
        self.commandLinkButton_3.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton_3.setCheckable(False)
        self.commandLinkButton_3.setDescription("")
        self.commandLinkButton_3.setObjectName("commandLinkButton_3")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(Dialog)
        self.commandLinkButton.setGeometry(QtCore.QRect(10, 310, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.commandLinkButton.setFont(font)
        self.commandLinkButton.setIconSize(QtCore.QSize(25, 25))
        self.commandLinkButton.setCheckable(False)
        self.commandLinkButton.setDescription("")
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(100, 250, 221, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 270, 151, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "User          : "))
        self.label_2.setText(_translate("Dialog", "Password : "))
        self.label_3.setText(_translate("Dialog", "Đuổi hình bắt chữ "))
        self.pushButton.setText(_translate("Dialog", "Log in"))
        self.commandLinkButton_2.setText(_translate("Dialog", "Google"))
        self.commandLinkButton_3.setText(_translate("Dialog", "Twitter"))
        self.commandLinkButton.setText(_translate("Dialog", "Facebook"))
        self.label_4.setText(_translate("Dialog", "Bạn chưa có tài khoản đăng nhập ? "))
        self.pushButton_2.setText(_translate("Dialog", "Create free account "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
