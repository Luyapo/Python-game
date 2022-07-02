import pygame
import random

pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  
pygame.display.set_caption("Movement and collisions!")

#set FPS(Frequency Per Second) and clock(抓CPU的時序)
FPS = 60
clock = pygame.time.Clock()

#Set game values
VELOCITY = 5  #速率
BLACK = (0, 0, 0)

angry_bird             = pygame.image.load("angrybird.png")
angry_bird_rect        = angry_bird.get_rect()
angry_bird_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

coin      = pygame.image.load("coin.png")
coin_rect = coin.get_rect()
coin_rect.center = (100, 100)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    keys = pygame.key.get_pressed()  #偵測目前有哪個鍵被按下
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and angry_bird_rect.left>0:
        angry_bird_rect.x -= VELOCITY
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and angry_bird_rect.right<WINDOW_WIDTH:
        angry_bird_rect.x += VELOCITY
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and angry_bird_rect.top>0:
        angry_bird_rect.y -= VELOCITY
    if (keys[pygame.K_DOWN]or keys[pygame.K_s]) and angry_bird_rect.bottom<WINDOW_HEIGHT:
        angry_bird_rect.y += VELOCITY
    
    if angry_bird_rect.colliderect(coin_rect):
        print("HIT")
        coin_rect.x = random.randint(0, WINDOW_WIDTH-50)
        coin_rect.y = random.randint(0, WINDOW_HEIGHT-50)
        
        
    displayscreen.fill(BLACK)            
    displayscreen.blit(angry_bird, angry_bird_rect)
    displayscreen.blit(coin, coin_rect)
    pygame.display.update()
    clock.tick(FPS)
            

pygame.quit()