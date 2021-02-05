import fygen
fy = fygen.FYGen('/dev/ttyUSB0', debug_level=1)

#fy = fygen.FYGen(debug_level=1)  # Same thingfy.set(
#  channel=fygen.CH1,
#  enable=True,
#  wave='sin',
#  freq_hz=1e6,
#  volts=5)
#fy.set(1, wave='sin', freq_hz=50, volts=2.50, enable=False)
#fy.set(0, wave='sin', freq_hz=10e6, volts=2.50, offset_volts=0, phase_degrees=0, enable=True)

import math  # if needed
fy = fygen.FYGen()
wave_data = [math.sin(t * math.pi * 2.0 / 8192.0) for t in range(8192)]
fy.set_waveform(1, values=wave_data)
fy.set(0, wave='arb1')
