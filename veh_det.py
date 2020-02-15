# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 19:24:30 2020

@author: joelg
"""
import cv2
import cvlib as cv
import matplotlib.pyplot as plt
#import numpy as numm

def getVehs(frame_no):
     cam1 = cv2.VideoCapture("1.mp4")
     cam1.set(1, frame_no);
     success1, image1 = cam1.read()
     cam1.release()
     #plt.imshow(numm.image2np(image1.data))
     plt.imshow(image1)
     plt.show()
     
     cam2 = cv2.VideoCapture("2.mp4")
          
     #cam2.set(1,frame_no);
     cam2.set(1, frame_no);
     success2, image2 = cam2.read()
     cam2.release()
     plt.imshow(image2)
     plt.show()
     
     cam3 = cv2.VideoCapture("3.mp4")
     cam3.set(1,frame_no);
     success3, image3 = cam3.read()
     cam3.release()
     plt.imshow(image3)
     plt.show()
     
     cam4 = cv2.VideoCapture("4.mp4")
     cam4.set(1,frame_no);
     success4, image4 = cam4.read()
     cam4.release()
     plt.imshow(image4)
     plt.show()

     bbox, label1, conf = cv.detect_common_objects(image1)
     bbox, label2, conf = cv.detect_common_objects(image2)
     bbox, label3, conf = cv.detect_common_objects(image3)
     bbox, label4, conf = cv.detect_common_objects(image4)
     
     way1 = [label1.count('car'), label1.count('bus'), label1.count('motorcycle')]
     way2 = [label2.count('car'), label2.count('bus'), label2.count('motorcycle')]
     way3 = [label3.count('car'), label3.count('bus'), label3.count('motorcycle')]
     way4 = [label4.count('car'), label4.count('bus'), label4.count('motorcycle')]
     totway1veh = label1.count('car') + label1.count('bus') + label1.count('motorcycle')
     totway2veh = label2.count('car') + label2.count('bus') + label2.count('motorcycle')
     totway3veh = label3.count('car') + label3.count('bus') + label3.count('motorcycle')
     totway4veh = label4.count('car') + label4.count('bus') + label4.count('motorcycle')
     
     totway1wei = label1.count('car') + (label1.count('bus')*3) + label1.count('motorcycle')
     totway2wei = label2.count('car') + (label2.count('bus')*3) + label2.count('motorcycle')
     totway3wei = label3.count('car') + (label3.count('bus')*3) + label3.count('motorcycle')
     totway4wei = label4.count('car') + (label4.count('bus')*3) + label4.count('motorcycle')
     #print('Number of cars in the image is '+ str(label.count('car')))
     #print('Number of buses in the image is '+ str(label.count('bus')))
     #print('Number of motorcycle in the image is '+ str(label.count('motorcycle')))
     totveh = totway1veh + totway2veh + totway3veh + totway4veh
     totwei = totway1wei + totway2wei + totway3wei + totway4wei  
     
     ways = [way1, way2, way3, way4, totveh, totwei]

     return (ways)
     #return(label.count('car'))

#getVehs()