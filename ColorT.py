# -*- coding: utf-8 -*-
import os
import tkinter.filedialog
from tkinter import *

import matplotlib.image as mpimg
#import cv2
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image
from pylab import *

slask=1
while(slask):
    #pic_pt = input("Please enter the name of picture(jpg):")
    root = tkinter.Tk()
    root.withdraw()
    pic_pt = tkinter.filedialog.askopenfilename()
    #print(pic_pt)
    if pic_pt == "":
        sys.exit()
    num_change = int(input("Please enter the choice: \n 1.Gray \n 2.Black or white \n 3.Blue red \n 4.Painting[+width] \n Please enter your choice:"))
    #读取图片并转为数组
    im = array(PIL.Image.open(pic_pt))
    img = PIL.Image.open(pic_pt).convert('LA')
    a = np.asarray(PIL.Image.open(pic_pt).convert('L'))#.convert是变成黑白的
    grad = np.gradient(a)
    grad
    grad_x, grad_y = grad
    if num_change == 1:
        img.show()
        #goto.begin
    elif num_change == 2:
        # In[*]
        ##b=255-a#在对应的颜色通道减去他自己变成黑白底片的效果
        ##im=Image.fromarray(b.astype('uint8'))
        ##im.show()

        # In[*]
        ##c=(100/255)*a+150#区间变换,颜色比较淡的灰度的图片
        ##im=Image.fromarray(c.astype('uint8'))
        ##im.show()

        # In[*]
        d=255*(a/255)**2#像素平方,颜色比较深的图
        im=PIL.Image.fromarray(d.astype('uint8'))
        im.show()
        #goto.begin
    elif num_change == 3:
        #红色通道
        r = im[:,:,0]
        #交换红蓝通道并显示
        im[:,:,0] = im[:,:,2]
        im[:,:,2] = r
        imshow(im)
        show()
        #goto.begin
    elif num_change == 4:
        depth = 10                  # (0-100)
        grad = np.gradient(a)             #取图像灰度的梯度值
        grad_x, grad_y =grad               #分别取横纵图像梯度值
        grad_x = grad_x*depth/100.
        grad_y = grad_y*depth/100.
        A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
        uni_x = grad_x/A
        uni_y = grad_y/A
        uni_z = 1./A

        vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
        vec_az = np.pi/4.                    # 光源的方位角度，弧度值
        dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
        dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
        dz = np.sin(vec_el)              #光源对z 轴的影响

        b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
        b = b.clip(0,255)

        im =PIL.Image.fromarray(b.astype('uint8'))  #重构图像
        im.show()
        # In[*]
        #im.save("手绘.jpg")
    else:
        depth = num_change - 400                  # (0-100)
        grad = np.gradient(a)             #取图像灰度的梯度值
        grad_x, grad_y =grad               #分别取横纵图像梯度值
        grad_x = grad_x*depth/100.
        grad_y = grad_y*depth/100.
        A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
        uni_x = grad_x/A
        uni_y = grad_y/A
        uni_z = 1./A

        vec_el = np.pi/2.2                   # 光源的俯视角度，弧度值
        vec_az = np.pi/4.                    # 光源的方位角度，弧度值
        dx = np.cos(vec_el)*np.cos(vec_az)   #光源对x 轴的影响
        dy = np.cos(vec_el)*np.sin(vec_az)   #光源对y 轴的影响
        dz = np.sin(vec_el)              #光源对z 轴的影响

        b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #光源归一化
        b = b.clip(0,255)

        im = PIL.Image.fromarray(b.astype('uint8'))  #重构图像
        im.show()
        # In[*]
        #im.save("手绘.jpg")
