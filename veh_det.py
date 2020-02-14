# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:24:30 2020

@author: joelg
"""
import cv2
import cvlib as cv
import matplotlib.pyplot as plt

def getVehs():
     cam1 = cv2.VideoCapture("3.avi")
     success, image = cam1.read()
     #if success:
          #cv2.imwrite("first_frame.jpg", image)
     cam1.release()
     bbox, label, conf = cv.detect_common_objects(image)
     print('Number of cars in the image is '+ str(label.count('car')))
     print('Number of buses in the image is '+ str(label.count('bus')))
     print('Number of motorcycle in the image is '+ str(label.count('motorcycle')))
     totveh = label.count('car') + label.count('bus') + label.count('motorcycle')
     totwei = label.count('car') + (label.count('bus')*3) + label.count('motorcycle')
     plt.imshow(image)
     plt.show()
     return ([label.count('car') ,label.count('bus'), label.count('motorcycle'), totveh, totwei])
     #return(label.count('car'))

#getVehs()7