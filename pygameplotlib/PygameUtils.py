
    ####################
   #  PygameUtils.py  #
  # by -=avokado0h=- #
 ####################

import pygame

class Colors():
    def __init__(self):
        self.white = pygame.Color('#ebdbb2')
        self.black = pygame.Color('#000000')
        self.bg = pygame.Color('#282828')
        self.bg1 = pygame.Color('#3c3836')
        self.cyan = pygame.Color('#b16286')
        self.yellow = pygame.Color('#fabd2f')
        self.blue = pygame.Color('#458588')
        self.green = pygame.Color('#b8bb26')
        self.red = pygame.Color('#fb4934')

class Settings():
    def __init__(self,width=1000,height=800,caption='PygamePlotLib_by_avokado0h'):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))
        pygame.font.init()
        # self.font = pygame.font.Font(pygame.font.get_default_font(),20)
        self.pltFont = pygame.font.SysFont('DejaVu Sans Mono', 15)
        self.font = pygame.font.SysFont('DejaVu Sans Mono', 25)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.c = Colors()
        self.fps = 0
        self.running = True
        self.key = ''
    
    def checkInput(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_LEFT:
                    self.key = 'j'
                else: self.key = ''

    def Update(self):
        self.checkInput()
        pygame.display.flip()
        self.clock.tick(30)
        self.fps = self.clock.get_fps()
        self.screen.fill(self.c.bg)
        return self.running

def showText (a,x,y,text='',size=20):
        c = Colors()
        txt = a.font.render(text,True,c.white)
        a.screen.blit(txt,(x,y))
