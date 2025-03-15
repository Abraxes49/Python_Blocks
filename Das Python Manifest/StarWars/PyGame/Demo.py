import pygame

pygame.init()

window_with = 800
window_height = 600
window = pygame.display.set_mode((window_with, window_height))
color = (25, 25, 25)

running = True
while running:                          # Events https://programmieren-starten.de/blog/pygame-events/

    for event in pygame.event.get():    #Geht darunter stehend Event Liste durch
        if event.type == pygame.QUIT:   # event Quit
            running = False
        elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:   #event Taste gedrückt ESC
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            color = (255,255,25)

    window.fill((color))
    pygame.display.update()
pygame.quit()








