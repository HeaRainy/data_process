import os

from PIL import Image

path_img = r'C:\FILE\teeth\health\shuizhong\total\input/'
img_dir = os.listdir(path_img)
print(img_dir)
print(len(img_dir))
for i in range(len(img_dir)):
    # 根据图片名称提取id,方便重命名
    id = str((img_dir[i].split('.')[0]))
    img = Image.open(path_img + '/' + img_dir[i])
    size_img = img.size
    #print(size_img)
    # 准备将图片切割成4张小图片,这里后面的2是开根号以后的数，比如你想分割为9张，将2改为3即可
    weight = int(size_img[0] // 2)
    height = int(size_img[1] // 2)
    for j in range(2):
        for k in range(2):
            box = (weight * k, height * j, weight * (k + 1), height * (j + 1))
            region = img.crop(box)
            # 输出路径
            region.save('C:\FILE/teeth\health\shuizhong/total\input/{}-{}{}.png'.format(id, j, k))
