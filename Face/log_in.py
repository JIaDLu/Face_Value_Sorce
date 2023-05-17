# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(875, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Face-server/logo.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("*{font: 12pt \"楷体\";}\n"
"QPushButton{\n"
"    background-color:#FF455E;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_bg = QtWidgets.QFrame(self.centralwidget)
        self.frame_bg.setGeometry(QtCore.QRect(60, 80, 751, 451))
        self.frame_bg.setStyleSheet("#frame_bg{\n"
"    border-image: url(:/bg/bg1.png);\n"
"background-color: rgb(243, 244, 248);\n"
"border-radius:30px;}")
        self.frame_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bg.setObjectName("frame_bg")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_bg)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.frame_bg)
        self.frame_2.setMinimumSize(QtCore.QSize(350, 370))
        self.frame_2.setMaximumSize(QtCore.QSize(350, 370))
        self.frame_2.setStyleSheet("border-image: url(:/bg/bg.png);\n"
" border-radius:30px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(self.frame_bg)
        self.frame.setMinimumSize(QtCore.QSize(390, 370))
        self.frame.setMaximumSize(QtCore.QSize(390, 370))
        self.frame.setStyleSheet("#frame{\n"
"    background-color: rgba(0, 0, 0,0);\n"
"     border-radius:30px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.pushButtonCancel = QtWidgets.QPushButton(self.frame)
        self.pushButtonCancel.setStyleSheet("background-color: rgba(0,0, 0, 0);")
        self.pushButtonCancel.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bg/关闭.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonCancel.setIcon(icon1)
        self.pushButtonCancel.setIconSize(QtCore.QSize(20, 20))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_6.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setStyleSheet("color:rgb(170, 85, 0);\n"
"font:  16pt \"Cascadia Code SemiBold\";")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.sr_zh = QtWidgets.QLineEdit(self.frame)
        self.sr_zh.setMinimumSize(QtCore.QSize(200, 30))
        self.sr_zh.setStyleSheet("")
        self.sr_zh.setObjectName("sr_zh")
        self.horizontalLayout.addWidget(self.sr_zh)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.sr_mm = QtWidgets.QLineEdit(self.frame)
        self.sr_mm.setMinimumSize(QtCore.QSize(200, 30))
        self.sr_mm.setStyleSheet("")
        self.sr_mm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.sr_mm.setObjectName("sr_mm")
        self.horizontalLayout_2.addWidget(self.sr_mm)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem8)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setMinimumSize(QtCore.QSize(200, 30))
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem10)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem11)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.pushButton_register = QtWidgets.QPushButton(self.frame)
        self.pushButton_register.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButton_register.setObjectName("pushButton_register")
        self.horizontalLayout_4.addWidget(self.pushButton_register)
        self.pushButtonOK = QtWidgets.QPushButton(self.frame)
        self.pushButtonOK.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonOK.setMaximumSize(QtCore.QSize(100, 35))
        self.pushButtonOK.setStyleSheet("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        self.horizontalLayout_4.addWidget(self.pushButtonOK)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem14)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.verticalLayout.setStretch(11, 1)
        self.horizontalLayout_5.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UsoBeauty"))
        self.label.setText(_translate("MainWindow", "welcome to UsoBeauty"))
        self.sr_zh.setPlaceholderText(_translate("MainWindow", "请输入账号："))
        self.sr_mm.setPlaceholderText(_translate("MainWindow", "请输入密码："))
        self.checkBox.setText(_translate("MainWindow", "记住密码"))
        self.pushButton_register.setText(_translate("MainWindow", "注册"))
        self.pushButtonOK.setText(_translate("MainWindow", "确定"))


        self.checkBox.stateChanged.connect(self.checkBoxChange)
        self.setUsernameAndPassword()


    def checkBoxChange(self, state):
        if (state):
            print("save")
            self.saveUsernameAndPassword()
        else:
            print("cancel")
            self.cancelusernameAndPassword()


    def setUsernameAndPassword(self):
        u, p = self.getUsernameAndPassword()

        self.sr_zh.setText(u)
        self.sr_mm.setText(p)

        if (u == "" and p == ""):
            self.checkBox.setChecked(False)
        else:
            self.checkBox.setChecked(True)


    def getUsernameAndPassword(self):
        with open("./username_password.txt", "r") as f:
            data = f.readlines()
            if (len(data) == 2):
                username = data[0].strip()
                password = data[1].strip()
                return username, password
            else:
                return "", ""


    def cancelusernameAndPassword(self):
        with open("./username_password.txt", "w") as f:
            f.write("")


    def saveUsernameAndPassword(self):
        username = self.sr_zh.text()
        password = self.sr_mm.text()
        print(username, password)
        with open("./username_password.txt", "w") as f:
            f.write(username + "\n")
            f.write(password + "\n")