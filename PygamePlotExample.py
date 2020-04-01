import numpy as np
from pygameplotlib.pygameplot import plotsurf as ps
from pygameplotlib.pygameutils import py_handler as ph
from pygameplotlib.pygameutils import Button

a = ph(width=1000,height=730)

f = 50.0
T = 1/f
fs = 40*f
Ts = 1/fs

t = np.arange(0,50*T,Ts)

# create 4 plot objects
signal = ps(a.screen,500,350,xlabel='x[m]',ylabel='y(t)',xstep=5,xlim=[0,2*T])
spectrum = ps(a.screen,500,350,xlabel='x[m]',ylabel='y(t)',xstep=6,xlim=[0,100])

b = Button(a,width=100,height=20,x=750,y=100)

def getSpectrum(timeSignal):
    Y = np.fft.fft(y)
    Y = np.abs(Y)
    Y = Y[:len(Y)/2]
    fspec = np.linspace(0,fs/2,len(Y))
    return fspec,Y

backward = True
running = True
b1state = True
while running:

    bState = b.check_button()

    # oscillate frequency between 1 and -1
    if bState == True:
        if f <= 40:
            backward = False
        if f >= 60:
            backward = True
        if backward:   
            f -= 0.25
        if not(backward):   
            f += 0.25

    # update sine waves
    y = np.sin(2*np.pi*f*t)
    fspec,Y = getSpectrum(y)

    signal.plot(10,10,t,y)
    spectrum.plot(10,370,fspec,Y)

    running = a.py_update()
