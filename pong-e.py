import pygame
from pygame.locals import *

class Pong(object):
    def __init__(self, screensize):
        self.screensize = screensize
        self.centerx = int(screensize[0]*0.5)
        self.centery = int(screensize[1]*0.5)
        self.radius = 5
        self.rect = pygame.Rect(self.centerx-self.radius,
                                self.centery-self.radius,
                                self.radius*2, self.radius*2)
        self.color = (100,100,255)
        self.direction = [1,1]
        self.speed = 5
        ## Task: change speed as game progresses to make it harder

        self.hit_edge_left = False
        self.hit_edge_right = False

    def update(self, player_paddle=None, ai_paddle=None):
        self.centerx += self.direction[0]*self.speed
        self.centery += self.direction[1]*self.speed

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1]-1:
            self.direction[1] = -1

        if self.rect.right >= self.screensize[0]-1:
            self.hit_edge_right = True
        elif self.rect.left <= 0:
            self.hit_edge_left = True

    def render(selfself, screen):
        pygame.draw.circle


def main():
    pygame.init()

    screensize = (640,480)

    screen = pygame.display.set_mode((640,480))
    clock = pygame.time.Clock()
    pong = Pong(screensize)
    running = True

    while running:
        ## FPS limiting/reporting phase
        clock.tick(100)

        ## Event handling phase
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        ## Object updating phase
        pong.update()

        ## Task: make some text on the screen over everything else
        ## Allow restarting of the game
        if pong.hit_edge_left:
            print("You won!")
            running = False
        elif pong.hit_edge_right:
            print("You lose")
            running = False

        ## Rendering phase
        screen.fill((0,0,0))
        pygame.display.flip()

    pygame.quit()

    
main()
