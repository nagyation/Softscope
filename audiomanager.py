import pyaudio
import numpy as np
from signalplotter import SignalPlotter

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)
sp = SignalPlotter(0.0001,1)
signal = []
while True:#for i in range(int(10*44100/1024)): #go for a few seconds
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak=np.average(data)#*2
    signal += list(data)
    print ("length of the data" ,len(data))
    if len(signal) > sp.numberOfSteps:
        sp.addAmp(signal)
        sp.draw()
        del signal[:]
    bars="#"*int(50*peak/2**16)
    print("%05d %s"%(peak,bars))

stream.stop_stream()
stream.close()
p.terminate()
