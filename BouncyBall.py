import pygame

#Initiate game
pygame.init()
#Create a screen size 800*600
screen = pygame.display.set_mode([800,600])
keep_playing = True

#Load ball image
ball = pygame.image.load("CrazySmile.bmp")
posx = 0
posy = 0
speedx = 5
speedy = 5

#paddle
paddlew= 200
paddleh = 25
paddlex = 300
paddley = 550

BLACK = (0,0,0)
WHITE = (255,255,255)

timer = pygame.time.Clock()

while keep_playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            keep_going = False


    screen.fill(BLACK) #Fill screen with black color
    posx += speedx
    posy += speedy

    paddlex = pygame.mouse.get_pos()[0]
    pygame.draw.rect(screen, WHITE, (paddlex, paddley, paddlew, paddleh))



    #if ball hit a wall change speed
    if posy+ball.get_height() >= 600 or posy <=0:
        speedy = -speedy
    if posx + ball.get_width() >= 800 or posx <=0:
        speedx = -speedx

    screen.blit(ball, (posx, posy))
    pygame.display.update()
    timer.tick(60) # Make frame per second as 60

pygame.quit()  # Exit

