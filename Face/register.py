import sys, math
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtCore, QtGui
import random
from PyMysql import *
from PyQt5.Qt import *

class Example(object):
    def setui(self,MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setObjectName("UsoBeauty")
        MainWindow.setWindowTitle(_translate("UsoBeauty", "UsoBeauty"))
        MainWindow.resize(775, 606)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Face-server/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)

        self.pushButton_exit = QtWidgets.QCommandLinkButton(self)
        self.pushButton_exit.setGeometry(QtCore.QRect(670, 500, 111, 52))
        self.pushButton_exit.setObjectName("pushButton_register")
        self.pushButton_exit.setText(_translate("MainWindow", "返回"))

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(175, 40, 431, 151))
        self.label.setStyleSheet("#label{\n"
                                 "    color:rgb(170, 85, 0);background:rgb(255, 170, 125);border:2px solid #F3F3F5;border-radius:45px;\n"
                                 "                font-size:20pt; font-weight:400;font-family: Roman times;\n"
                                 "}")
        self.label.setObjectName("label")
        self.label.setText(_translate("MainWindow", "        欢迎注册"))

        label_wzbj = 'border-width:1px;border-style:solid;font-size:15px;border-color:rgb(0,0,0,0.5);background-color:rgb(255, 254, 239);'
        self.label_zh = QLabel(self)
        self.label_zh.setText("账户 :")
        self.label_zh.move(100, 210)
        self.label_zh.setFixedSize(100, 30)
        self.label_zh.setStyleSheet(label_wzbj)
        self.label_zh.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_mm = QLabel(self)
        self.label_mm.setText("密码 :")
        self.label_mm.move(100, 250)
        self.label_mm.setFixedSize(100, 30)
        self.label_mm.setStyleSheet(label_wzbj)
        self.label_mm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_qmm = QLabel(self)
        self.label_qmm.setText("确认密码 :")
        self.label_qmm.move(100, 290)
        self.label_qmm.setFixedSize(100, 30)
        self.label_qmm.setStyleSheet(label_wzbj)
        self.label_qmm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_lxdh = QLabel(self)
        self.label_lxdh.setText("联系电话 :")
        self.label_lxdh.move(100, 330)
        self.label_lxdh.setFixedSize(100, 30)
        self.label_lxdh.setStyleSheet(label_wzbj)
        self.label_lxdh.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.label_emil = QLabel(self)
        self.label_emil.setText("邮箱 :")
        self.label_emil.move(100, 370)
        self.label_emil.setFixedSize(100, 30)
        self.label_emil.setStyleSheet(label_wzbj)
        self.label_emil.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        self.sr_zh = QLineEdit(self)
        #self.sr_zh.setText("32261228")  # 用户名
        self.sr_zh.setPlaceholderText("请输入您的账号")
        self.sr_zh.move(210, 210)
        self.sr_zh.setFixedSize(400, 30)
        self.sr_zh.setStyleSheet(label_wzbj)

        self.sr_mm = QLineEdit(self)
        self.sr_mm.setPlaceholderText("请输入您的密码")
        self.sr_mm.setEchoMode(QLineEdit.PasswordEchoOnEdit)#密码输入正常，之后特殊显示
        self.sr_mm.move(210, 250)
        self.sr_mm.setFixedSize(400, 30)
        self.sr_mm.setStyleSheet(label_wzbj)

        self.sr_qmm = QLineEdit(self)
        self.sr_qmm.setPlaceholderText("请确认您的密码")
        self.sr_qmm.setEchoMode(QLineEdit.PasswordEchoOnEdit)  # 密码输入正常，之后特殊显示
        self.sr_qmm.move(210, 290)
        self.sr_qmm.setFixedSize(400, 30)
        self.sr_qmm.setStyleSheet(label_wzbj)

        self.sr_lxdh = QLineEdit(self)
        self.sr_lxdh.setPlaceholderText("请输入您的电话")
        self.sr_lxdh.move(210, 330)
        self.sr_lxdh.setFixedSize(400, 30)
        self.sr_lxdh.setStyleSheet(label_wzbj)

        self.sr_emil = QLineEdit(self)
        self.sr_emil.setPlaceholderText("请输入您的邮箱地址")
        self.sr_emil.move(210, 370)
        self.sr_emil.setFixedSize(400, 30)
        self.sr_emil.setStyleSheet(label_wzbj)

        #右侧确认
        self.label_zh_qr = QLabel(self)
        self.label_zh_qr.setText("*")
        self.label_zh_qr.move(620, 210)
        self.label_zh_qr.setFixedSize(100, 30)

        self.label_mm_qr = QLabel(self)
        self.label_mm_qr.setText("*")
        self.label_mm_qr.move(620, 250)
        self.label_mm_qr.setFixedSize(100, 30)

        self.label_qmm_qr = QLabel(self)
        self.label_qmm_qr.setText("*")
        self.label_qmm_qr.move(620, 290)
        self.label_qmm_qr.setFixedSize(100, 30)

        self.label_lxdh_qr = QLabel(self)
        self.label_lxdh_qr.setText("")
        self.label_lxdh_qr.move(620, 330)
        self.label_lxdh_qr.setFixedSize(100, 30)

        self.label_emil_qr = QLabel(self)
        self.label_emil_qr.setText("")
        self.label_emil_qr.move(620, 370)
        self.label_emil_qr.setFixedSize(100, 30)

        #使用条款外链接
        self.label_sytk_qr = QLabel(self)
        self.label_sytk_qr.setText("请认真阅读：<a href='https://www.baidu.com/'>《使用条款》</a>")
        self.label_sytk_qr.setOpenExternalLinks(True)#允许超链接
        self.label_sytk_qr.move(210, 410)
        self.label_sytk_qr.setFixedSize(200, 36)
        self.label_sytk_qr.setStyleSheet('font-size:15px;')

        #同意协议并注册
        self.bt1 = QPushButton('获取随机验证码', self)
        self.bt1.move(100, 450)
        self.bt1.setFixedSize(100, 36)
        # 设定时间
        self.count = 30
        self.bt1.clicked.connect(self.Action)
        self.time = QtCore.QTimer(self)
        # 每秒1000毫秒
        self.time.setInterval(1000)
        # 时间到触发 Refresh
        self.time.timeout.connect(self.Refresh)

        #随机码展示区
        self.label_sjm = QLabel(self)
        self.label_sjm.setText("随机码")
        self.label_sjm.move(210, 450)
        self.label_sjm.setFixedSize(60, 36)
        self.label_sjm.setStyleSheet(label_wzbj)
        self.label_sjm.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignCenter)

        #输入验证码
        self.sr_yzm = QLineEdit(self)
        self.sr_yzm.setPlaceholderText("请输入您的验证码")
        self.sr_yzm.move(280, 450)
        self.sr_yzm.setFixedSize(200, 36)
        self.sr_yzm.setStyleSheet(label_wzbj)

        #同意协议并注册
        self.bt2 = QPushButton('同意协议并注册', self)
        self.bt2.move(490, 450)
        self.bt2.setFixedSize(150, 36)
        self.bt2.clicked.connect(self.register)

        self.label_zctg_qr = QLabel(self)
        self.label_zctg_qr.setText("")
        self.label_zctg_qr.move(620, 450)
        self.label_zctg_qr.setFixedSize(100, 30)


        # self.show()



    def Action(self):
        if self.bt1.isEnabled():
            self.time.start()
            self.bt1.setEnabled(False)
            sjs = str(random.randint(0, 9999))
            #如果随机码长度不够4位，前面补零
            if len(sjs) < 4:
                sjs = '0' * (4 - len(sjs)) + sjs
            self.label_sjm.setText(sjs)

    def show_exit_menu(self):
        self.exit_signal.emit()


    def Refresh(self):
        if self.count > 0:
            self.bt1.setText(str(self.count) + '秒后重发')
            self.count -= 1
        else:
            self.time.stop()
            self.bt1.setText('获取随机验证码')
            self.bt1.setEnabled(True)
            # 点击发送后 count 重置为30
            self.count = 30

    def register(self):
        #先将标记还原
        self.label_zh_qr.setText('*')
        self.label_mm_qr.setText('*')
        self.label_qmm_qr.setText('*')

        if len(self.sr_zh.text()) == 0:
            self.label_zh_qr.setText('用户账号为空')

        elif len(self.sr_mm.text()) == 0:
            self.label_mm_qr.setText('用户密码为空')

        elif len(self.sr_qmm.text()) == 0:
            self.label_qmm_qr.setText('确认密码为空')

        elif self.sr_qmm.text() != self.sr_mm.text():
            self.label_qmm_qr.setText('确认密码不一致')

        elif len(self.sr_yzm.text()) == 0:
            self.label_zctg_qr.setText('验证码为空')

        elif self.label_sjm.text() != self.sr_yzm.text():
            self.label_zctg_qr.setText('验证码不一致')
        else:
            # self.label_zctg_qr.setText('恭喜注册通过')

            ms = MSSQL()
            print("====================")
            data = []
            data.append(self.sr_zh.text())
            data.append(self.sr_mm.text())
            data.append(self.sr_lxdh.text())
            data.append(self.sr_emil.text())
            # print(tuple(data))
            ms.insert_user_2_db(tuple(data))
            QMessageBox.information(self, '消息', '注册成功')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
