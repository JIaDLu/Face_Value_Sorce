# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Beautiful_Photo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1104, 800)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Face-server/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#frame{\n"
"    border-image: url(:/bg/bg1.png);}\n"
"*{font: 12pt \"楷体\";}\n"
"QPushButton{\n"
"    background-color:#FF455E;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtWidgets.QSpacerItem(20, 779, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.commandLinkButton = QtWidgets.QCommandLinkButton(self.frame)
        self.commandLinkButton.setMinimumSize(QtCore.QSize(100, 30))
        self.commandLinkButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.commandLinkButton.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0, 0, 0);\n"
"    color:rgb(0, 0, 0);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/bg/返回.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.commandLinkButton.setIcon(icon)
        self.commandLinkButton.setIconSize(QtCore.QSize(30, 30))
        self.commandLinkButton.setObjectName("commandLinkButton")
        self.horizontalLayout_6.addWidget(self.commandLinkButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem2)
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setStyleSheet("#frame_4{\n"
"border-radius:30px;  \n"
"border:2px solid #FF455E;\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem3)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setStyleSheet("#label{\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout_7.addWidget(self.label)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_7.addItem(spacerItem4)
        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_5.addWidget(self.frame_4)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.setStretch(2, 1)
        self.horizontalLayout_11.addLayout(self.verticalLayout_5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 779, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem7)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem8)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setStyleSheet("")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        self.verticalLayout_6.addLayout(self.horizontalLayout_10)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:30px;\n"
"}\n"
"QPushButton::hover{\n"
"    padding-bottom:15px;\n"
"    border-radius: 30px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"  \n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem9)
        self.bt_open = QtWidgets.QPushButton(self.frame_5)
        self.bt_open.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_open.setStyleSheet("")
        self.bt_open.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/bg/图片.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_open.setIcon(icon1)
        self.bt_open.setIconSize(QtCore.QSize(30, 30))
        self.bt_open.setObjectName("bt_open")
        self.horizontalLayout_7.addWidget(self.bt_open)
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem10)
        self.bt_reset = QtWidgets.QPushButton(self.frame_5)
        self.bt_reset.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_reset.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/bg/恢复.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_reset.setIcon(icon2)
        self.bt_reset.setIconSize(QtCore.QSize(30, 30))
        self.bt_reset.setObjectName("bt_reset")
        self.horizontalLayout_7.addWidget(self.bt_reset)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem11)
        self.bt_cancel = QtWidgets.QPushButton(self.frame_5)
        self.bt_cancel.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_cancel.setStyleSheet("")
        self.bt_cancel.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/bg/撤销.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_cancel.setIcon(icon3)
        self.bt_cancel.setIconSize(QtCore.QSize(30, 30))
        self.bt_cancel.setObjectName("bt_cancel")
        self.horizontalLayout_7.addWidget(self.bt_cancel)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem12)
        self.verticalLayout_8.addLayout(self.horizontalLayout_7)
        self.verticalLayout_6.addWidget(self.frame_5)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem13)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:#FF455E;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bt_whitening = QtWidgets.QPushButton(self.frame_2)
        self.bt_whitening.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_whitening.setStyleSheet("")
        self.bt_whitening.setObjectName("bt_whitening")
        self.horizontalLayout.addWidget(self.bt_whitening)
        self.sl_whitening = QtWidgets.QSlider(self.frame_2)
        self.sl_whitening.setStyleSheet("#sl_whitening{\n"
"    background-color:rgb(174, 230, 255)\n"
"}")
        self.sl_whitening.setOrientation(QtCore.Qt.Horizontal)
        self.sl_whitening.setObjectName("sl_whitening")
        self.horizontalLayout.addWidget(self.sl_whitening)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem14)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bt_brightening = QtWidgets.QPushButton(self.frame_2)
        self.bt_brightening.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_brightening.setStyleSheet("")
        self.bt_brightening.setObjectName("bt_brightening")
        self.horizontalLayout_4.addWidget(self.bt_brightening)
        self.sl_brightening = QtWidgets.QSlider(self.frame_2)
        self.sl_brightening.setStyleSheet("#sl_brightening{\n"
"    background-color:rgb(190, 224, 255)\n"
"}")
        self.sl_brightening.setOrientation(QtCore.Qt.Horizontal)
        self.sl_brightening.setObjectName("sl_brightening")
        self.horizontalLayout_4.addWidget(self.sl_brightening)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem15)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bt_Laplace = QtWidgets.QPushButton(self.frame_2)
        self.bt_Laplace.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_Laplace.setStyleSheet("")
        self.bt_Laplace.setObjectName("bt_Laplace")
        self.horizontalLayout_5.addWidget(self.bt_Laplace)
        self.sl_Laplace = QtWidgets.QSlider(self.frame_2)
        self.sl_Laplace.setStyleSheet("#sl_Laplace{\n"
"    background-color:rgb(190, 224, 255)\n"
"}")
        self.sl_Laplace.setOrientation(QtCore.Qt.Horizontal)
        self.sl_Laplace.setObjectName("sl_Laplace")
        self.horizontalLayout_5.addWidget(self.sl_Laplace)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem16)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bt_smooth = QtWidgets.QPushButton(self.frame_2)
        self.bt_smooth.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_smooth.setStyleSheet("")
        self.bt_smooth.setObjectName("bt_smooth")
        self.horizontalLayout_2.addWidget(self.bt_smooth)
        self.sl_smooth = QtWidgets.QSlider(self.frame_2)
        self.sl_smooth.setStyleSheet("#sl_smooth{\n"
"    background-color:rgb(190, 224, 255)\n"
"}")
        self.sl_smooth.setOrientation(QtCore.Qt.Horizontal)
        self.sl_smooth.setObjectName("sl_smooth")
        self.horizontalLayout_2.addWidget(self.sl_smooth)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem17)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bt_sharpen = QtWidgets.QPushButton(self.frame_2)
        self.bt_sharpen.setMinimumSize(QtCore.QSize(100, 30))
        self.bt_sharpen.setStyleSheet("")
        self.bt_sharpen.setObjectName("bt_sharpen")
        self.horizontalLayout_3.addWidget(self.bt_sharpen)
        self.sl_sharpen = QtWidgets.QSlider(self.frame_2)
        self.sl_sharpen.setStyleSheet("#sl_sharpen{\n"
"    background-color:rgb(190, 224, 255)\n"
"}")
        self.sl_sharpen.setOrientation(QtCore.Qt.Horizontal)
        self.sl_sharpen.setObjectName("sl_sharpen")
        self.horizontalLayout_3.addWidget(self.sl_sharpen)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_6.addWidget(self.frame_2)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem18)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem19)
        self.bt_view_compare = QtWidgets.QPushButton(self.frame)
        self.bt_view_compare.setMinimumSize(QtCore.QSize(60, 60))
        self.bt_view_compare.setStyleSheet("QPushButton{\n"
"    background-color:rgb(255, 255, 255);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:30px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}\n"
"QPushButton::hover{\n"
"    padding-bottom:15px;\n"
"    border-radius: 30px;\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"  \n"
"}")
        self.bt_view_compare.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/bg/对比.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bt_view_compare.setIcon(icon4)
        self.bt_view_compare.setIconSize(QtCore.QSize(30, 30))
        self.bt_view_compare.setObjectName("bt_view_compare")
        self.horizontalLayout_9.addWidget(self.bt_view_compare)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem20)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_6.addItem(spacerItem21)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("\n"
"QPushButton{\n"
"    background-color:#FF455E;\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    padding-left:5px;\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem22)
        self.bt_save = QtWidgets.QPushButton(self.frame_3)
        self.bt_save.setMinimumSize(QtCore.QSize(150, 30))
        self.bt_save.setStyleSheet("")
        self.bt_save.setObjectName("bt_save")
        self.horizontalLayout_8.addWidget(self.bt_save)
        self.bt_save_compare = QtWidgets.QPushButton(self.frame_3)
        self.bt_save_compare.setMinimumSize(QtCore.QSize(150, 30))
        self.bt_save_compare.setStyleSheet("")
        self.bt_save_compare.setObjectName("bt_save_compare")
        self.horizontalLayout_8.addWidget(self.bt_save_compare)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem23)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.verticalLayout_6.addWidget(self.frame_3)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem24)
        self.horizontalLayout_11.addLayout(self.verticalLayout_6)
        spacerItem25 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout_11.addItem(spacerItem25)
        self.horizontalLayout_11.setStretch(1, 1)
        self.verticalLayout_2.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UsoBeauty"))
        self.commandLinkButton.setText(_translate("MainWindow", "返回"))
        self.label_2.setText(_translate("MainWindow", "请在返回前保存图片"))
        self.bt_open.setToolTip(_translate("MainWindow", "打开图片"))
        self.bt_reset.setToolTip(_translate("MainWindow", "还原"))
        self.bt_cancel.setToolTip(_translate("MainWindow", "撤销更改"))
        self.bt_whitening.setText(_translate("MainWindow", "美白"))
        self.bt_brightening.setText(_translate("MainWindow", "红唇"))
        self.bt_Laplace.setText(_translate("MainWindow", "锐化"))
        self.bt_smooth.setText(_translate("MainWindow", "磨皮"))
        self.bt_sharpen.setText(_translate("MainWindow", "亮眼"))
        self.bt_view_compare.setToolTip(_translate("MainWindow", "查看对比"))
        self.bt_save.setText(_translate("MainWindow", "保存"))
        self.bt_save_compare.setText(_translate("MainWindow", "保存对比"))

import images_rc
