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

input_font = pygame.font.Font(None,32);
userText = ''

## rect for text
rect_width = 200
rect_height = 50
rect = pygame.Rect(SCREEN_WIDTH_CENTER - rect_width // 2,SCREEN_HEIGHT_CENTER, rect_width, rect_height)

is_active = False
colorActive = (0,0,255)
colorInactive = (0,255,0)

currColorRect = colorInactive



#### Btn

btn_font = pygame.font.Font(None,30)
button_width = 100
button_height = 100

button_rect = pygame.Rect(SCREEN_WIDTH_CENTER - button_width // 2 + rect_width ,
                          SCREEN_HEIGHT_CENTER - button_height // 2 + rect_height ,
                          button_width, button_height)





running = True 




while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False 

        if event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                print(is_active)
                is_active =  not is_active
            else:
                is_active = False
            
            if is_active:
                currColorRect = colorActive
            else:
                currColorRect = colorInactive


            if button_rect.collidepoint(event.pos):
                if len(userText) >= 1:
                    userText = ''
                    print("Ok ")
        if is_active:
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if len(userText) < 10 :
                        userText += event.unicode
        
        
    screen.fill(BLACK) 



    text_surface = input_font.render(userText, True, (255, 255, 255))
    screen.blit(text_surface, (rect.x+5, rect.y+5))


    pygame.draw.rect(screen, (255,255,255), button_rect)
    btn_text_surface = btn_font.render("Click Confirm!", True, (0,0,255))
    button_rect = btn_text_surface.get_rect(center=button_rect.center)
    screen.blit(btn_text_surface,button_rect)

    
    pygame.draw.rect(screen,currColorRect,rect,2)
    pygame.display.flip()    

    clock.tick(60)

pygame.quit()