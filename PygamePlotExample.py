
    ######################
   #  ExamplePygamePlot #
  #  by -=avokado0h=-  #
 ######################

import numpy as np
from pygameplotlib.PygamePlot import Plot as plt
from pygameplotlib.PygameUtils import Settings
from pygameplotlib.PygameUtils import showText

a = Settings(width=1030,height=400)

f = 40.0
T = 1/f
fs = 40*f
Ts = 1/fs

t = np.arange(0,30*T,Ts)

signal = plt(a,500,350,xlabel='t [s]',ylabel='y(t)',
        xstep=5,caption='Signal',xlim=[0,5*T])
spectrum = plt(a,500,350,xlabel='frequency [Hz]',ylabel='|Y|',
        xstep=5,xlim=[30,70],ylim=[0,300],caption='Spectrum')
window = plt(a,350,350)

hamming = np.hanning(len(t))

def getSpectrum(s):
    s = s * hamming
    s = np.append(s,np.zeros(len(s)*4))
    Y = np.fft.fft(s)
    Y = np.abs(Y)
    Y = Y[:len(Y)/2]
    fspec = np.linspace(0,fs/2,len(Y))
    return fspec,Y

d = 1
running = True
while running:

    if f <= 40: d = 1
    if f >= 60: d = -1
    f += d*0.25 

    y = np.sin(2*np.pi*f*t)
    fspec,Y = getSpectrum(y)

    signal.Show(10,10,t,y,0,'green')
    spectrum.Show(520,10,fspec,Y,0,'blue')

    signalTxt = 'y(t) = sin(2*pi*{0:.2f}*t)'.format(f)
    showText(a,150,365,signalTxt,20)
    showText(a,925,370,'FPS: {0:.2f}'.format(a.fps),15)

    running = a.Update()
