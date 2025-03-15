import pygame

pygame.init()

window_with = 800
window_height = 600
window = pygame.display.set_mode((window_with, window_height))

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key ==pygame.K_ESCAPE:
            running = False

    window.fill((25, 25, 25))
    pygame.draw.circle(window, "red",(window_with/2, window_height/2), 100)

    pygame.display.update()
pygame.quit()








