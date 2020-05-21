import pygame
from pygame.locals import *
from pygame import mixer
import time
# Intialize the pygame
pygame.init()   

# create the screen
screen = pygame.display.set_mode((800, 600))

# Caption and Icon
pygame.display.set_caption("Dinoventure")
icon = pygame.image.load('dino_icon.png')
pygame.display.set_icon(icon)

# BackGround Sound
mixer.music.load('music.mp3')
mixer.music.play(-1)

########################################################################################################################################
clock = pygame.time.Clock()
click = False
menu = True
def draw_text(text, size, color, surface, x, y, center):
    font = pygame.font.SysFont(None, size)
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    if center==True:
        textrect.center = (x, y)
    else:
        textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def Rules():
    screen.fill((0,0,0))
    draw_text("You will Play this game however.", 50, (255,50,0), screen, 800//2 ,140, True)
    pygame.display.update()
    time.sleep(2)
    while True:
        button_back = pygame.Rect(250,250,190,50)
        pygame.draw.rect(screen, (0, 100, 150), button_back)
        draw_text('back',45, (255,255,0), screen, 260, 260, False)
        click = False
        mx,my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            if event.type == QUIT:
                pygame.quit()
        if button_back.collidepoint((mx,my)):
            if click:
                break
        pygame.display.update()

def mainmenu():
    global click
    global menu
    global run
    while menu:
        screen.fill((0,0,0))
        draw_text('Dinoventure', 80, (255,0,0), screen, 800//2, 140, True)
        button_1 = pygame.Rect(250,250,190,50) # rectangle position and dimentions
        button_2 = pygame.Rect(250,350,300,50) 
        button_3 = pygame.Rect(250,450,80,50) 

        mx,my = pygame.mouse.get_pos()

        if button_1.collidepoint((mx,my)):
            if click:
                run = True
                menu = False
                break
        if button_2.collidepoint((mx,my)):
            if click:
                Rules()
        if button_3.collidepoint((mx,my)):
            if click:
                pygame.quit()

        pygame.draw.rect(screen, (0, 100, 150), button_1) # start game button
        pygame.draw.rect(screen, (0, 100, 150), button_2) # rules game button
        pygame.draw.rect(screen, (0, 100, 150), button_3) # exit

        draw_text('Start Game',45, (255,255,0), screen, 260, 260, False) #button text
        draw_text('Rules and Controls',45, (255,255,0), screen, 260, 360, False)
        draw_text('Exit',45, (255,255,0), screen, 260, 460, False)

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                menu = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    menu = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)

#######################################################################################################################3
mainmenu()

# Player
playerImg = pygame.image.load('dino_char.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))

# Game Loop
def game():
    global playerX
    global playerX_change
    global playerY
    global playerY_change
    running = True
    while running:
        # This will delay the game the given amount of milliseconds. In our casee 0.1 seconds will be the delay
        clock.tick(60)

        # RGB = Red, Green, Blue
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # if keystroke is pressed check whether its right or left
            if event.type == pygame.KEYDOWN: #checking if any key was pressed
                if event.key == pygame.K_LEFT:
                    playerX_change = -5
                    playerY_change = 0 # to avoid diagonal movement
                if event.key == pygame.K_RIGHT:
                    playerX_change = 5
                    playerY_change = 0 
                if event.key == pygame.K_DOWN:
                    playerY_change = 5
                    playerX_change = 0
                if event.key == pygame.K_UP:
                    playerY_change = -5
                    playerX_change = 0
                if event.key == pygame.K_SPACE:
                    break
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0
                if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    playerY_change = 0
                if event.key == pygame.K_SPACE:
                    break

        playerX += playerX_change
        playerY += playerY_change
        player(playerX, playerY)
        pygame.display.update()

game()