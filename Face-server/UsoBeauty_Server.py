from server_log_in import Ui_MainWindow
import sys
from server_function_APP import Server_MyWindow
from server_public_notice_APP import Public_Notice_MyWindow
from PyQt5 import QtWidgets,QtCore
from server_PyMysql import MSSQL
from PyQt5.Qt import QWidget,QMessageBox
from Server_function_option import SFO_Ui_MainWindow

# 主窗口
class MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    switch_window2 = QtCore.pyqtSignal()  # 跳转信号
    switch_window3 = QtCore.pyqtSignal()
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        # self.pushButton_register.clicked.connect(self.goPic)
        self.pushButtonOK.clicked.connect(self.goapp)
        self.pushButtonCancel.clicked.connect(self.cancel_Log)
    def goapp(self):
        self.switch_window2.emit()
    def cancel_Log(self):
        self.switch_window3.emit()

# 功能选择窗口
class Function_Option_Window(QtWidgets.QMainWindow, SFO_Ui_MainWindow):
    switch_window_PN = QtCore.pyqtSignal() # 跳转信号
    switch_window_CG = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(Function_Option_Window, self).__init__()
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.goFaceSorce)
        self.pushButton.clicked.connect(self.goBeautifyPhoto)

    def goFaceSorce(self):
        self.switch_window_PN.emit()

    def goBeautifyPhoto(self):
        self.switch_window_CG.emit()

# 公告发布窗口
class Public_notice_AppWindow(QtWidgets.QMainWindow, Public_Notice_MyWindow):
    switch_window_1 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(Public_notice_AppWindow, self).__init__()
        self.commandLinkButton.clicked.connect(self.goback)

    def goback(self):
        self.switch_window_1.emit()

#管理用户群体
class Server_AppWindow(QtWidgets.QMainWindow, Server_MyWindow):
    switch_window_1 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(Server_AppWindow, self).__init__()
        self.commandLinkButton.clicked.connect(self.quit)
    def quit(self):
        self.switch_window_1.emit()

# 利用一个控制器来控制页面的跳转
class Controller1(QWidget):
    def __init__(self):
        super().__init__()
        self.main = MainWindow()
        self.ser_app = Server_AppWindow()
        self.ser_publicNotice = Public_notice_AppWindow()
        self.ser_functionOption = Function_Option_Window()
        self.main.hide()
        self.ser_app.hide()
        self.ser_functionOption.hide()
        self.ser_publicNotice.hide()

    # 跳转到 main 窗口
    def show_main(self):
        self.main.show()
        self.main.switch_window2.connect(self.show_app)
        self.main.switch_window3.connect(self.cancel_Log)


    def cancel_Log(self):
        self.main.close()

    def show_functionOption_window(self):
        self.ser_functionOption.show()
        self.main.close()
        self.ser_functionOption.switch_window_PN.connect(self.show_Face_Sorce_Windows)
        self.ser_functionOption.switch_window_CG.connect(self.show_Beautify_Photo_Windows)

    def show_Face_Sorce_Windows(self):
        self.ser_publicNotice.show()
        self.ser_functionOption.close()
        self.ser_publicNotice.switch_window_1.connect(self.goBack_1_from_fs)

    def goBack_1_from_fs(self):
        self.ser_publicNotice.close()
        self.ser_functionOption.show()

    def show_Beautify_Photo_Windows(self):
        self.ser_app.show()
        self.ser_functionOption.close()
        self.ser_app.switch_window_1.connect(self.goBack_2_from_bp)

    def goBack_2_from_bp(self):
        self.ser_app.close()
        self.ser_functionOption.show()

    #     self.ser_app.switch_window_1.connect(self.quit_server)
    #
    # def quit_server(self):
    #     reply = QMessageBox.question(self, '退出', '确定退出？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
    #     if reply == QMessageBox.Yes:
    #         sys.exit(app.exec_())

    # 跳转到 pic窗口
    def show_app(self):
        usr_name = self.main.sr_zh.text()
        usr_pwd = self.main.sr_mm.text()
        #2 查询数据库，判定是否有匹配
        ms = MSSQL()
        table_name = 'admin'
        args = ('acount', 'password')
        result = ms.query_super(table_name, args,usr_name,usr_pwd)
        if(result > 0):
            print("密码正确")
            QMessageBox.information(self, '消息', '登录成功')
            self.show_functionOption_window()
        else:
            print("密码错误")
            QMessageBox.warning(self,
                                "警告",
                                "用户名或密码错误！",
                                QMessageBox.Yes)
            self.main.sr_zh.setFocus()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    # app.setStyleSheet(open('./custom/styleSheet.qss', encoding='utf-8').read())
    controller1 = Controller1()  # 控制器实例
    controller1.show_main()
    sys.exit(app.exec_())