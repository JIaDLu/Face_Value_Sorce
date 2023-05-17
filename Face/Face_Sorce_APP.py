import matplotlib.pyplot as plt
import numpy as np
import torch
import win32api, win32con
from threading import Thread
import torchvision.transforms as transforms
import Nets
from PIL import Image
from Face_Sorce_window import Ui_MainWindow

from PyQt5 import QtWidgets,QtGui,QtCore
import cv2
import sys
import mediapipe as mp
import time
from PyQt5 import QtWidgets,QtCore
import io
from PyQt5.Qt import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QGraphicsScene, QGraphicsPixmapItem
import warnings
from face_criterion import FC_Ui_MainWindow
warnings.filterwarnings('ignore')

class MyWindow(QtWidgets.QWidget,Ui_MainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

        self.timer_camera = QtCore.QTimer()  # 定义定时器，用于控制显示视频的帧率
        self.cap = cv2.VideoCapture()  # 视频流
        self.CAM_NUM = 0  # 为0时表示视频流来自笔记本内置摄像头

        self.slot_init()  # 初始化槽函数
        self.mp_drawing = mp.solutions.drawing_utils

        # 导入人脸识别模块
        self.mpFace = mp.solutions.face_detection
        # 导入绘图模块
        self.mpDraw = mp.solutions.drawing_utils
        # 自定义人脸识别方法，最小的人脸检测置信度0.5
        self.faceDetection = self.mpFace.FaceDetection(min_detection_confidence=0.5)
        self.pTime = 0  # 记录每帧图像处理的起始时间

        self.boxlist = []  # 保存每帧图像每个框的信息
        self.face_img_info = {}
        self.img_res = []
        self.face_sorce = 0
        self.usr_name = ''
        self.fc_ui = FC_ui()

        # self.switch_window_1 = QtCore.pyqtSignal()
        # 多线程成员
        self.thread_start_btn = 0
        self.mark = 0

    def slot_init(self):
        self.pushButton.clicked.connect(self.button_open_camera_clicked)# 若该按键被点击，则调用button_open_camera_clicked()
        self.timer_camera.timeout.connect(self.show_camera)# 若定时器结束，则调用show_camera()
        self.commandLinkButton_2.clicked.connect(self.renew_camera)
        self.pushButton_2.clicked.connect(self.start_sorce)
        self.commandLinkButton_3.clicked.connect(self.com_config)
    '''点击识别的时候，要坚持数据库的image列是否有数据，若没有，需要提示用户重新录入人脸'''

    def com_config(self):
        self.fc_ui.show()

    def renew_camera(self):
        if self.graphicsView.scene() == None and self.timer_camera.isActive() == True:
            QMessageBox.information(self, '消息', '您正在录入，请对准摄像头')
        elif self.graphicsView.scene() == None:
            QMessageBox.information(self, '消息', '您需要先开启摄像头')
        elif self.graphicsView.scene() == True and self.timer_camera.isActive() == False:
            QMessageBox.information(self, '消息', '您直接开启摄像头即可')
        else:
            self.face_sorce = 0
            self.boxlist = []
            self.img_res = []
            self.face_img_info = {}
            self.label.setPixmap(QPixmap(""))
            if self.timer_camera.isActive() == True:
                self.timer_camera.stop()
                self.cap.release()  # 释放视频流
            '''这里要有清空对应用户名数据库的image列的数据'''
            QMessageBox.information(self, '消息', '点击开启摄像头即可')

    def read(self):
        self.file_name, ok = QFileDialog.getOpenFileName(self, '读取', '../images')
        jpg = QtGui.QPixmap(self.file_name).scaled(200, 200)
        graphicscene = QtWidgets.QGraphicsScene()
        graphicscene.addPixmap(jpg)
        self.graphicsView.setScene(graphicscene)
        self.graphicsView.show()  # 显示原图
        # self.img = cv2.imread(self.file_name)
        # self.result_path = self.deal_img()

    def button_open_camera_clicked(self):
        if self.timer_camera.isActive() == False:  # 若定时器未启动
            flag = self.cap.open(self.CAM_NUM)  # 参数是0，表示打开笔记本的内置摄像头，参数是视频文件路径则打开视频
            if flag == False:  # flag表示open()成不成功
                msg = QtWidgets.QMessageBox.warning(self, 'warning', "请检查相机于电脑是否连接正确", buttons=QtWidgets.QMessageBox.Ok)
            else:
                self.timer_camera.start(20)  # 定时器开始计时30ms，结果是每过30ms从摄像头中取一帧显示
                # self.button_open_camera.setText('关闭相机')


    def show_close(self):
        self.timer_camera.stop()  # 关闭定时器
        self.cap.release()  # 释放视频流
        # self.label.clear()

    def show_camera(self):
        flag, self.image = self.cap.read()  # 从视频流中读取
        # 将opencv导入的BGR图像转为RGB图像
        imgRGB = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
        # 将每一帧图像传给人脸识别模块
        results = self.faceDetection.process(imgRGB)
        # 如果检测不到人脸那就返回None
        if results.detections:
            # 返回人脸索引index(第几张脸)，和关键点的坐标信息
            in_a = []
            for index, detection in enumerate(results.detections):
                in_a.append(index)
            if len(in_a) > 2:
                QMessageBox.information(self, '消息', '请保持摄像头前为一个人脸')
            else:
                # 遍历每一帧图像并打印结果
                # print(index, detection)
                # 每帧图像返回一次是人脸的几率，以及识别框的xywh，后续返回关键点的xy坐标
                # print(detection.score)  # 是人脸的的可能性
                # print(detection.location_data.relative_bounding_box)  # 识别框的xywh

                # 设置一个边界框，接收所有的框的xywh及关键点信息
                bboxC = detection.location_data.relative_bounding_box

                # 接收每一帧图像的宽、高、通道数
                ih, iw, ic = self.image.shape

                # 将边界框的坐标点从比例坐标转换成像素坐标
                # 将边界框的宽和高从比例长度转换为像素长度
                bbox = (int(bboxC.xmin * iw), int(bboxC.ymin * ih),
                        int(bboxC.width * iw), int(bboxC.height * ih))

                # 有了识别框的xywh就可以在每一帧图像上把框画出来
                # cv2.rectangle(img, bbox, (255,0,0), 5)  # 自定义绘制函数，不适用官方的mpDraw.draw_detection

                if round(detection.score[0] * 100, 2) > 96.30:
                    QMessageBox.information(self, '消息', '人脸录入完毕')
                    self.show_close()
                    # 保存索引，人脸概率，识别框的x/y/w/h
                    self.boxlist.append([detection.score, bbox])
                    self.face_img_info[0] = self.image
                    self.show_cut_picture_result()
                # else:self.switch_window_1.connect(self.show_cut_picture_result)

                # 把人脸的概率显示在检测框上,img画板，概率值*100保留两位小数变成百分数，再变成字符串
                cv2.putText(self.image, f'{str(round(detection.score[0] * 100, 2))}%',
                            (bbox[0], bbox[1] - 20),  # 文本显示的位置，-20是为了不和框重合
                            cv2.FONT_HERSHEY_PLAIN,  # 文本字体类型
                            2, (0, 0, 255), 2)  # 字体大小; 字体颜色; 线条粗细

                # （3）修改识别框样式
                x, y, w, h = bbox  # 获取识别框的信息,xy为左上角坐标点
                x1, y1 = x + w, y + h  # 右下角坐标点

                # 绘制比矩形框粗的线段，img画板，线段起始点坐标，线段颜色，线宽为8
                cv2.line(self.image, (x, y), (x + 20, y), (255, 0, 255), 4)
                cv2.line(self.image, (x, y), (x, y + 20), (255, 0, 255), 4)

                cv2.line(self.image, (x1, y1), (x1 - 20, y1), (255, 0, 255), 4)
                cv2.line(self.image, (x1, y1), (x1, y1 - 20), (255, 0, 255), 4)

                cv2.line(self.image, (x1, y), (x1 - 20, y), (255, 0, 255), 4)
                cv2.line(self.image, (x1, y), (x1, y + 20), (255, 0, 255), 4)

                cv2.line(self.image, (x, y1), (x + 20, y1), (255, 0, 255), 4)
                cv2.line(self.image, (x, y1), (x, y1 - 20), (255, 0, 255), 4)

                # 在每一帧图像上绘制矩形框
                cv2.rectangle(self.image, bbox, (255, 0, 255), 1)  # 自定义绘制函数

                show = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)
                # 显示图像，输入窗口名及图像数据
                showImage = QtGui.QImage(show.data, show.shape[1], show.shape[0],QtGui.QImage.Format_RGB888)
                self.label.setPixmap(QtGui.QPixmap.fromImage(showImage))  #往显示视频的Label里 显示QImage

    def show_cut_picture_result(self):
        for index,info in self.face_img_info.items():
            img = cv2.cvtColor(info, cv2.COLOR_BGR2RGB)  # 转换图像通道
            x, y, w, h = self.boxlist[index][1]
            cut_img = img[y-120:y+h,x-20:x+w+20]
            x = cut_img.shape[1]
            y = cut_img.shape[0]
            cut_img1 = np.array(cut_img)
            frame = QImage(cut_img1,x,y,x*3,QImage.Format_RGB888).scaled(210,190)
            pix = QPixmap.fromImage(frame)
            self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
            self.scene = QGraphicsScene()  # 创建场景
            self.scene.addItem(self.item)
            self.graphicsView.setScene(self.scene)
            self.graphicsView.show()
            self.img_res = cut_img1
        '''以下需要获取用户名称，以此作为文件名来保存用户的人脸数据---用户名.jpg'''
        picture_file_name = self.usr_name
        client_face_path = './client_face_data/' + str(picture_file_name) + '.jpg'
        client_face_picture = cv2.cvtColor(self.img_res,cv2.COLOR_BGR2RGB)
        cv2.imwrite(client_face_path,client_face_picture)
        # cv2.imencode('.jpg', img)[1].tofile("含有中文路径/xxx.jpg")

    def start_sorce(self):
        self.thread_start_btn = Thread(target=self.get_sorce)
        self.thread_start_btn.start()
        if self.graphicsView.scene() != None:
            print("==============")
            QMessageBox.information(self, '消息', '识别中，请耐心等待识别')
            while True:
                if self.mark == 1:
                    QMessageBox.information(self, '消息', '识别完成,即将为您展示结果')
                    self.sorce_to_graph()
                    self.show_skin_info()
                    self.show_recommend_product_info()
                    break
                else:
                    continue

    def get_sorce(self):
        if self.graphicsView.scene() == None:
            win32api.MessageBox(0, "请先录入人脸", "消息")
        else:
            transform = transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ])
            PIL_image = Image.fromarray(self.img_res)  # 这里ndarray_image为原来的numpy数组类型的输入
            img = transform(PIL_image)
            net = Nets.AlexNet().cuda()
            self.load_model(torch.load('./models/alexnet.pth', encoding='latin1'), net)
            net.eval()
            with torch.no_grad():
                img = img.unsqueeze(0).cuda(non_blocking=True)
                output = net(img).squeeze(1)
                output.cpu().detach().numpy()
                print(output[0])
                self.face_sorce = output
                ''' 这里存在一个问题，在子线程中不要设计matplotlib '''
                self.mark = 1

    def load_model(slef,pretrained_dict, new):
        model_dict = new.state_dict()
        # 1. filter out unnecessary keys
        pretrained_dict = {k: v for k, v in pretrained_dict['state_dict'].items() if k in model_dict}
        # 2. overwrite entries in the existing state dict
        model_dict.update(pretrained_dict)
        new.load_state_dict(model_dict)

    def sorce_to_graph(self):
        sorce = self.face_sorce
        sorce = round(float(str(sorce[0])[7:12]),2) - 1.00
        rate = 100.00/(4.75-1.00)
        value = round(sorce*rate,2)
        other_value = 100.00-value
        s = {'S0': 3}
        s_labels = list(sorted(s.keys()))
        s_fracs = [s.get(s_labels[i]) for i in range(len(s_labels))]
        text = 'sorce:' + str(value)
        election_data = { text : value, 'non-sorce': other_value}
        candidate = [key for key in election_data]
        votes = [value for value in election_data.values()]
        fig = plt.figure(figsize=(10, 10), dpi=100)
        plt.pie(votes, labels=candidate, colors=['c', 'w'], textprops={'fontsize': 39},
                labeldistance=1.05, wedgeprops={'linewidth': 1, 'edgecolor': "black"})
        plt.pie(s_fracs, radius=0.6,
                colors='w', wedgeprops={'linewidth': 1, 'edgecolor': "black"})
        plot_img_np = self.get_img_from_fig(fig)
        x = plot_img_np.shape[1]
        y = plot_img_np.shape[0]
        plot_img_np = np.array(plot_img_np)
        frame = QImage(plot_img_np, x, y, x * 3, QImage.Format_RGB888).scaled(552, 335)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView_11.setScene(self.scene)
        self.graphicsView_11.show()

    def show_skin_info(self):
        plt.rcParams['font.sans-serif'] = 'SimHei'
        plt.rcParams['axes.unicode_minus'] = False
        plt.style.use('ggplot')
        values = np.random.randint(0, 5, 5)
        feature = ['健康度', '干油性', '细腻度', '年轻度', '匀净度']
        feature = np.concatenate((feature, [feature[0]]))
        angles = np.linspace(0, 2 * np.pi, len(values), endpoint=False)
        values = np.concatenate((values, [values[0]]))
        angles = np.concatenate((angles, [angles[0]]))
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.plot(angles, values, 'o-', linewidth=2)
        ax.fill(angles, values, alpha=0.45)
        ax.set_thetagrids(angles * 180 / np.pi, feature)
        ax.set_ylim(0, 5)
        plt.title('肤质报告')
        ax.grid(True)
        plot_img_np = self.get_img_from_fig(fig)
        x = plot_img_np.shape[1]
        y = plot_img_np.shape[0]
        plot_img_np = np.array(plot_img_np)
        frame = QImage(plot_img_np, x, y, x * 3, QImage.Format_RGB888).scaled(552, 335)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView_7.setScene(self.scene)
        self.graphicsView_7.show()

    def show_recommend_product_info(self):
        a = np.random.randint(1, 6, 1)[0]
        file_name = './product_pic/' + str(a) + '.jpg'
        img = cv2.imread(file_name)  # 读取图像
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        x = img.shape[1]  # 获取图像大小
        y = img.shape[0]
        prod_info_img = np.array(img)
        frame = QImage(prod_info_img, x, y, x * 3, QImage.Format_RGB888).scaled(432, 335)
        pix = QPixmap.fromImage(frame)
        self.item = QGraphicsPixmapItem(pix)  # 创建像素图元
        self.scene = QGraphicsScene()  # 创建场景
        self.scene.addItem(self.item)
        self.graphicsView_8.setScene(self.scene)
        self.graphicsView_8.show()

    def get_img_from_fig(self,fig):
        buf = io.BytesIO()
        fig.savefig(buf, format="png", dpi=180)
        buf.seek(0)
        img_arr = np.frombuffer(buf.getvalue(), dtype=np.uint8)
        buf.close()
        img = cv2.imdecode(img_arr, 1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
    
class FC_ui(QMainWindow, FC_Ui_MainWindow):
    def __init__(self,parent=None):
        super(FC_ui, self).__init__(parent)
        self.setupUi(self)
        self.label.setPixmap(QPixmap("fc_criterion.jpg"))  # 我的图片格式为png.与代码在同一目录下
        self.label.setScaledContents(True)
        