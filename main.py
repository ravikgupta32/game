import pygame
import random
#intialize the pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((800,600))
#background
background = pygame.image.load('background.png')
#Title and Icon
pygame.display.set_caption("Warriors")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 480
playerX_change = 0
#Enemy
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 3
enemyY_change = 30
#Bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 6
bullet_state = "ready"
def player(x,y):
    screen.blit(playerImg,(x,y))
def enemy(x,y):
    screen.blit(enemyImg,(x,y))    
def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))    
#Game Loop
running = True

while running:
    screen.fill((0, 0, 0))
    #Background image
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
             if bullet_state is "ready":
                bulletX = playerX   
                fire_bullet(bulletX,bulletY) 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or  event.key == pygame.K_RIGHT: 
                playerX_change = 0
        
    #Checking For Boundaries
    playerX += playerX_change
    if playerX <=0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736    
    #Enemy Movement    
    enemyX += enemyX_change
    if enemyX <=0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3  
    #Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state is "fire":
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    player(playerX,playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()       