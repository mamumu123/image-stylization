from PIL import Image    # Pillow                    9.0.0
import pillow_avif       # pillow-avif-plugin        1.2.2
import os
#以上只是其中一个可用版本，并非必须
#必须先安装pip install pillow-avif-plugin才能使用


dir_avif = '_avif'
input_png = 'input_png'


for root, dirs, files in os.walk(dir_avif):
    for file in files:
        file_path = os.path.join(root, file)  # 获取文件的绝对路径
        out_path = os.path.join(input_png, file.replace("avif",'png'))  # 获取文件的绝对路径
        avif_img = Image.open(file_path)
        avif_img.save(out_path, 'PNG')