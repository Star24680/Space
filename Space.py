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

BG=pygame.image.load('Background.png')

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
    Enemy.append(pygame.image.load('RedRobot'))
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
Font=pygame.font.Font('Freesensbold.ttf',32)
TextX=10
TextY=10

OverFont=pygame.font.Font('freesensbold.ttf',64)

def ShowScore(X,Y):
    Score=Font.render("Score: "+str(Score),True,(225,255,255))
    screen.blit(Score,(X,Y))

def GameOverText():
    OverText=OverFont.render("GAME OVER",True,(225,225,225))
    screen.blit(OverText,(200,250))

def player(X,Y):
    screen.blit(player,(X,Y))