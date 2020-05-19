import pygame

# Intialize the pygame
pygame.init()   

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Dinoventure")
icon = pygame.image.load('dino_icon.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('dino_char.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
running = True
while running:
     # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
    pygame.time.delay(100)

    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN: #checking if any key was pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_DOWN:
                playerY_change = 5
            if event.key == pygame.K_UP:
                playerY_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                playerY_change = 0

    playerX += playerX_change
    playerY += playerY_change
    player(playerX, playerY)
    pygame.display.update()
