from pcars.stream import PCarsStreamReceiver
from pyudmx import pyudmx
from time import *
import math


dev = pyudmx.uDMXDevice()
dev.open()
#print 'found '+dev.Device.serial_number
cv = [0 for v in range(0, 512)]



class MyPCarsListener(object):
    def handlePacket(self, data):
        # You probably want to do something more exciting here
        # You probably also want to switch on data.packetType
        # See listings in packet.py for packet types and available fields for each
        #print dir(data)
        #for i in range(len( data._data)):
            #print data._data[i]
        #print data._data['windDirectionY'],
        #print data._data.['windDirectionX']
        #print data._data
        
        #data._data['speed']
        #print data._data['steering']
        try:
            temp =int(data._data['speed'])
            temp=math.pow(temp,1.3)
            cv[0]=int(temp)
            steer=data._data['steering']

            if steer>0:
                #wind left
                cv[0]=cv[0]*(steer*.1)
            
            #cv[0] =int(data._data['throttle'])
            print data._data['steering'],' steering'
        except:
            print 'cant get speed'
        if cv[0]>254:
            cv[0]=254
        cv[0]=int(cv[0]+1)
        print cv[0]
        try:
            sent = dev.send_multi_value(1, cv)
            #print time.clock()
        except:
            print 'cant send dmx'
            #sent = dev.send_multi_value(1, cv)
        

    
            
        


listener = MyPCarsListener()
stream = PCarsStreamReceiver()
try:
    stream.addListener(listener)
    stream.start()
except:
    ''
