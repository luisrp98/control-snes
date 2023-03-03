import pygame

pygame.init()

clk = pygame.time.Clock()

size = width, height = 256, 256
screen = pygame.display.set_mode(size)
background_image = pygame.image.load('./templates/control.png').convert()
frameReact = pygame.Rect((0, 0), (width, height))

crosshair = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshair, pygame.Color("white"), (5, 5), 10, 0)

crosshairb = pygame.surface.Surface((10, 10))
pygame.draw.circle(crosshairb, pygame.Color("red"), (5, 5), 5, 0)




while True:

    pygame.event.pump()

    screen.blit(background_image, (0,0))

    Keys=pygame.key.get_pressed()

    # Botones 
    if Keys[pygame.K_h]: screen.blit(crosshair, (180, 120))
    if Keys[pygame.K_j]: screen.blit(crosshair, (200, 100))
    if Keys[pygame.K_k]: screen.blit(crosshair, (200, 140))
    if Keys[pygame.K_l]: screen.blit(crosshair, (230, 120))

    # Gatillos
    if Keys[pygame.K_i]: screen.blit(crosshair, (200, 60))
    if Keys[pygame.K_u]: screen.blit(crosshair, (50, 60))

    # Pausa y
    if Keys[pygame.K_v]: screen.blit(crosshair, (100, 135))
    if Keys[pygame.K_b]: screen.blit(crosshair, (130, 135))


    x = -1 if Keys[pygame.K_a] else 1 if Keys[pygame.K_d] else 0

    y = -1 if Keys[pygame.K_w] else 1 if Keys[pygame.K_s] else 0



    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()
            exit()


    screen.blit(crosshairb, ((x*20)+55-5, (y*20)+125-5))

    pygame.display.flip()

    clk.tick(40)