import numpy as np
from pygameplotlib.pygameplot import plotsurf as ps
from pygameplotlib.pygameutils import py_handler as ph
from pygameplotlib.pygameutils import tbutton

a = ph()

# create 4 plot objects
signal_1 = ps(a.screen,670,220,xlabel='x[m]',ylabel='y(x)',xstep=5,xlim=[0,5])
signal_2 = ps(a.screen,670,550,xlabel='x[m]',ylabel='y(x)',xstep=5)
signal_3 = ps(a.screen,300,170,xstep=3)

b1 = tbutton(a,width=200,height=50,x=750,y=10)

# create x vector
x = np.linspace(-2*np.pi,2*np.pi,400)
freq = 1.0

backward = True
running = True
b1state = True
while running:

    # oscillate frequency between 1 and -1
    if freq <= -1:
        backward = not(backward)
    if freq >= 1:
        backward = not(backward)
    if backward:   
        freq -= 0.005
    if not(backward):   
        freq += 0.005
    
    # update sine waves
    y1 = 2.5*np.sin(2*np.pi*x)+2*np.sin(2*np.pi*0.5*freq*x)+5
    y2 = 0.5*np.sin(2*np.pi*0.25*x)+2*np.sin(2*np.pi*freq*x)+3
    y3 = 5*np.sin(2*np.pi*0.1*x)+2*np.sin(3*2*np.pi*freq*x)+3

    # plot all graphs
    if(b1state):
        signal_1.plot(10,10,x,y2)
        signal_2.plot(10,240,x,y1)
        signal_3.plot(690,620,x,y3)
    if(b1state == False):
        signal_1.plot(10,10,x,y1)
        signal_2.plot(10,240,x,y2)
        signal_3.plot(690,620,x,y3)

    b1state = b1.check_button()
    running = a.py_update()
