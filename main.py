import pygame
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


pygame.display.set_caption("Game")

BLACK = (0,0,0)

running = True 

while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False 


    screen.fill(BLACK) 

  


    pygame.display.flip() 


pygame.quit()