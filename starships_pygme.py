import pygame
import os

# Definer spillvinduet i objektet WIN
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eriks første Pythonspill")

#Globale variabler (konstanter egentlig)
WHITE = (255,255,255)
FPS = 60
SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55,60


# Importerer grafikkfilene, skalerer de og roterer rett vei
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)



# Tegner opp spillvinduet
def draw_window(red, yellow):
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()



# Hovedprogram starter her
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    clock = pygame.time.Clock()
    run = True 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
        
        draw_window(red, yellow)

    pygame.quit()


if __name__=="__main__":
    main()

