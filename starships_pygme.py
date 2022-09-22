import pygame
import os

# Definer spillvinduet i objektet WIN
WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Eriks første Pythonspill")

# Bruker definerte events
YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2



# Skillestrek
BORDER = pygame.Rect((WIDTH/2)-5, 0, 10, HEIGHT)

#Globale variabler (konstanter egentlig)
FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_HEIGHT, SPACESHIP_WIDTH = 55,60

# farger
WHITE = (255,255,255)
BLACK = (0,0,0)

# Importerer grafikkfilene, skalerer de og roterer rett vei
RED_SPACESHIP_IMAGE=pygame.image.load(os.path.join("Assets","spaceship_red.png"))
RED_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)

YELLOW_SPACESHIP_IMAGE=pygame.image.load(os.path.join("Assets","spaceship_yellow.png"))
YELLOW_SPACESHIP=pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)




# Tegner opp spillvinduet
def draw_window(red, yellow):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x,yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x,red.y))
    pygame.display.update()

# The yellow spaceship  bevegelse (wasd)
def yellow_handle_movement(keys_pressed, yellow): 
        if keys_pressed[pygame.K_a] and yellow.x - VEL > 0 :
            yellow.x -= VEL
        if keys_pressed[pygame.K_d] and yellow.x + VEL + SPACESHIP_WIDTH < BORDER.x:
            yellow.x += VEL     
        if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
            yellow.y -= VEL
        if keys_pressed[pygame.K_s] and yellow.y + VEL + SPACESHIP_HEIGHT < HEIGHT -10:
            yellow.y += VEL

# The red spaceship bevegelse (piltaster)
def red_handle_movement(keys_pressed, red): 
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + 10 :
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + SPACESHIP_WIDTH < WIDTH:
        red.x += VEL     
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + SPACESHIP_HEIGHT < HEIGHT -10:
        red.y += VEL

# Kuler bevegelse og hit sjekk
def handle_bullets(yellow_bullets, red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += 1
        if yellow.colliderect(bullet)


# Hovedprogram starter her :::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    
    red_bullets=[]
    yellow_bullets=[]

    clock = pygame.time.Clock()
   
    run = True 
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(yellow.x+yellow.width, yellow.y + yellow.height/2 + 2, 10, 5)
                    yellow_bullets.append(bullet)

                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet=pygame.Rect(red.x, red.y + red.height/2 + 2, 10, 5)
                    red_bullets.append(bullet)

        keys_pressed = pygame.key.get_pressed()
        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movement(keys_pressed, red)
        
        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        draw_window(red, yellow)

    pygame.quit()


if __name__=="__main__":
    main()

