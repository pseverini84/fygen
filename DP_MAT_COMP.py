import serial
import time
import math  # if needed
import fygen
from scipy.io import loadmat

fileName='reg_unificados_ace.mat'
dp=loadmat(fileName)
#dp.keys()
label_pf=list(dp.keys())[3]
type(dp[label_pf]),dp[label_pf].shape
type(dp[label_pf][0][0]),dp[label_pf][0][0].shape

fy = fygen.FYGen('/dev/ttyUSB3', debug_level=1)
#fy = fygen.FYGen(debug_level=1)  # Same thingfy = fygen.FYGen()

fy.set(0, wave='dc')#en verdad esta shifteado en el dds (esto equivale al cmos)
fy.set(0, freq_hz=50)

ser = serial.Serial('/dev/ttyUSB2', 115200, timeout=0.5)
command=b"\x15\x00\x0A\x02"

f = open(fileName + '.log.comp','w') 
f.write('peak;degree\n')
f.close()

for y in range(dp[label_pf].shape[0]):
    #print(dp['cor_pf'][y][0]) 
    #print(dp['cor_pf'][y][1])
    fy.set(0, enable=False)
    if(dp[label_pf][y][1]>=0):
        fy.set(0, volts=dp[label_pf][y][1])
        fy.set(0, duty_cycle=0.0001)
        fy.set(0, phase_degrees=dp[label_pf][y][0])
    else:
        fy.set(0, volts=(dp[label_pf][y][1])*-1)
        fy.set(0, duty_cycle=0.9999)
        fy.set(0, phase_degrees=(dp[label_pf][y][0])+0.01)
        
    fy.set(0, enable=True)
    #fy.set_modulation(fygen.MODULATION_BURST, fygen.TRIGGER_CH2, 1)
    time.sleep(0.1)
    ser.write(command)
    time.sleep(0.1)
    rx=ser.read(10)
    print(rx)    
    degree=(rx[4]*256)+rx[3]
    volts=(rx[2]*256)+rx[1]
    if(volts>=32768):
        volts-=65536
    print(y)    
    print(volts)  
    print(degree)  
    f = open(fileName + '.log','a') 
    f.write(str(volts) + ';' + str(degree) + '\n')
    f.close()


