#import serial
import lightcontrol
import time
from random import randrange
import veh_det

state = [0,0,0,0]
cars = [0, 0, 0, 0]
ways = 4
while True:
    for i in range(0,ways):

        cars[0]=veh_det.getCars()
        print("cars in image yo: " + str(cars[0]))
        cars[1]=cars[1]+randrange(3)
        cars[2]=cars[2]+randrange(4)
        cars[3]=cars[3]+randrange(2)

        #retime = lightcontrol.control([randrange(5),randrange(5),randrange(5),randrange(5)])
        retime = lightcontrol.control(cars)
        state[i] = 2
        lightcontrol.light(state)
        time.sleep(retime[i])
        cars[i]=cars[i]-(retime[i]*2/6)
        state[i] = 1
        lightcontrol.light(state)
        if retime[i] == 0:
            time.sleep(0)
        else:
            time.sleep(5)
        state[i] = 0
        lightcontrol.light(state)
