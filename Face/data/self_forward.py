import numpy as np
import os
import torch
import torch.nn as nn
import torchvision.transforms as transforms
from PIL import Image
import matplotlib.pyplot as plt
from torch.utils.data import Dataset
import Nets
import cv2
import time

def load_model(pretrained_dict, new):
    model_dict = new.state_dict()
    # 1. filter out unnecessary keys
    pretrained_dict = {k: v for k, v in pretrained_dict['state_dict'].items() if k in model_dict}
    # 2. overwrite entries in the existing state dict
    model_dict.update(pretrained_dict)
    new.load_state_dict(model_dict)

def cv_show(name,img):
    cv2.namedWindow(name,0)
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    start_time = time.time()
    image = './3.jpg'
    img = Image.open(image).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]), ])

    img = transform(img)
    # net definition
    net = Nets.AlexNet().cuda()
    # net = Nets.ResNet(block = Nets.BasicBlock, layers = [2, 2, 2, 2], num_classes = 1).cuda()
    # load pretrained model
    load_model(torch.load('./models/alexnet.pth',encoding='latin1'), net)
    # load_model(torch.load('./models/resnet18.pth'), net)
    # evaluate
    net.eval()

    with torch.no_grad():
        img = img.unsqueeze(0).cuda(non_blocking=True)
        output = net(img).squeeze(1)
        output.cpu().detach().numpy()
        print(output)
        print(output[0])
    end_time = time.time()
    time_sum = start_time - end_time  # 计算的时间差为程序的执行时间，单位为秒/s
    print(time_sum)

    aaa = cv2.imread('./3.jpg')
    text = 'Sorce:'+ str(output[0])[7:12]
    cv2.putText(aaa,text,(0,26),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),1)
    cv_show('result',aaa)


