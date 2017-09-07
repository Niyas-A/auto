import serial
import time

ser = serial.Serial('/dev/ttyACM0', baudrate = 9600, timeout = 1)
time.sleep(3)
numPoints = 17 #no.of values coming
dataList = [0]*numPoints

def getValues():
    
    arduinoOutput = ser.readline().decode().split(':')
    #print(arduinoOutput)
    #print(len(arduinoOutput))
    if(numPoints == len(arduinoOutput)):
        for i in range(0,numPoints-1):  
             arduinoOutput[i] = arduinoOutput[i].encode('ascii','ignore')
        arduinoOutput[numPoints-1] = arduinoOutput[numPoints-1].encode('ascii','ignore').split('\r\n')[0]
        return arduinoOutput
    else:
        return None   #Add NULL case


    #arduinoData = ser.readline().decode().split('\r\n')
    #return arduinoData[0].encode('ascii','ignore')


while(1):
        
        data = getValues()
	#for i in range(0,numPoints): 
            #dataList[i] = data[i]
       
        print(data)

    
