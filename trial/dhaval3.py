import pygame
import random
import os

width = 360
heigth = 480
fps = 30

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gamefolder = os.path.dirname(__file__)
imgfolder = os.path.join(gamefolder,"image")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(imgfolder,"k1.png")).convert()
        #self.image = pygame.Surface((50,50))
        #self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (width/2,heigth/2)

    def update(self):
        self.rect.x += 5
#initialize pygmae and gaming screen
pygame.init()
pygame.mixer.init()
window = pygame.display.set_mode((550,550))#width and lenght for window
pygame.display.set_caption("Sahil the Knight")#title for heading of pygame window
clock = pygame.time.Clock()
spirites = pygame.sprite.Group()
player = Player()
spirites.add(player)

run = True
while run:
    clock.tick(fps)
    pygame.display.flip()#flip the display front side back
    for event in pygame.event.get():#check all event we do like moving the mouse
        if event.type == pygame.QUIT:
            run = False

    spirites.update()
    window.fill(black)
    spirites.draw(window)

pygame.quit()