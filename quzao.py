import os

import cv2
import cv2 as cv
from matplotlib import pyplot as plt

import cv2
from numba import jit
import os

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.fftpack as fft
# %matplotlib inline
# %matplotlib QT5


filePath = 'data/result/'
outpath = 'data/quzao/'
file_list = os.listdir(filePath)

for file_name in file_list:
    impath = filePath + file_name
    img = cv.imread(impath)

    dst = cv.fastNlMeansDenoising(img, None, 20, 7, 21)
    #dst = cv2.medianBlur(img,1)

    print(file_name)
    cv.imwrite(outpath + file_name, dst)
















