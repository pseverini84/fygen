import math  # if needed
import fygen

fy = fygen.FYGen('/dev/ttyUSB3', debug_level=1)
#fy = fygen.FYGen(debug_level=1)  # Same thingfy = fygen.FYGen()

fy.set(0, wave='dc')#en verdad esta shifteado en el dds (esto equivale al cmos)
fy.set(0, freq_hz=50)
#fy.set(0, volts=400e-3)
fy.set(0, volts=411e-3)
fy.set(0, duty_cycle=0.0001)
fy.set(0, phase_degrees=90)
fy.set(0, enable=True)
