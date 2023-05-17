from server_PyMysql import MSSQL
from PyQt5 import QtWidgets,QtCore
from server_public_notice import PC_Ui_MainWindow
from PyQt5.Qt import QPixmap,QWidget,QMessageBox

class Public_Notice_MyWindow(QtWidgets.QWidget,PC_Ui_MainWindow):
    def __init__(self):
        super(Public_Notice_MyWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.get_notice_data)
        self.mysql = MSSQL()

    def get_notice_data(self):
        n = []
        n.append(self.lineEdit.text())
        n.append(self.textEdit.toPlainText())
        print(n)
        try:
            self.mysql.store_notice_data(n)
            print('发布成功！')
            QMessageBox.information(self, '消息', '发布成功！')
            self.textEdit.setText('')
            self.lineEdit.setText('')
        except:
            print('添加失败')


