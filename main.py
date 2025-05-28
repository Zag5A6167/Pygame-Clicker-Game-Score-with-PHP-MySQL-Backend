import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_WIDTH_CENTER = SCREEN_WIDTH // 2
SCREEN_HEIGHT_CENTER = SCREEN_HEIGHT // 2
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Game")

BLACK = (0,0,0)
clock = pygame.time.Clock()

### Font

font = pygame.font.Font(None,32);
userText = ''

## rect for text
rect_width = 200
rect_height = 50
rect = pygame.Rect(SCREEN_WIDTH_CENTER - rect_width // 2,SCREEN_HEIGHT_CENTER, rect_width, rect_height)


running = True 

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False 


    screen.fill(BLACK) 

  

    pygame.draw.rect(screen,(0,255,0),rect)
    pygame.display.flip()    

    clock.tick(60)

pygame.quit()