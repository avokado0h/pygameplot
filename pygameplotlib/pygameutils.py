
   ####################
  #  pygameutils.py  #
 # by -=avokado0h=- #
####################

import pygame

class colors():
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

class py_handler():
    def __init__(self,width=1000,height=800,caption='PygamePlotLib_by_avokado0h'):
        pygame.init()

        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width,self.height))

        pygame.font.init()

        self.font = pygame.font.SysFont('DejaVu Sans Mono', 30)
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.c = colors()
        self.fps = 0
        self.running = True
    
    def check_input(self,b=None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                if b.button.collidepoint(mouse_pos):
                    b.state = not(b.state)

    def py_update(self):
        self.check_input()
        pygame.display.flip()
        self.clock.tick(30)
        self.fps = self.clock.get_fps()
        self.screen.fill(self.c.bg)
        return self.running

class tbutton():
    def __init__(self,a,width=50,height=10,x=0,y=0):
        self.a = a
        self.scr = self.a.screen
        self.w = width
        self.h = height
        self.x = x
        self.y = y
        self.button = pygame.Rect(self.x,self.y,self.w,self.h)
        self.c = colors()
        self.state = False

    def check_button(self):
        self.a.check_input(self)
        #pygame.draw.rect(self.scr,(255,255,255),self.button)
        st = pygame.Surface((self.w,self.h))
        st.fill(self.c.bg1)
        if self.state == True:
            sa = pygame.Surface((self.w/2,self.h))
            sa.fill(self.c.red)
            st.blit(sa,(0,0))
        if self.state == False:
            sa = pygame.Surface((self.w/2,self.h))
            sa.fill(self.c.red)
            st.blit(sa,(self.w/2,0))
        self.scr.blit(st,(self.x,self.y))
        return self.state

