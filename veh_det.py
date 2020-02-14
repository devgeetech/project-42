# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:24:30 2020

@author: joelg
"""

import cv2
import cvlib as cv
import matplotlib.pyplot as plt

def getCars():
     cam1 = cv2.VideoCapture(2)
     success, image = cam1.read()
     #if success:
          #cv2.imwrite("first_frame.jpg", image)
     cam1.release()
     bbox, label, conf = cv.detect_common_objects(image)
     print('Number of cars in the image is '+ str(label.count('car')))
     plt.imshow(image)
     plt.show()
     #return(label.count('car'))

getCars()