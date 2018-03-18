#给训练集和测试集补白
import os
from argparse import ArgumentParser
from PIL import Image

Image_Width = 299
Image_Height = 299

if __name__ == '__main__':
    argparser = ArgumentParser()
    argparser.add_argument('source_folder', help='input the source folder path')
    argparser.add_argument('destination_folder', help='input the desination folder path')
    args = argparser.parse_args()
    source_folder = args.source_folder
    destination_folder = args.destination_folder
    index = 0
    #os.walk()返回的root_folder实际上是把当前目录的每一级子目录当做根目录进行遍历
    for root_folder1, sub_folder1, file_list1 in os.walk(source_folder):
        destination_folder_path = ''
        if index > 0:
            destination_folder_path = root_folder1.replace(source_folder, destination_folder)
            os.mkdir(destination_folder_path)
        for file_name1 in file_list1:
            source_file_path = root_folder1 + os.sep + file_name1
            if source_file_path.find('jpg') > -1:
                destination_file_path = destination_folder_path + os.sep + file_name1
                target = Image.new('RGB', (Image_Width, Image_Height), color=0xFFFFFF)
                img = Image.open(source_file_path)
                width = img.size[0]
                height = img.size[1]
                if width > Image_Width:
                    height = int(Image_Width * 1.0 / width * height)
                    width = Image_Width
                    img = img.resize((width, height))
                if height > Image_Height:
                    width = int(Image_Height * 1.0 / height * width)
                    height = Image_Height
                    img = img.resize((width, height))
                x = int((Image_Width - width)/2)
                y = int((Image_Height - height)/2)
                print(width, height, x, y)
                target.paste(img, (x, y, x + width, y + height))
                target.save(destination_file_path, quality = 100)
        index += 1