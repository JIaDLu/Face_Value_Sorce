from server_get_work_data import DATA_Ui_MainWindow
from PyQt5 import QtWidgets
from server_PyMysql import MSSQL
import pandas as pd
from PyQt5.QtCore import QAbstractTableModel,Qt
from server_delete import Ui_MainWindow
from PyQt5.Qt import QPixmap,QWidget,QMessageBox
from server_add import Add_Ui_MainWindow
from PyQt5 import QtWidgets,QtCore

class Server_MyWindow(QtWidgets.QWidget,DATA_Ui_MainWindow):
    def __init__(self):
        super(Server_MyWindow, self).__init__()
        self.setupUi(self)
        self.mysql = MSSQL()
        self.df = {}

        self.pushButton_3.clicked.connect(self.show_work_data_)
        self.pushButton_4.clicked.connect(self.deleteRecord)
        self.pushButton_5.clicked.connect(self.addRecord)
        self.pushButton.clicked.connect(self.setBrowerPath)
        self.pushButton_2.clicked.connect(self.savefile)

        self.delete_class = DeleteWindow()
        self.add_class = AddWindow()

    def deleteRecord(self):
        self.delete_class.show()

    def addRecord(self):
        self.add_class.show()
        self.add_class.switch_window_1.connect(self.Meanwhile_unpate)

    def Meanwhile_unpate(self):
        del_row = self.tableView.currentIndex().row()
        self.model.removeRow(del_row)
        self.show_work_data_()

    def show_work_data_(self):
        result = self.mysql.get_work_data_info()
        dict = {}
        for number, i in enumerate(result):
            dict[number] = i
        self.df = pd.DataFrame(dict)
        self.model = PdTable(self.df)
        view = self.tableView
        view.setModel(self.model)

    def setBrowerPath(self):  # 选择文件夹进行存储
        download_path = QtWidgets.QFileDialog.getExistingDirectory(None, "浏览", "/home")
        self.lineEdit.setText(download_path)

    def savefile(self):
        if len(self.lineEdit_2.text()) < 1:
            QMessageBox.information(self.pushButton, ' ', '文件名不可为空', QMessageBox.Ok)
        else:
            try:
                aaa = pd.DataFrame(self.df)
                aaa.to_csv(self.lineEdit.text() + '/' + self.lineEdit_2.text() + '.csv')
                QMessageBox.information(self, '消息', '已保存到指定路径')
            except:
                QMessageBox.information(self.pushButton, ' ', '所选目录错误！', QMessageBox.Ok)


class PdTable(QAbstractTableModel):
    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    # 显示数据
    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    # 显示行和列头
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.axes[0][col]
        return None


class DeleteWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(DeleteWindow, self).__init__()
        self.setupUi(self)
        self.mysql = MSSQL()
        self.pushButton.clicked.connect(self.delete)

    def delete(self):
        numb = self.lineEdit.text()
        try:
            self.mysql.delete(numb)
            print('删除成功！')
            QMessageBox.information(self, '消息', '删除成功！')
            self.lineEdit.setText('')
        except:
            print('删除失败')


class AddWindow(QtWidgets.QMainWindow, Add_Ui_MainWindow):
    switch_window_1 = QtCore.pyqtSignal()  # 跳转信号
    def __init__(self):
        super(AddWindow, self).__init__()
        self.setupUi(self)
        self.mysql = MSSQL()
        self.pushButton.clicked.connect(self.add)

    def add(self):
        n = []
        n.append(self.lineEdit.text())
        n.append(self.lineEdit_2.text())
        n.append(self.lineEdit_4.text())
        n.append(self.lineEdit_3.text())
        print(n)
        try:
            self.mysql.add(n)
            print('添加成功！')
            QMessageBox.information(self, '消息', '添加成功！')
            self.lineEdit.setText('')
            self.lineEdit_2.setText('')
            self.lineEdit_4.setText('')
            self.lineEdit_3.setText('')
            self.switch_window_1.emit()
        except:
            print('添加失败')
