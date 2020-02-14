#import serial

def control(veh, totwei, maxlim):

    minlim = 0
    #avgtime = 6
    #lanes = 2
    terrainFactor = [1, 1, 1.5, 1]
    ways = len(veh) #no of lanes
    times = []
    time = 0
    for i in range(0,ways):
        pretime = ((veh[i]*terrainFactor[i])/totwei)*maxlim
        if(pretime%5 != 0):
             time = pretime + (5-(pretime%5))
        else:
             time=pretime
        if time>maxlim: 
            allotime = maxlim
        elif time<minlim:
            allotime=minlim
        else:
            allotime=time
        times.append(allotime)
    print(times)
    return times

def light(state):
    output = []
    for i in range(0,len(state)):
        if state[i] == 2:
            output.append('g')
        elif state[i] == 1:
            output.append('y')
        else:
            output.append('r')
    print(output)