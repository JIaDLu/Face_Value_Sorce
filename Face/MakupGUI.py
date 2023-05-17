import sys
import os
import numpy as np
import cv2
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from AIMakeup import Makeup, detector, predictor
from utils import face_thin_auto, SharpenImage
from PyQt5 import QtCore, QtGui, QtWidgets
from Beautiful_Photo import Ui_MainWindow
from PyQt5 import QtWidgets

class BP_Ui_MainWindow(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(BP_Ui_MainWindow, self).__init__()
        self.setupUi(self)

        self.bg_edit = [self.bt_brightening,
                        self.bt_whitening, self.bt_sharpen, self.bt_smooth,
                        self.bt_Laplace]
        self.bg_op = [ self.bt_cancel, self.bt_reset]
        self.bg_result = [self.bt_view_compare,
                          self.bt_save, self.bt_save_compare]
        self.sls = [self.sl_brightening, self.sl_sharpen,
                    self.sl_whitening, self.sl_smooth,
                    self.sl_Laplace,]
        for u in self.sls:
            u.setTickPosition(QtWidgets.QSlider.TicksBelow)
            u.setTickInterval(2)  # 设置刻度的间隔
        # 批量设置状态
        self._set_statu(self.bg_edit, False)
        self._set_statu(self.bg_op, False)
        self._set_statu(self.bg_result, False)
        self._set_statu(self.sls, False)
        # 导入dlib模型文件
        # if os.path.exists("./data/shape_predictor_68_face_landmarks.dat"):
        self.path_predictor = os.path.join(
                "data","shape_predictor_68_face_landmarks.dat")
        # else:
        #     QMessageBox.warning(self.centralWidget, '警告', '默认的dlib模型文件路径不存在，请指定文件位置。\
        #                         \n或从http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2下载')
        #     self.path_predictor, _ = QFileDialog.getOpenFileName(
        #         self.centralWidget, '选择dlib模型文件', './', 'Data Files(*.dat)')
        # 实例化化妆器
        self.mu = Makeup(self.path_predictor)
        self.path_img = ''
        self._set_connect()

    def _set_connect(self):
        '''
        设置程序逻辑
        '''
        self.bt_open.clicked.connect(self._open_img)
        OPs = ['sharpen', 'whitening', 'smooth', 'brightening',
               'Laplace', 'cancel', 'reset',
               'save', 'save_compare', 'view_compare']
        for op in OPs:
            self.__getattribute__(
                'bt_'+op).clicked.connect(self.__getattribute__('_'+op))

    def _open_img(self):
        '''
        打开图片
        '''
        print('111111')
        self.path_img, _ = QFileDialog.getOpenFileName(
            None, '打开图片文件', './', 'Image Files(*.png *.jpg *.bmp)')
        if self.path_img and os.path.exists(self.path_img):
            print(self.path_img)
            self.im_bgr, self.temp_bgr, self.faces = self.mu.read_and_mark(
                self.path_img)
            self.im_ori, self.previous_bgr = self.im_bgr.copy(), self.im_bgr.copy()
            self._set_statu(self.bg_edit, True)
            self._set_statu(self.bg_op, True)
            self._set_statu(self.bg_result, True)
            self._set_statu(self.sls, True)
            self._set_img()
        else:
            QMessageBox.warning(self, '无效路径', '无效路径，请重新选择！')

    def _cv2qimg(self, cvImg):
        '''
        将opencv的图片转换为QImage
        '''
        height, width, channel = cvImg.shape
        bytesPerLine = 3 * width
        image2show = QImage(cv2.cvtColor(cvImg, cv2.COLOR_BGR2RGB).data,
                            width, height, bytesPerLine, QImage.Format_RGB888)
        return image2show

    def _set_img(self):
        '''
        显示pixmap
        '''
        self.label.setPixmap(QPixmap.fromImage(self._cv2qimg(self.temp_bgr)))
        self._confirm()

    def _set_statu(self, group, value):
        '''
        批量设置状态
        '''
        [item.setEnabled(value) for item in group]

    def _confirm(self):
        '''
        确认操作
        '''
        self.im_bgr[:] = self.temp_bgr[:]

    def _cancel(self):
        '''
        还原到上一步
        '''
        self.temp_bgr[:] = self.previous_bgr[:]
        self._set_img()


    def _reset(self):
        '''
        重置为原始图片
        '''
        self.temp_bgr[:] = self.im_ori[:]
        self._set_img()
        for it in self.sls:
            it.setValue(0)

    def _mapfaces(self, fun, value):
        '''
        对每张脸进行迭代操作
        '''
        self.previous_bgr[:] = self.temp_bgr[:]
        for face in self.faces[self.path_img]:
            fun(face, value)
        self._set_img()

    def _Laplace(self):
        value = min(1, max(self.sl_Laplace.value()/200, 0))
        kernel = np.array([[0, -1, 0], [0, 5, 0], [0, -1, 0]])
        print('-[INFO] laplace:', value)
        self.previous_bgr[:] = self.temp_bgr[:]
        self.temp_bgr = SharpenImage(self.temp_bgr)
        # self.temp_bgr = cv2.filter2D(self.temp_bgr, -1, kernel)
        self.temp_bgr = np.minimum(self.temp_bgr, 255).astype('uint8')
        self.im_bgr = self.temp_bgr
        self._set_img()


    def _sharpen(self):
        value = min(1, max(self.sl_sharpen.value()/200, 0))
        print('-[INFO] sharpen:', value)

        def fun(face, value):
            face.organs['left eye'].sharpen(value, confirm=False)
            face.organs['right eye'].sharpen(value, confirm=False)
        self._mapfaces(fun, value)

    def _whitening(self):
        value = min(1, max(self.sl_whitening.value()/200, 0))
        print('-[INFO] whitening:', value)

        def fun(face, v):
            face.organs['left eye'].whitening(value, confirm=False)
            face.organs['right eye'].whitening(value, confirm=False)
            face.organs['left brow'].whitening(value, confirm=False)
            face.organs['right brow'].whitening(value, confirm=False)
            face.organs['nose'].whitening(value, confirm=False)
            face.organs['forehead'].whitening(value, confirm=False)
            face.organs['mouth'].whitening(value, confirm=False)
            face.whitening(value, confirm=False)
        self._mapfaces(fun, value)

    def _brightening(self):
        value = min(1, max(self.sl_brightening.value()/200, 0))
        print('-[INFO] brightening:', value)

        def fun(face, value):
            face.organs['mouth'].brightening(value, confirm=False)
        self._mapfaces(fun, value)

    def _smooth(self):
        value = min(1, max(self.sl_smooth.value()/100, 0))
        print('-[INFO] smooth:', value)

        def fun(face, value):
            face.smooth(value, confirm=False)
            face.organs['nose'].smooth(value*2/3, confirm=False)
            face.organs['forehead'].smooth(value*3/2, confirm=False)
            face.organs['mouth'].smooth(value, confirm=False)
        self._mapfaces(fun, value)

    def _save(self):
        output_path, _ = QFileDialog.getSaveFileName(
            None, '选择保存位置', './', 'Image Files(*.png *.jpg *.bmp)')
        if output_path:
            self.save(output_path, self.im_bgr)
        else:
            QMessageBox.warning(self, '无效路径', '无效路径，请重新选择！')

    def _save_compare(self):
        output_path, _ = QFileDialog.getSaveFileName(
            None, '选择保存位置', './', 'Image Files(*.png *.jpg *.bmp)')
        if output_path:
            self.save(output_path, np.concatenate(
                [self.im_ori, self.im_bgr], 1))
        else:
            QMessageBox.warning(self, '无效路径', '无效路径，请重新选择！')

    def _view_compare(self):
        cv2.imshow('Compare', np.concatenate([self.im_ori, self.im_bgr], 1))
        cv2.waitKey()

    def save(self, output_path, output_im):
        cv2.imencode('.jpg', output_im)[1].tofile(output_path)


