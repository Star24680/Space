import math
import random
import pygame

W= 800

H = 500

PLAYER_START_X = 370

PLAYER_START_Y = 380

ENEMY_START_Y_MIN = 50

ENEMY_START_Y_MAX = 150

ENEMY_SPEED_X = 4

ENEMY_SPEED_Y = 40

BULLET_SPEED_Y = 10

COLLISION_DISTANCE = 27

pygame.init()
screen= pygame.display.set_mode((W,H))

BG=pygame.image.load('BG.png')

pygame.display.set_caption("Space Invader")
Icon=pygame.image.load('UFO.png')
pygame.display.set_icon(Icon)

player=pygame.image.load('SpaceShip.png')
playerX=PLAYER_START_X
playerY=PLAYER_START_X
playerX_change=0

Enemy=[]
EnemyX=[]
EnemyY=[]
EnemyX_change=[]
EnemyY_change=[]
NoEnemy=6

for i in range(NoEnemy):
    Enemy.append(pygame.image.load('RedRobot.png'))
    EnemyX.append(random.randint(0,W-64))
    EnemyY.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    EnemyX_change.append(ENEMY_SPEED_X)
    EnemyY_change.append(ENEMY_SPEED_Y)

Bullet=pygame.image.load('Bullet.png')
BulletX=0
BulletY=PLAYER_START_Y
BulletX_change=0
BulletY_change=BULLET_SPEED_Y
BulletState="Ready"

Score=0
Font=pygame.font.Font('freesansbold.ttf',32)
TextX=10
TextY=10

OverFont=pygame.font.Font('freesansbold.ttf',64)

def ShowScore(X,Y):
    S=Font.render("Score: "+str(Score),True,(225,255,255))
    screen.blit(S,(X,Y))

def GameOverText():
    OverText=OverFont.render("GAME OVER",True,(225,225,225))
    screen.blit(OverText,(200,250))

def Player(X,Y):
    screen.blit(player,(X,Y))

def enemy(x,y,i):
    screen.blit(Enemy[i],(x,y))

def FireBullet(x,y):
    global BulletState
    BulletState="Fire"
    screen.blit(Bullet,(x+16,y+10))

def Collision(EnemyX,EnemyY,BulletX,BulletY):
    Distance=math.sqrt((EnemyX-BulletX)**2+(EnemyY-BulletY)**2)
    return Distance<COLLISION_DISTANCE

running=True
while running:
    screen.fill((0,0,0))
    screen.blit(BG,(0,0))

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerX_change=-5
            if event.key==pygame.K_RIGHT:
                playerX_change=5
            if event.key==pygame.K_SPACE and BulletState=="Ready":
               BulletX=playerX
               FireBullet(BulletX,BulletY)
        if event.type==pygame.KEYUP and event.key in [pygame.K_LEFT,pygame.K_RIGHT]:
            playerX_change=0

    playerX += playerX_change
    playerX=max(0,min(playerX,W-64))

    for i in range(NoEnemy):
        if EnemyY[i]>340:
           for j in range (NoEnemy):
               EnemyY[j]=2000
           GameOverText()
           break
        EnemyX[i] += EnemyX_change[i]
        if EnemyX[i] <= 0 or EnemyX[i] >= W-64:
          EnemyX_change[i]*= -1
          EnemyY[i] += EnemyY_change[i]

        if Collision(EnemyX[i],EnemyY[i],BulletX,BulletY):
          BulletY=PLAYER_START_Y
          BulletState="Ready"
          Score += 1
          EnemyX[i]=random.randint(0,W-64)
          EnemyY[i]=random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX)

    enemy(EnemyX[i],EnemyY[i],i)
    if BulletY<=0:
        BulleyY=PLAYER_START_Y
        BulletState="Ready"
    elif BulletState=="Fire":
         FireBullet(BulletX,BulletY)
         BulletY-=BulletY_change
        
    Player(playerX,playerY)
    ShowScore(TextX,TextY)
    pygame.display.update()
pygame.quit()