import pygame  #載入pygame module

pygame.init()  #啟動
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  #產生畫布
pygame.display.set_caption("My first pygame!")

BLACK  = (0, 0, 0)
WHITE  = (255, 255, 255)
RED    = (255, 0, 0)
GREEN  = (0, 255, 0)
BLUE   = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN   = (0, 255, 255)
MEG    = (255, 0, 255)
GRAY   = (192, 192, 192)

ABC = (130, 200, 200)
BCA = (235, 235, 200)
CAB = (235, 200, 235)
ACB = (200, 235, 235)

displayscreen.fill(ABC)  #填滿畫布背景
#pygame.draw.line(畫布名稱, color, start, end, thickness)
pygame.draw.line(displayscreen, BCA, (0, WINDOW_HEIGHT//2), (WINDOW_WIDTH, WINDOW_HEIGHT//2), 5)
pygame.draw.line(displayscreen, CAB, (WINDOW_WIDTH//2 , 0), (WINDOW_WIDTH//2, WINDOW_HEIGHT), 5)

pygame.draw.line(displayscreen, BCA, (0, 0), (WINDOW_WIDTH, WINDOW_HEIGHT), 5)
pygame.draw.line(displayscreen, CAB, (WINDOW_WIDTH , 0), (0, WINDOW_HEIGHT), 5)

#pygame.draw.circle(畫布名稱, 顏色, 中心點, 半徑, thickness)  thickness=0(填滿)  1,2,...,10:線條寬度
pygame.draw.circle(displayscreen, ACB, (WINDOW_WIDTH//2, WINDOW_HEIGHT//2), 150, 3)

#pygame.draw.rect(畫布名稱, 顏色, (topleft-x, topleft-y, width, height), thickness)  0:填滿, 1,2,...,10:線條寬度
pygame.draw.rect(displayscreen, ACB, (0, 0, WINDOW_WIDTH, 100), 0)


running = True
while running:
    for event in pygame.event.get():  #抓取畫布上所有的事件
        #print(event)
        if event.type == pygame.QUIT:  #事件的Type==QUIT(按下結束鍵)
            running = False
            
    pygame.display.update()  #畫布更新

pygame.quit()  #結束