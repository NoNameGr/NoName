from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 110, 256, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 150, 256, 31))
        self.lineEdit_2.setObjectName("LineEdit_2")
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
        if self.lineEdit.text() == 'noname' and self.lineEdit_2.text() == 'noname':
            Dialog.hide()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Version()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else:
            msg = QtWidgets.QMessageBox(Dialog)
            msg.setText('abc')
            msg.exec_()


class Version(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(452, 296)

        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 180, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(30, 100, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(340, 60, 81, 31))
        self.label_2.setObjectName("label_2")

        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(210, 150, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(100, 20, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(31)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(210, 120, 100, 20))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))

        self.pushButton.setText(_translate("Frame", "Next"))
        self.pushButton.clicked.connect(lambda: self.on_pushButton_clicked(Frame))

        self.label_3.setText(_translate("Frame", "Phiên bản / Version"))
        self.label_2.setText(_translate("Frame", "by NoName"))

        self.radioButton_2.setText(_translate("Frame", "English"))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.radioButton.setText(_translate("Frame", "Tiếng Việt"))

    def on_pushButton_clicked(self, Frame):
        if self.radioButton.isChecked():
            Frame.hide()
            self.dialog = Level()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Level()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        if self.radioButton_2.isChecked():
            Frame.hide()
            self.dialog = LevelEng()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = LevelEng()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()


class Level(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)

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
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(190, 110, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 150, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Frame)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 190, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Mức độ chơi "))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.label_2.setText(_translate("Frame", "by NoName"))
        self.radioButton.setText(_translate("Frame", "Dễ"))
        self.radioButton_2.setText(_translate("Frame", "Trung Bình"))
        self.radioButton_3.setText(_translate("Frame", "Khó"))
        self.pushButton.setText(_translate("Frame", "Tiếp tục"))
        self.pushButton.clicked.connect(lambda: self.on_pushButton_clicked(Frame))

    def on_pushButton_clicked(self, Frame):
        if self.radioButton.isChecked() :
            Frame.hide()
            self.dialog = De()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = De()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        if self.radioButton_2.isChecked() :
            Frame.hide()
            self.dialog = TrungBinh()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = TrungBinh()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        if self.radioButton_3.isChecked():
            Frame.hide()
            self.dialog = Kho()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Kho()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()


class De(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(462, 403)

        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(320, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(-430, 80, 931, 401))
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap("../../Downloads/Easy 2/116585517_595969061089144_7152213483962716199_n.png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(40, 40, 271, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))
        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = De1()

    def on_pushButton_clicked(self, Frame):
        if self.lineEdit.text() == 'alo':
            Frame.hide()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = De1()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        else :
            agg = QtWidgets.QMessageBox(Frame)
            agg.setText('Alo alo')
            agg.exec_()

class De1(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(462, 403)
        Frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        Frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(130, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(-240, 90, 711, 451))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/Easy 2/116876374_1802275236592370_1047754930775541732_n.png"))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Frame)
        self.lineEdit.setGeometry(QtCore.QRect(10, 40, 311, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))


class TrungBinh(object):
    def setupUi(self, Frame):
        Frame.setObjectName("TrungBinh")
        Frame.resize(483, 469)

        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 40, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(120, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 40, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(-330, 80, 881, 391))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/Medium 2/116879570_391505055159934_1546795416759554758_n.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))

class Kho(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Kho")
        Frame.resize(497, 440)

        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(50, 40, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(320, 30, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(-190, 80, 701, 391))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/Hard 2/116878144_849065205618343_7101748322150918133_n.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Hãy nhập đáp án của bạn"))
        self.pushButton.setText(_translate("Frame", "Kiểm tra"))

class LevelEng(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 300)

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
        self.radioButton = QtWidgets.QRadioButton(Frame)
        self.radioButton.setGeometry(QtCore.QRect(190, 100, 100, 20))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Frame)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 140, 100, 20))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Frame)
        self.radioButton_3.setGeometry(QtCore.QRect(190, 180, 100, 20))
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(260, 230, 113, 32))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label_4.setText(_translate("Frame", "Level"))
        self.label.setText(_translate("Frame", "Đuổi hình bắt chữ"))
        self.label_2.setText(_translate("Frame", "by NoName"))
        self.radioButton.setText(_translate("Frame", "Easy"))
        self.radioButton_2.setText(_translate("Frame", "Medium"))
        self.radioButton_3.setText(_translate("Frame", "Hard"))
        self.pushButton.setText(_translate("Frame", "Next"))
        self.pushButton.clicked.connect(lambda:self.on_pushButton_clicked(Frame))

    def on_pushButton_clicked(self, Frame):
        if self.radioButton.isChecked():
            Frame.hide()
            self.dialog = Easy()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Easy()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        if self.radioButton_2.isChecked():
            Frame.hide()
            self.dialog = Medium()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Medium()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()
        if self.radioButton_3.isChecked():
            Frame.hide()
            self.dialog = Hard()
            dialog = QtWidgets.QDialog()
            self.dialog.ui = Hard()
            self.dialog.ui.setupUi(dialog)
            dialog.show()
            dialog.exec_()


class Easy(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(510, 309)

        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(70, 50, 411, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(150, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 90, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(100, 130, 321, 151))
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap("../../Downloads/Easy/116341300_897281977430895_4028080577005173643_n.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))


class Medium(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 281)

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
        self.pushButton.setGeometry(QtCore.QRect(240, 90, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(60, 110, 281, 161))
        self.label_2.setText("")
        self.label_2.setPixmap(
            QtGui.QPixmap("../../Downloads/Medium/117036784_3207827889304561_8314431154431398287_n.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))


class Hard(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(400, 299)
        Frame.setBaseSize(QtCore.QSize(452, 296))

        self.textEdit = QtWidgets.QTextEdit(Frame)
        self.textEdit.setGeometry(QtCore.QRect(20, 230, 256, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(90, 10, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Frame)
        self.pushButton.setGeometry(QtCore.QRect(280, 230, 113, 32))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(120, 40, 151, 181))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../Downloads/116388362_294147695201732_4050924223029574126_n.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "Please enter your answer "))
        self.pushButton.setText(_translate("Frame", "Check"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
