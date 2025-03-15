import pygame

pygame.init()

window_with = 800
window_height = 600
window = pygame.display.set_mode((window_with, window_height))
player_x = 32
player_y = 32
clock = pygame.time.Clock()                     #clock initailisieren

running = True
while running:
    delta_time = clock.tick(60) / 1000                              #Framerate
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
            running = False

    keys = pygame.key.get_pressed()
    speed = 240                                  # alles modifiziert vergleich VI
    if keys[pygame.K_RIGHT]:
        player_x += speed * delta_time
    elif keys[pygame.K_LEFT]:
        player_x -= speed * delta_time
    if keys[pygame.K_DOWN]:
        player_y += speed * delta_time
    elif keys[pygame.K_UP]:
        player_y -= speed * delta_time


    window.fill((25, 25, 25))
    pygame.draw.rect(window, "red", (player_x, player_y, 64, 64))
    pygame.display.update()

pygame.quit()








