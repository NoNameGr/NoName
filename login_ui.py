from PyQt5 import QtCore, QtGui, QtWidgets


class Version(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Version")
        Frame.resize(452, 296)

        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(110, 100, 91, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(340, 60, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(100, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 101, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(240, 150, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_3.setText(_translate("Frame", "Phiên bản"))
        self.label_2.setText(_translate("Frame", "by NoName"))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.pushButton.setText(_translate("Frame", "Tiếng Việt"))
        self.pushButton.clicked.connect(self.on_pushButton)
        self.dialog = Level()
        self.pushButton_2.setText(_translate("Frame", "English"))
        self.pushButton_2.clicked.connect(self.on_pushButton_2)
        self.dialog_1 = LevelEng()


    def on_pushButton(self):
        Dialog.hide()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        dialog = QtWidgets.QDialog()
        self.dialog.ui = Level()
        self.dialog.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()

    def on_pushButton_2(self):
        Dialog.hide()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        dialog_1 = QtWidgets.QDialog()
        self.dialog_1.ui = LevelEng()
        self.dialog_1.setupUi(dialog_1)
        dialog_1.show()
        dialog_1.exec_()


class Level(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Level")
        Frame.resize(452,296)

        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(50, 30, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(290, 70, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(200, 100, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 150, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 200, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Mức độ chơi "))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.label_2.setText(_translate("Frame", "by NoName"))
        self.pushButton.setText(_translate("Frame", "Dễ"))
        self.pushButton.clicked.connect(self.on_pushButton_1)
        self.dialog = De()
        self.pushButton_2.setText(_translate("Frame", "Trung Bình"))
        self.pushButton_2.clicked.connect(self.on_pushButton_2)
        self.dialog_2 = TrungBinh()
        self.pushButton_3.setText(_translate("Frame", "Khó"))
        self.pushButton_3.clicked.connect(self.on_pushButton_3)
        self.dialog_3 = Kho()

    def on_pushButton_1(self):
        Dialog.hide()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        dialog = QtWidgets.QDialog()
        self.dialog.ui = De()
        self.dialog.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()

    def on_pushButton_2(self):
        Dialog.hide()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        dialog_2 = QtWidgets.QDialog()
        self.dialog_2.ui = TrungBinh()
        self.dialog_2.setupUi(dialog_2)
        dialog_2.show()
        dialog_2.exec_()

    def on_pushButton_3(self):
        Dialog.hide()
        import sys
        app = QtWidgets.QApplication(sys.argv)
        dialog_3 = QtWidgets.QDialog()
        self.dialog_3.ui = Kho()
        self.dialog_3.setupUi(dialog_3)
        dialog_3.show()
        dialog_3.exec_()


class chucmung(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Chuc Mung")

        Frame.resize(452, 296)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 90, 121, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Chúc mừng !"))


class De(object):
    def setupUi(self, Frame):
        Frame.setObjectName("De")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = chucmung()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == 'canbang':
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = chucmung()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Xin hay nhap lai dap an cua ban khong dau va khong co khoang trong! ')
            ann.exec_()


class TrungBinh(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Trung Binh")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = chucmung()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == 'noname' :
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = chucmung()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Nhpa lai ket qua cua ban. Hay chac chan ban khong nhap co dau va co khoang ')
            ann.exec_()



class Kho(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Kho")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = chucmung()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == 'noname':
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = chucmung()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Nhpa lai ket qua cua ban. Hay chac chan ban khong nhap co dau va co khoang trong')
            ann.exec_()


class LevelEng(object):
    def setupUi(self, Frame):
        Frame.setObjectName("levelEng")
        Frame.resize(452, 296)
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(90, 100, 51, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(40, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(280, 60, 81, 31))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(210, 90, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Frame)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 130, 131, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 170, 131, 41))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Level"))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.label_2.setText(_translate("Frame", "by NoName"))
        self.pushButton.setText(_translate("Frame", "Easy"))
        self.pushButton.clicked.connect(self.on_pushButton_1)
        self.dialog = Easy()
        self.pushButton_2.setText(_translate("Frame", "Medium"))
        self.pushButton_2.clicked.connect(self.on_pushButton_2)
        self.dialog_2 = Medium()
        self.pushButton_3.setText(_translate("Frame", "Hard"))
        self.pushButton_3.clicked.connect(self.on_pushButton_3)
        self.dialog_3 = Hard()

    def on_pushButton_1(self):
        Dialog.hide()
        import sys
        dialog = QtWidgets.QDialog()
        self.dialog.ui = Easy()
        self.dialog.ui.setupUi(dialog)
        dialog.show()
        dialog.exec_()


    def on_pushButton_2(self):
        Dialog.hide()
        import sys
        dialog_2 = QtWidgets.QDialog()
        self.dialog_2.ui = Medium()
        self.dialog_2.ui.setupUi(dialog_2)
        dialog_2.show()
        dialog_2.exec_()

    def on_pushButton_3(self):
        Dialog.hide()
        import sys
        dialog_3 = QtWidgets.QDialog()
        self.dialog_3.ui = Hard()
        self.dialog_3.ui.setupUi(dialog_3)
        dialog_3.show()
        dialog_3.exec_()


class congratulation(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(452, 296)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(130, 90, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Congratulations !"))


class Easy(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = congratulation()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == '@@@':
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = congratulation()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Please enter your answer again. Please write without space ')
            ann.exec_()


class Medium(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = congratulation()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == '@@@':
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = congratulation()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Please enter your answer again. Please write without space ')
            ann.exec_()


class Hard(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(452, 296)
        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(240, 100, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = congratulation()

    def on_pushButton_clicked(self):
        if self.textEdit.text() == '@@@':
            Dialog.hide()
            import sys
            dialog = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = congratulation()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Please enter your answer again. Please write without space ')
            ann.exec_()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(450, 520)
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
        self.textEdit = QtWidgets.QLineEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(120, 110, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QLineEdit(Dialog)
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
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Version()
        self.commandLinkButton_2.setText(_translate("Dialog", "Google"))
        self.commandLinkButton_3.setText(_translate("Dialog", "Twitter"))
        self.commandLinkButton.setText(_translate("Dialog", "Facebook"))
        self.label_4.setText(_translate("Dialog", "Bạn chưa có tài khoản đăng nhập ? "))
        self.pushButton_2.setText(_translate("Dialog", "Create free account "))

    def on_pushButton_clicked(self):
        if self.textEdit.text() == 'noname' and self.textEdit_2.text() == 'noname':
            Dialog.hide()
            import sys
            app = QtWidgets.QApplication(sys.argv)
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Version()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            ann = QtWidgets.QMessageBox(Dialog)
            ann.setText('Incorrect Username or Password. Please try again!')
            ann.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())