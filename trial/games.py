import pygame

pygame.init()
window = pygame.display.set_mode((550, 550))  # width and lenght for window
pygame.display.set_caption("Sahil the Knight")  # title for heading of pygame window
right = [pygame.image.load("image/k1.png"), pygame.image.load("image/k2.png"), pygame.image.load("image/k3.png"),
         pygame.image.load("image/k4.png"), pygame.image.load("image/k5.png"), pygame.image.load("image/k6.png"),
         pygame.image.load("image/k7.png"), pygame.image.load("image/k8.png")]
left = [pygame.image.load("image/k9.png"), pygame.image.load("image/k10.png"), pygame.image.load("image/k11.png"),
        pygame.image.load("image/k12.png"), pygame.image.load("image/k13.png"), pygame.image.load("image/k14.png"),
        pygame.image.load("image/k15.png"), pygame.image.load("image/k16.png")]
bg = pygame.image.load("bg.jpg")
rest = pygame.image.load("image/k0.png")
clock = pygame.time.Clock()

#def game():
class players(object):
    def __init__(self,x,y,width,height):
        self.x = 50
        self.y = 500
        self.width = 50
        self.height = 50
        self.velocity = 5
        self.run = True
        self.isjump = False
        self.jumpcount = 10
        self.walkleft = False
        self.walkright = False
        self.wcount = 0

    def draws(self,window):
        if self.wcount >= 64:
            self.wcount = 0
        if self.walkleft:
            window.blit(left[self.wcount // 8], (self.x, self.y))
        elif self.walkright:
            window.blit(right[self.wcount // 8], (self.x, self.y))
        else:
            window.blit(rest, (self.x, self.y))

def drawgames():
    global wcount
    window.blit(bg,(0,0))
    play.draws(window)
    pygame.display.update()

play = players(50, 480, 50, 50)
run = True

while run:
    clock.tick(64)
    for event in pygame.event.get():# check all event we do like moving the mouse
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and play.x > play.velocity:  # AND condition is to maintain the block within the screen
        play.x -= play.velocity
        play.walkleft = True
        play.walkright = False
    elif keys[pygame.K_RIGHT] and play.x < (550 - play.width - play.velocity):
        play.x += play.velocity
        play.walkright = True
        play.walkleft = False
    else:
        play.walkleft = False
        play.walkright = False
        play.wcount = 0
    if not(play.isjump):  # checks whether the variable is filled with none,empty,zero or False and if yes then it will execute
        if keys[pygame.K_SPACE]:
            play.isjump = True
            play.walkleft = False
            play.walkright = False
            play.wcount = 0
    else:
        if play.jumpcount >= -10:
            neg = 1
            if play.jumpcount < 0:
                neg = -1
            play.y -= (play.jumpcount ** 2) * 0.5 * neg  # to move box upward and then by decrementing the val of the jumpcount moving it slowly decreasing speed
            play.jumpcount -= 1
        else:
            play.isjump = False
            play.jumpcount = 10
    drawgames()
    pygame.quit()