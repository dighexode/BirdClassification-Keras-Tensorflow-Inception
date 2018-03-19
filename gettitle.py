import cv2
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from glob import glob
import os

SAVE_PATH = './DATA 100 4th_title/'
image_dirs = glob('./DATA 100 4th/*')
for image_dir in image_dirs:
    image_paths = glob(image_dir + '/*')
    save_dir = SAVE_PATH + image_dir.split('\\')[-1]
    print(save_dir)
    os.mkdir(save_dir)
    for image_path in image_paths:
        image_name = image_path.split('\\')[-1]
        if image_name.find('.jpg') > -1:
            #print(image_name)
            image = cv2.imread(image_path)

            h,w = image.shape[0:2]
            roi = image[:int(h*.35),:,:]

            '''showroi = cv2.cvtColor(roi, cv2.COLOR_BGR2RGB)
            showimg = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            plt.imshow(showroi)
            plt.show()'''
            print(image_name)
            cv2.imwrite(save_dir + '\\' + image_name, roi)