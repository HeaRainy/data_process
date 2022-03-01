# Written by Tian
# 2019年11月19日 20点41分
"""
 Resize images by Batch
"""
from PIL import Image
import os

Files_path = r"C:\FILE\teeth\health\shuizhong\total\mask1"
image_list = os.listdir(Files_path)

for image_name in image_list:
        image_path = os.path.join(Files_path, image_name)
        img = Image.open(image_path)
        print(img)

        x_s = 256
        y_s = 256

        Resize_image = img.resize((x_s, y_s), Image.ANTIALIAS)

        Resize_out_path = r"C:\FILE\teeth\health\shuizhong\total\mask"

        #Resize_image.save(Resize_out_path + '/' + str(os.listdir(Files_path)[i]) + '/' + str(image_name))
        Resize_image.save(Resize_out_path + '/' + str(image_name))