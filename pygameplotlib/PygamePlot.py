
    ####################
   # PygamePlot.py # 
  # by -=avokado0h=- #
 ####################

import pygame
import numpy as np
from pygameutils import Colors

class Plot():
    def __init__(self,a,w,h,xlabel='',ylabel='',
            caption='',xlim=[],ylim=[],ystep=3,xstep=3):
        self.w = w
        self.h = h
        # surface to draw plotsurface on 
        self.s_surf = a.screen
        self.font = a.pltFont
        # plotsurface to draw graphsurface on
        self.p_surf = pygame.Surface((w,h))
        # graphsurface
        self.g_surf = None
        self.xy_graph = []
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.caption = caption
        self.xlim = xlim
        self.ylim = ylim
        self.ystep = ystep
        self.xstep = xstep
        self.c = Colors()

    def Show(self,x,y,xve,yve,sci,cc):
        self.p_surf.fill(self.c.bg1)
        self.drawAxis(xve,yve)
        self.drawGraph(xve,yve,sci,cc)
        self.s_surf.blit(self.p_surf,(x,y))

    def drawAxis(self,xve,yve):
        # create x/y-label surface
        xlabel = self.font.render(self.xlabel,True,self.c.white)
        ylabel = self.font.render(self.ylabel,True,self.c.white)
        caption = self.font.render(self.caption,True,self.c.white)

        # first time executed set params for plot
        if self.xlim == []:
            self.xlim = [round(xve.min(),4),round(xve.max(),4)]
        if self.ylim == []:
            self.ylim = [round(yve.min(),4),round(yve.max(),4)]

        # get params
        xlim = self.xlim
        ylim = self.ylim
        xstep = self.xstep
        ystep = self.ystep

        # array for tick numbers
        xnums = []
        ynums = []

        for i in np.linspace(xlim[0],xlim[1],xstep):
            xnums.append(self.font.render('{0:.2f}'.format(i),True,self.c.white))

        for i in np.linspace(ylim[0],ylim[1],ystep):
            ynums.append(self.font.render('{0:.2f}'.format(i),True,self.c.white))

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

        # draw caption
        self.p_surf.blit(caption,(int(self.w/2-caption.get_width()/2),int(yb[1]/2-caption.get_height()/2)))

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

    def drawGraph(self,x,y,sci,color):

        xb = self.xy_graph[0]
        yb = self.xy_graph[1]

        if color == 'green':
            clr = self.c.green
        if color == 'blue':
            clr = self.c.blue

        # get params
        xlim = self.xlim
        ylim = self.ylim
        xstep = self.xstep
        ystep = self.ystep

        if sci == False:
            self.g_surf = pygame.Surface((xb[1]-xb[0],yb[0]-yb[1]))
            self.g_surf.fill(self.c.bg)
            scrw = xb[1]-xb[0]
            scrh = yb[0]-yb[1]

        if sci == True:
            self.g_surf = pygame.Surface((self.w,self.h))
            self.g_surf.fill(self.c.bg)
            scrw = self.w
            scrh = self.h

        # transform coordinates
        x = x*scrw/(xlim[1]-xlim[0]) + scrw*xlim[0]/(xlim[0]-xlim[1])
        y = y*-1
        y = y*scrh/(ylim[1]-ylim[0]) + scrh*ylim[1]/(ylim[1]-ylim[0])

        if sci == False:
            # draw graph (linear interpolation point to point)
            for i in range(len(x)-1):
                pygame.draw.line(self.g_surf,clr,(x[i],y[i]),(x[i+1],y[i+1]),2)
            self.p_surf.blit(self.g_surf,(xb[0]+2,yb[1])) # +2 because y-axis

        if sci == True:
            for i in range(len(x)-1):
                pygame.draw.line(self.g_surf,clr,(x[i],y[i]),(x[i+1],y[i+1]),2)
            self.p_surf.blit(self.g_surf,(0,0)) # +2 because y-axis

