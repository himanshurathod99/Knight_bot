import pygame
pygame.init()
window = pygame.display.set_mode((500,500))#width and lenght for window
pygame.display.set_caption("Sahil Palkar")#title for heading of pygame window
x = 50
y = 440
width = 40
height = 60
velocity = 5
run = True
isjump = False
jumpcount = 10

while run:
    pygame.time.delay(100)
    for event in pygame.event.get():#check all event we do like moving the mouse
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT] and x > velocity:#AND condition is to maintain the block within the screen
    #   x -= velocity
    #if keys[pygame.K_RIGHT] and x < (500-width-velocity):
    #    x += velocity
    x += velocity
    if not(isjump):#checks whether the variable is filled with none,empty,zero or False and if yes then it will execute
        if keys[pygame.K_SPACE]:
            isjump = True
            #walkleft = False
            #walkright = False
            #wcount = 0
    else:
        if jumpcount >= -10:
            neg = 1
            if jumpcount < 0:
                neg = -1
                y -= (jumpcount ** 2) * 0.5 * neg #to move box upward and then by decrementing the val of the jumpcount moving it slowly decreasing speed
                jumpcount -= 1
        else:
            isjump = False
            jumpcount = 10
    #move.update(x,velocity)
    window.fill((0,0,0))
    pygame.draw.rect(window, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
pygame.quit()