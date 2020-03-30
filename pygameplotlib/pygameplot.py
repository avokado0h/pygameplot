
   ####################
  # pygameplotlib.py # 
 # by -=avokado0h=- #
####################

import pygame
import numpy as np
from pygameutils import colors

# defining colors

pygame.font.init()
myfont = pygame.font.SysFont('DejaVu Sans Mono', 16)


class plotsurf():
    def __init__(self,s_surf,w,h,xlabel='',ylabel='',
            xlim=[],ylim=[],ystep=3,xstep=3):
        self.w = w
        self.h = h
        # surface to draw plotsurface on 
        self.s_surf = s_surf
        # plotsurface to draw graphsurface on
        self.p_surf = pygame.Surface((w,h))
        # graphsurface
        self.g_surf = None
        self.xy_graph = []
        self.params_set = False
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.xlim = xlim
        self.ylim = ylim
        self.ystep = ystep
        self.xstep = xstep
        self.c = colors()

    def plot(self,x,y,xve,yve):
        self.p_surf.fill(self.c.bg1)
        self.draw_axis(xve,yve)
        self.draw_graph(xve,yve)
        self.s_surf.blit(self.p_surf,(x,y))

    def draw_axis(self,xve,yve):
        # create x/y-label surface
        xlabel = myfont.render(self.xlabel,True,self.c.white)
        ylabel = myfont.render(self.ylabel,True,self.c.white)

        # first time executed set params for plot
        if self.xlim == []:
            self.xlim = [round(xve.min(),4),round(xve.max(),4)]
        if self.ylim == []:
            self.ylim = [round(yve.min(),4),round(yve.max(),4)]
#            self.params_set = True

        # get params
        xlim = self.xlim
        ylim = self.ylim
        xstep = self.xstep
        ystep = self.ystep

        # array for tick numbers
        xnums = []
        ynums = []

        for i in np.linspace(xlim[0],xlim[1],xstep):
            xnums.append(myfont.render('{0:.2f}'.format(i),True,self.c.white))

        for i in np.linspace(ylim[0],ylim[1],ystep):
            ynums.append(myfont.render('{0:.2f}'.format(i),True,self.c.white))

        max_num_w = ynums[-1].get_width()
        max_num_h = xnums[-1].get_height()

        # tick coordinates in x and y direction
        tickX = int(5+ylabel.get_height()+5+max_num_w+5)
        tickY = int(self.h-5-xlabel.get_height()-5-max_num_h-5)

        # graph boundaries coordinates
        self.xy_graph.append([tickX+5,self.w-tickX+10])
        self.xy_graph.append([tickY-5,self.h-tickY-10])

        xb = self.xy_graph[0]
        yb = self.xy_graph[1]

        # draw xlabel
        y = int(self.h-xlabel.get_height()-5)
        x = int(xb[0]+(xb[1]-xb[0])/2-xlabel.get_width()/2)
        self.p_surf.blit(xlabel,(x,y))

        # draw ylabel 
        ylabel = pygame.transform.rotate(ylabel, 90)
        y = int(yb[1]+(yb[0]-yb[1])/2 -ylabel.get_height()/2)
        x = int(5)
        self.p_surf.blit(ylabel,(x,y))

        # draw x-axis
        pygame.draw.line(self.p_surf,(0,0,0),(xb[0],yb[0]),(xb[1],yb[0]),2)
        # draw y-axis
        pygame.draw.line(self.p_surf,(0,0,0),(xb[0],yb[0]),(xb[0],yb[1]),2)

        # draw x-axis numbers and ticks
        for i,x in enumerate(np.linspace(xb[0],xb[1],xstep)):
            pygame.draw.line(self.p_surf,self.c.black,(int(x),yb[0]),(int(x),tickY),2)
            self.p_surf.blit(xnums[i],(int(x)-(xnums[i].get_width()/2),tickY+5))

        # draw y-axis numbers and ticks
        for i,y in enumerate(np.linspace(yb[0],yb[1],ystep)):
            pygame.draw.line(self.p_surf,self.c.black,(xb[0],int(y)),(tickX,int(y)),2)
            yPos = int(y)-ynums[i].get_height()/2
            self.p_surf.blit(ynums[i],(tickX-5-ynums[i].get_width(),yPos))

    def draw_graph(self,x,y):

        xb = self.xy_graph[0]
        yb = self.xy_graph[1]

        # get params
        xlim = self.xlim
        ylim = self.ylim
        xstep = self.xstep
        ystep = self.ystep

        self.g_surf = pygame.Surface((xb[1]-xb[0],yb[0]-yb[1]))
        self.g_surf.fill(self.c.bg)

        scrw = xb[1]-xb[0]
        scrh = yb[0]-yb[1]

        # transform coordinates
        x = x*scrw/(xlim[1]-xlim[0]) + scrw*xlim[0]/(xlim[0]-xlim[1])
        y = y*-1
        y = y*scrh/(ylim[1]-ylim[0]) + scrh*ylim[1]/(ylim[1]-ylim[0])

        # draw graph (linear interpolation point to point)
        for i in range(len(x)-1):
            pygame.draw.line(self.g_surf,self.c.green,(x[i],y[i]),(x[i+1],y[i+1]),2)
        self.p_surf.blit(self.g_surf,(xb[0]+2,yb[1])) # +2 because y-axis

