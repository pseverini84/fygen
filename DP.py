import math  # if needed
import fygen

fy = fygen.FYGen('/dev/ttyUSB0', debug_level=1)
fy = fygen.FYGen(debug_level=1)  # Same thingfy = fygen.FYGen()
wave_data = [math.sin(t * math.pi * 2.0 * 10 / 8192.0) * math.e**(-t/2*10/8192.0) for t in range(8192)]
fy.set_waveform(1, values=wave_data)
fy.set(0, wave='arb1')
fy.set(0, freq_hz=10e6/10)
fy.set(0, volts=400e-3)
fy.set(0, enable=True)
