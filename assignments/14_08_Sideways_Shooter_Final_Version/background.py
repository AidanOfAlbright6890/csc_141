import random

import pygame

# Initialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode ((800, 600))

# Backround
backround = pygame.image.load('assignments/14_scoring/14_08_Sideways_Shooter_Final_Version/background.png')

# Caption and Icon
pygame.display.set_caption("assignments/14_scoring/14_08_Sideways_Shooter_Final_Version")
icon = pygame.image.load('assignments/14_scoring/14_08_Sideways_Shooter_Final_Version/new_alien.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('assignments/14_scoring/14_08_Sideways_Shooter_Final_Version/ship3.bmp')
playerX = 370
playerY = 480
playerX_change = 0

# Ememy
alienImg = pygame.image.load('assignments/14_scoring/14_08_Sideways_Shooter_Final_Version/new_alien.png')
alienX = random.randint (0, 800)
alienY = random.randint (50, 150)
alienX_change = 0.3
alienY_change = 40

def player(x, y):
    screen.blit(playerImg, (x, y))

def alien(x, y):
    screen.blit (alienImg, (x, y))

# Game Loop
running = True
while running:
    # RGB = Red, Green, Blue
    screen.fill ((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # if keystroke is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.3

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

# 5 = 5 + -0.1 -> 5 = 5 - 0.1
# 5 = 5 + 0.1

playerX += playerX_change
if playerX <= 0:
    playerX = 0
elif playerX >= 736:
    playerX = 736

# Enemy Movement

