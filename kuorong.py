# -*- coding: utf-8 -*-

import cv2
import numpy as np
import os.path
import copy

#y方向缩放
from PIL import ImageEnhance
from PIL.Image import Image
from numpy import array


def yre(image):
    w = image.width
    h = image.height
    out_ww = image.resize((w, h + 40))
    out_ww_1 = np.array(out_ww)
    out_w_2 = out_ww_1[30:(h - 10), 0:w]  # 开始的纵坐标，开始的横坐标
    out_w_2 = Image.fromarray(out_w_2)
    return  out_w_2

#x方向缩放
def xre(image):
    w = image.width
    h = image.height
    out_hh = image.resize((w + 80, h))  # 拉伸成宽为w的正方形,width,height
    # out_hh.show()
    out_hh_1 = array(out_hh)
    out_h_2 = out_hh_1[0:h, 40:(w + 40)]
    out_h_2 = Image.fromarray(out_h_2)
    return out_h_2

#y方向平移


# 椒盐噪声
def SaltAndPepper(src, percetage):
    SP_NoiseImg = src.copy()
    SP_NoiseNum = int(percetage * src.shape[0] * src.shape[1])
    for i in range(SP_NoiseNum):
        randR = np.random.randint(0, src.shape[0] - 1)
        randG = np.random.randint(0, src.shape[1] - 1)
        randB = np.random.randint(0, 3)
        if np.random.randint(0, 1) == 0:
            SP_NoiseImg[randR, randG, randB] = 0
        else:
            SP_NoiseImg[randR, randG, randB] = 255
    return SP_NoiseImg


# 高斯噪声
def addGaussianNoise(image, percetage):
    G_Noiseimg = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    G_NoiseNum = int(percetage * image.shape[0] * image.shape[1])
    for i in range(G_NoiseNum):
        temp_x = np.random.randint(0, h)
        temp_y = np.random.randint(0, w)
        G_Noiseimg[temp_x][temp_y][np.random.randint(3)] = np.random.randn(1)[0]
    return G_Noiseimg


# 昏暗
def darker(image, percetage=0.9):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get darker
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = int(image[xj, xi, 0] * percetage)
            image_copy[xj, xi, 1] = int(image[xj, xi, 1] * percetage)
            image_copy[xj, xi, 2] = int(image[xj, xi, 2] * percetage)
    return image_copy


# 亮度
def brighter(image, percetage=1.5):
    image_copy = image.copy()
    w = image.shape[1]
    h = image.shape[0]
    # get brighter
    for xi in range(0, w):
        for xj in range(0, h):
            image_copy[xj, xi, 0] = np.clip(int(image[xj, xi, 0] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 1] = np.clip(int(image[xj, xi, 1] * percetage), a_max=255, a_min=0)
            image_copy[xj, xi, 2] = np.clip(int(image[xj, xi, 2] * percetage), a_max=255, a_min=0)
    return image_copy


# 旋转
def rotate(image, angle, center=None, scale=1.0):
    (h, w) = image.shape[:2]
    # If no rotation center is specified, the center of the image is set as the rotation center
    if center is None:
        center = (w / 2, h / 2)
    m = cv2.getRotationMatrix2D(center, angle, scale)
    rotated = cv2.warpAffine(image, m, (w, h))
    return rotated


# 翻转
def flip(image):
    flipped_image = np.fliplr(image)
    return flipped_image

#改变锐度
def shapness(image):
    enh_sha = ImageEnhance.Sharpness(image)
    sharpness = 3.0
    image_sharp = enh_sha.enhance(sharpness)
    return image_sharp

# 图片文件夹路径
#file_dir = r'C:\SOFTWARE\ANACONDA\envs\Unet\Zero-DCE-master\Zero-DCE_code\data\/'
out_dir = r'C:\FILE\teeth\health\shuizhong\total\mask/'
for img_name in os.listdir(out_dir):
    img_path = out_dir + img_name
    img = cv2.imread(img_path)
    # cv2.imshow("1",img)
    # cv2.waitKey(5000)
    #print(img_name)


    #镜像
    #flipped_img = flip(img)
    #cv2.imwrite(out_dir + img_name[0:-4] + '_fli.bmp', flipped_img)



    # 旋转
    rotated_45 = rotate(img, 45)
    cv2.imwrite(out_dir + img_name[0:-4] + '_r45.bmp', rotated_45)
    rotated_90 = rotate(img, 90)
    cv2.imwrite(out_dir + img_name[0:-4] + '_r90.bmp', rotated_90)
    rotated_135 = rotate(img, 135)
    cv2.imwrite(out_dir + img_name[0:-4] + '_r135.bmp', rotated_135)
    rotated_180 = rotate(img, 180)
    cv2.imwrite(out_dir + img_name[0:-4] + '_r180.bmp', rotated_180)


'''
    #改变锐度
    shapned_img = shapness(img)
    cv2.imwrite(file_dir + img_name[0:-4] + '_fli.jpg', shapned_img)



    # 增加噪声
    # img_salt = SaltAndPepper(img, 0.3)
    # cv2.imwrite(file_dir + img_name[0:7] + '_salt.jpg', img_salt)
    img_gauss = addGaussianNoise(img, 0.3)
    cv2.imwrite(file_dir + img_name[0:-4] + '_noise.jpg', img_gauss)

    # 变亮、变暗
    img_darker = darker(img)
    cv2.imwrite(file_dir + img_name[0:-4] + '_darker.jpg', img_darker)
    img_brighter = brighter(img)
    cv2.imwrite(file_dir + img_name[0:-4] + '_brighter.jpg', img_brighter)

    blur = cv2.GaussianBlur(img, (7, 7), 1.5)
    #      cv2.GaussianBlur(图像，卷积核，标准差）
    cv2.imwrite(file_dir + img_name[0:-4] + '_blur.jpg', blur)
'''
