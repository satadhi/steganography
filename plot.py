import matplotlib.pyplot as plt
import numpy as np
import wave
import sys


spf = wave.open('opera.wav','r')
#spf2 = wave.open('opera_new.wav','r')

#Extract Raw Audio from Wav File
signal = spf.readframes(-1)
print(signal)
signal = np.fromstring(signal, 'Int16')
for i in signal:
    print(signal)
#signal2 = spf2.readframes(-1)
#signal2 = np.fromstring(signal2, 'Int16')

fs = spf.getframerate()

#If Stereo
if spf.getnchannels() == 2:
    print ('Just mono files')
    sys.exit(0)


Time=np.linspace(0, len(signal)/fs, num=len(signal))

plt.figure(1)
plt.title('Signal Wave...')
plt.plot(Time,signal,'r')
#plt.plot(Time,signal2,'b')

plt.show()
