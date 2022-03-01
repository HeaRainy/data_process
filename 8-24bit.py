import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os

import sys
import shutil

path=r'C:\FILE\teeth\dataset_GT1/'
newpath=r'C:\FILE\teeth\dataset_GT1/'
def turnto24(path):
    files = os.listdir(path)
    files = np.sort(files)
    i=0
    for f in files:
        imgpath = path + f
        img=Image.open(imgpath).convert('RGB')
        dirpath = newpath
        file_name, file_extend = os.path.splitext(f)
        dst = os.path.join(os.path.abspath(dirpath), file_name + '.bmp')
        img.save(dst)

turnto24(path)
