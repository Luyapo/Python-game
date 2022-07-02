# Python-games_basics 
#### 利用pygame創造的小遊戲

--- 

**_參考資料_**
  * Pygame Page: http://pygame.org 
  * Documentation: http://pygame.org/docs/ref
  * Icon Archive: https://iconarchive.com/
  * Leshy SFMaker: https://www.leshylabs.com/apps/sfMaker/
  * Font Space: https://www.fontspace.com/commercial-fonts
   
  <br>

## What is Pygame?
  * Pygame提供Display, Sound, Music, Image, Text, Event幫助製作遊戲
  * Pygame可以做出2-D小遊戲
  * Pygame偵測使用者使用keyboard, joystick, mouse來控制遊戲
  * Pygame提供許多內建的game objects來製作遊戲
   
  <br>
  

## Pygame Basics
  | Name | Description |
  |:-----:|:----------:|
  | _1.py_ | Create my game surface, game loop and drawing.|
  | _2.py_ | Blit text, font, sound and image objects. |
  | _3.py_ | Getting user keyboard and collision dection. | 
  
  <br>
  
## Code snippet
```python
#Create game display
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 600
displayscreen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Feed the Angry Bird!")

```
```python
#Blit image object and setting its rec
player_image        = pygame.image.load("angry_bird.png")
player_rect         = player_image.get_rect()
player_rect.left    = 32
player_rect.centery = WINDOW_HEIGHT//2
displayscreen.blit(player_image, player_rect)
```

**_Game Assets_**
* [Icon Archive:](https://iconarchive.com/) 提供很多遊戲角色下載
* [Leshy SFMaker:](https://www.leshylabs.com/apps/sfMaker/) 網站可以下載遊戲音效，也可以自行製作<br>

![ 2.py程式截圖 ](https://github.com/Luyapo/Python-games_basics/blob/main/png.png) 
