# Project 42: ADAPTIVE TRAFFIC LIGHT ARCHITECTURE

## Initialization:
*	Write the latest raspbian OS in the SD card (Raspbian-Lite should suffice) (ref: https://www.raspberrypi.org/documentation/installation/installing-images/)
*	The code uses Rpi.GPIO instead of the new GPIO zero (make sure your os supports it)
*	Install python3 if it’s not pre-installed (ref: https://www.circuitbasics.com/how-to-write-and-run-a-python-program-on-the-raspberry-pi/)
*	Install Git (Ref: https://raspberrypi.stackexchange.com/questions/8658/can-i-install-git-on-raspbian)
*	Clone the project-42 repo (Run this in terminal: 
   $ git clone http://github.com/devgeetech/project-42 
*   If you are using video files as camera input, place the 4 video files in the root folder.

## Configuration:
*	The pin[] array (in lightcontrol.py) has the list of GPIOs (Physical naming convention). In the order as follows
    *	3: Light-Post1, Red
    *	5: Light-Post1, Yellow
    *	7: Light-Post1, Green
    *	8: Light-Post2, Red
    *	10: Light-Post2, Yellow
    *	11: Light-Post2, Green
    *	12: Light-Post3, Red
    *	13: Light-Post3, Yellow
    *	15: Light-Post3, Green
    *	16: Light-Post4, Red
    *	18: Light-Post4, Yellow
    *	19: Light-Post4, Green
*	You can configure it by changing the pin[] array accordingly
*	Connect the lights through relays or any required control circuitry according to the applications
*	Install OpenCV, cvlib, and matplotlib 

##	References:
*	https://tutorials-raspberrypi.com/installing-opencv-on-the-raspberry-pi/
*	https://raspberrypi.stackexchange.com/questions/15420/how-to-install-python3-matplotlib-on-raspi/15457

## Running:
*	Run main.py in the project folder.
