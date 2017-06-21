import pyaudio
import numpy as np
from signalplotter import SignalPlotter

CHUNK = 2**11
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,
              frames_per_buffer=CHUNK)

sp = SignalPlotter(0.001,0.1) #change here for signal step and max time on the graph

signal = []
while True:
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    signal += list(data)
    
    if len(signal) > sp.numberOfSteps:
        sp.addAmp(signal)
        sp.draw()
        del signal[:]
        
stream.stop_stream()
stream.close()
p.terminate()
