import os
import shutil

path = "C:\\FILE\\teeth\\health\\shuizhong\\total"  # 抽取的源文件夹，无需以\结尾


def img_extract(file_path):
    i = 1  # 重命名的起始编号
    destination = 'C:\\FILE\\teeth\\health\\shuizhong\\total\\input\\'  # 抽取的目的文件夹
    for root, dirs, files in os.walk(file_path):
        for file in files:
            if file.find('img.png') != -1:  # 判断是否为Thumbnails开头的缩略图文件
                #src_extension = os.path.splitext(file)[-1]  # 获取源文件后缀
                shutil.copyfile(root + '\\' + file, destination + '%d' % i + '.png')  # 复制文件，重命名
                print('Copyed and renamed the %d file' % i)
                i += 1


# 主函数
if __name__ == '__main__':
    img_extract(path)
