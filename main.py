#import serial
import lightcontrol
import time
from random import randrange
import veh_det

state = [0,0,0,0]
vehicles = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
timeWeights = [0, 0, 0, 0]
j=0
ways = 4
while j<1:
    j=j+1  
    for i in range(0,ways):

        #[0]=veh_det.getVehs()
        #print("cars in image yo: " + str(cars[0]))
        #cars[0]=cars[1]+randrange(5)
        vehicles[0]=veh_det.getVehs()
        vehicles[1][0]=vehicles[1][0]+randrange(3)
        vehicles[2][0]=vehicles[2][0]+randrange(4)
        vehicles[3][0]=vehicles[3][0]+randrange(2)
        
        totveh = vehicles[0][3] + vehicles[1][3] + vehicles[2][3] + vehicles[3][3]
        #timeWeights[0] = vehicles[0][4]
        timeWeights[0] = 5    #CHANGE!!!!!!!
        timeWeights[1] = timeWeights[1]+randrange(3)
        timeWeights[2] = timeWeights[2]+randrange(3)
        timeWeights[3] = timeWeights[3]+randrange(3)
        
        if(totveh > 0):
             retime = lightcontrol.control(timeWeights)
             state[i] = 2
             lightcontrol.light(state)
             time.sleep(retime[i])
             timeWeights[i]=timeWeights[i]-(retime[i]*2/6)
             state[i] = 1
             lightcontrol.light(state)
             if retime[i] == 0:
                 time.sleep(0)
             else:
                 time.sleep(3)
             state[i] = 0
             lightcontrol.light(state)     
        else:
             state = [3, 3, 3, 3]
             lightcontrol.light(state)

        #retime = lightcontrol.control([randrange(5),randrange(5),randrange(5),randrange(5)])
      
