import pygame
import math
import random
pygame.init()

screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Space Invaders")

icon = pygame.image.load("rocket-launch.png")
pygame.display.set_icon(icon)

playerImg = pygame.image.load('battleship.png')
Player_size = (200,200)
image = pygame.transform.scale(playerImg, Player_size)
playerX = 370
playerY = 700
playerX_change = 0
playerY_change = 0

enemyImg = pygame.image.load('spaceship.png')
enemyX = 300
enemyY = 50

bulletImg = pygame.image.load('fire.png')
bulletX = playerX
bulletY = playerY
bulletY_change = 10
bullet_state = "ready"

enemy_hp = 100
font = pygame.font.Font('freesansbold.ttf',32)

textX = 10
textY = 10

def show_hp(x,y):
    health = font.render("Health: " + str(enemy_hp),True, (255, 255, 255))
    screen.blit(health, (x,y))
def player(x,y):
    screen.blit(playerImg,(x, y))

def enemy(x,y):
    screen.blit(enemyImg,(x, y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+16,y+10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow((enemyX+60)-bulletX,2)+math.pow(enemyY-bulletY,2)))
    if distance < 100:
        return True
    return False

def obstacle(obs_starty, obs_startx, obs):
    obs_pic = pygame.image.load("fire.png")
    screen.blit(obs_pic,(obs_startx, obs_starty))

running = True


while running:

    screen.fill((0, 0, 0))

    obstacle_speed = 6
    obs =0
    y_change = 0
    obs_startx = random.randrange(0, 800)
    obs_starty = 60


    obs_width = 15
    obs_height = 15

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -4
            if event.key == pygame.K_d:
                playerX_change = 4
            if event.key == pygame.K_w:
                playerY_change = -4
            if event.key == pygame.K_s:
                playerY_change = 4
            if event.key == pygame.K_SPACE:
                fire_bullet(playerX+3*playerX_change, playerY+2*playerY_change)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change= 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                playerY_change= 0


    playerX+=playerX_change
    playerY+=playerY_change
    if playerX<=0:
        playerX=0
    elif playerX>=736:
        playerX=736
    if playerY<=400:
        playerY=400
    elif playerY>=700:
        playerY = 700

    if bulletY <=0:
        bulletX=playerX
        bulletY = playerY
        bullet_state="ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY-=bulletY_change

    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        enemy_hp -=1
        bulletY = playerY
        bulletX = playerX
        bullet_state = "ready"
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    show_hp(textX, textY)
    
    obstacle(obs_startx, obs_starty,obs)
    obs_starty+=obstacle_speed
    if obs_starty >700: 
      obs_starty= 0
      obs_startx=random.randrange(0,800)
      print("NEW")
      print(random.randrange(0,800))
      obs=random.randrange(0,7)
      


    pygame.display.update()