from PyQt5 import QtWidgets,QtCore,QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("UsoBeauty")
        MainWindow.resize(875, 646)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Face-server/logo.ico"), QtGui.QIcon.Normal,
                       QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(220, 40, 431, 151))
        self.label.setStyleSheet("#label{\n"
                                 "    color:rgb(170, 85, 0);background:rgb(255, 254, 239);border:2px solid #F3F3F5;border-radius:45px;\n"
                                 "                font-size:20pt; font-weight:400;font-family: Roman times;\n"
                                 "}")
        self.label.setObjectName("label")
        self.label_zh = QtWidgets.QLabel(self.centralwidget)
        self.label_zh.setGeometry(QtCore.QRect(110, 250, 101, 41))
        self.label_zh.setObjectName("label_zh")
        self.label_mm = QtWidgets.QLabel(self.centralwidget)
        self.label_mm.setGeometry(QtCore.QRect(110, 320, 101, 41))
        self.label_mm.setObjectName("label_mm")
        self.sr_zh = QtWidgets.QLineEdit(self.centralwidget)
        self.sr_zh.setGeometry(QtCore.QRect(180, 250, 531, 41))
        self.sr_zh.setText("admin")
        self.sr_zh.setStyleSheet("#sr_zh{\n"
                                 "color:rgb(170, 0, 0);\n"
                                 "                    border:2px solid #F3F3F5;\n"
                                 "                    border-radius:15px;\n"
                                 "                    background:rgb(230, 255, 255);\n"
                                 "border:2px solid #423f48;\n"
                                 "}")
        self.sr_zh.setObjectName("sr_zh")
        self.sr_mm = QtWidgets.QLineEdit(self.centralwidget)
        self.sr_mm.setGeometry(QtCore.QRect(180, 320, 531, 41))
        self.sr_mm.setEchoMode(2)
        # self.label_mm.setText("admin")
        self.sr_mm.setStyleSheet("#sr_mm{\n"
                                 "color:rgb(170, 0, 0);\n"
                                 "                    border:2px solid #F3F3F5;\n"
                                 "                    border-radius:15px;\n"
                                 "                    background:rgb(230, 255, 255);\n"
                                 "border:2px solid #423f48;\n"
                                 "}")
        self.sr_mm.setObjectName("sr_mm")
        self.pushButtonOK = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOK.setGeometry(QtCore.QRect(200, 410, 131, 51))
        self.pushButtonOK.setStyleSheet("")
        self.pushButtonOK.setObjectName("pushButtonOK")
        # self.pushButton_register = QtWidgets.QCommandLinkButton(self.centralwidget)
        # self.pushButton_register.setGeometry(QtCore.QRect(670, 500, 111, 52))
        # self.pushButton_register.setObjectName("pushButton_register")
        self.pushButtonCancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonCancel.setGeometry(QtCore.QRect(490, 410, 131, 51))
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 875, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("UsoBeauty", "UsoBeauty"))
        self.label.setText(_translate("MainWindow", "  管理端：管理员请登陆"))
        self.label_zh.setText(_translate("MainWindow", "账户："))
        self.label_mm.setText(_translate("MainWindow", "密码："))
        self.pushButtonOK.setText(_translate("MainWindow", "确定"))
        self.pushButtonCancel.setText(_translate("MainWindow", "取消"))


