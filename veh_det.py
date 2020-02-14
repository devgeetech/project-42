# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:24:30 2020

@author: joelg
"""
import cv2
import cvlib as cv
import matplotlib.pyplot as plt

def getVehs():
     cam1 = cv2.VideoCapture("1.avi")
     success1, image1 = cam1.read()
     cam1.release()
     plt.imshow(image1)
     plt.show()
     
     cam2 = cv2.VideoCapture("2.avi")
     success2, image2 = cam2.read()
     cam2.release()
     plt.imshow(image2)
     plt.show()
     
     cam3 = cv2.VideoCapture("3.avi")
     success3, image3 = cam3.read()
     cam3.release()
     plt.imshow(image3)
     plt.show()
     
     cam4 = cv2.VideoCapture("4.avi")
     success4, image4 = cam4.read()
     cam4.release()
     plt.imshow(image4)
     plt.show()

     bbox, label, conf = cv.detect_common_objects(image1)
     print('Number of cars in the image is '+ str(label.count('car')))
     print('Number of buses in the image is '+ str(label.count('bus')))
     print('Number of motorcycle in the image is '+ str(label.count('motorcycle')))
     totveh = label.count('car') + label.count('bus') + label.count('motorcycle')
     totwei = label.count('car') + (label.count('bus')*3) + label.count('motorcycle')

     return ([label.count('car') ,label.count('bus'), label.count('motorcycle'), totveh, totwei])
     #return(label.count('car'))

getVehs()