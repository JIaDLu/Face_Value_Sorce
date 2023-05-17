from log_in import Ui_MainWindow
from register import Example as register_ui
import sys
from Face_Sorce_APP import MyWindow


from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets, QtCore, QtGui
from PyMysql import *
from PyQt5.Qt import *
from function_option import Function_Option_MainWindow
from MakupGUI import BP_Ui_MainWindow
from Public_Notice import PN_Ui_MainWindow
import warnings
warnings.filterwarnings('ignore')

# 主窗口
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    switch_window1 = QtCore.pyqtSignal() # 跳转信号
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号
    switch_window3 = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        '''隐蔽窗口'''
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 上窗口
        self.setAttribute((QtCore.Qt.WA_TranslucentBackground))  # 中间空白
        self.pushButton_register.clicked.connect(self.goPic)
        self.pushButtonOK.clicked.connect(self.goapp)
        self.pushButtonCancel.clicked.connect(self.cancel_Log)
    def goPic(self):
        self.switch_window1.emit()
    def goapp(self):
        self.switch_window2.emit()
    def cancel_Log(self):
        self.switch_window3.emit()

    '''实现窗口拖动'''

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton and self.isMaximized() == False:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, mouse_event):
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(mouse_event.globalPos() - self.m_Position)  # 更改窗口位置
            mouse_event.accept()

    def mouseReleaseEvent(self, mouse_event):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    # 窗口拖动结束

# 注册窗口
class PicWindow(QtWidgets.QMainWindow, register_ui):
    switch_window5 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(PicWindow, self).__init__()
        self.setui(self)
        self.pushButton_exit.clicked.connect(self.goPic_main)
    def goPic_main(self):
        self.switch_window5.emit()


# 颜值打分窗口
class FS_AppWindow(QtWidgets.QMainWindow, MyWindow):
    switch_window_1 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(FS_AppWindow, self).__init__()
        self.commandLinkButton.clicked.connect(self.goback)
    def goback(self):
        if self.timer_camera.isActive() == True:
            self.timer_camera.stop()
            self.cap.release()  # 释放视频流
        self.label.setPixmap(QPixmap(""))
        self.switch_window_1.emit()


class BP_AppWindow(QtWidgets.QMainWindow, BP_Ui_MainWindow):
    switch_window_1 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(BP_AppWindow, self).__init__()
        self.commandLinkButton.clicked.connect(self.goback)

    def goback(self):
        self.label.setPixmap(QPixmap(""))
        for ite in self.sls:
            if ite.value() != 0:
                ite.setValue(0)
        self.switch_window_1.emit()


class Public_notice_Window(QtWidgets.QMainWindow, PN_Ui_MainWindow):
    def __init__(self):
        super(Public_notice_Window, self).__init__()
        self.setupUi(self)

# 功能选择窗口
class Function_Option_Window(QtWidgets.QMainWindow, Function_Option_MainWindow):
    switch_window_FS = QtCore.pyqtSignal() # 跳转信号
    switch_window_BP = QtCore.pyqtSignal()  # 跳转信号
    switch_window_main = QtCore.pyqtSignal()
    def __init__(self):
        super(Function_Option_Window, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.goFaceSorce)
        self.pushButton_2.clicked.connect(self.goBeautifyPhoto)
        self.pushButton_3.clicked.connect(self.show_notice)
        self.commandLinkButton.clicked.connect(self.return_main)
        self.mysql = MSSQL()
        self.notice_len = None
        self.mark = None

        self.PN = Public_notice_Window()

    def return_main(self):
        self.switch_window_main.emit()

    def show_notice(self):
        self.PN.show()
        # print(self.mysql.get_notice_data())
        try:
            aaa = str(self.mysql.get_notice_data()[self.notice_len-1][1])
            self.PN.label_2.setText(aaa)
        except:
            self.PN.label_2.setText('')

    def bbb(self):
        self.notice_len = int(len(self.mysql.get_notice_data()))
        print('bbb self.notice_len',self.notice_len)
        self.mark = int(self.mysql.get_mark_data()[0][1])
        print('self.mark',self.mark)
        if self.notice_len != self.mark:
            QMessageBox.information(self, '消息', '您有一则新公告，请注意查收')

    def aaa(self):
        self.notice_len = len(self.mysql.get_notice_data())
        n = (str(self.notice_len))
        self.mysql.insert_mark_data(n)
    def goFaceSorce(self):
        self.switch_window_FS.emit()

    def goBeautifyPhoto(self):
        self.switch_window_BP.emit()

# 利用一个控制器来控制页面的跳转
class Controller1(QWidget):
    def __init__(self):
        super().__init__()
        self.reg = PicWindow()
        self.main = MainWindow()
        self.fs_app = FS_AppWindow()
        self.bp_app = BP_AppWindow()
        self.funtion_o = Function_Option_Window()
        self.reg.hide()
        self.main.hide()
        self.fs_app.hide()
        self.bp_app.hide()
        self.funtion_o.hide()
        self.first_length = None
        self.last_length = None

    # 跳转到 main 窗口
    def show_main(self):
        self.main.show()
        self.main.switch_window1.connect(self.show_reg)
        self.main.switch_window2.connect(self.show_app)
        self.main.switch_window3.connect(self.cancel_Log)

    # 跳转到 pic窗口
    def show_reg(self):
        self.main.close()
        self.reg.show()
        self.reg.switch_window5.connect(self.return_main_show)

    def return_main_show(self):
        self.reg.close()
        self.main.show()

    def cancel_Log(self):
        self.main.close()

    def show_Func_Op(self):
        self.funtion_o.show()
        self.main.close()
        self.funtion_o.bbb()
        self.funtion_o.aaa()
        # self.length = len(self.funtion_o.aaa())
        self.funtion_o.switch_window_FS.connect(self.show_Face_Sorce_Windows)
        self.funtion_o.switch_window_BP.connect(self.show_Beautify_Photo_Windows)
        self.funtion_o.switch_window_main.connect(self.return_mian_show)

    def return_mian_show(self):
        self.funtion_o.close()
        self.main.show()

    def show_Face_Sorce_Windows(self):
        self.fs_app.show()
        self.funtion_o.close()
        # self.funtion_o.aaa()
        self.fs_app.switch_window_1.connect(self.goBack_1_from_fs)

    def goBack_1_from_fs(self):
        self.fs_app.close()
        self.funtion_o.show()

    def show_Beautify_Photo_Windows(self):
        self.bp_app.show()
        self.funtion_o.close()
        # self.funtion_o.aaa()
        self.bp_app.switch_window_1.connect(self.goBack_2_from_bp)

    def goBack_2_from_bp(self):
        self.bp_app.close()
        self.funtion_o.show()

    # 跳转到 pic窗口
    def show_app(self):
        usr_name = self.main.sr_zh.text()
        usr_pwd = self.main.sr_mm.text()
        #2 查询数据库，判定是否有匹配
        ms = MSSQL()
        mark = [1]
        table_name = 'client_info'
        args = ('acount', 'password')
        result = ms.query_super(table_name, args,usr_name,usr_pwd)
        # if self.checkbox.isChecked():
        #     self.settings.setValue('username', usr_name)
        #     self.settings.setValue('password', usr_pwd)
        if(result > 0):
            # print("密码正确")
            QMessageBox.information(self, '消息', '登录成功')
            self.fs_app.usr_name = usr_name
            self.show_Func_Op()
        else:
            # print("密码错误")
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误！",
                                QMessageBox.Yes)
            self.main.sr_zh.setFocus()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    controller1 = Controller1()
    controller1.show_main()
    sys.exit(app.exec_())