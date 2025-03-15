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

    window.fill((25, 25, 25))       #Hintergrundfarbe GRau
    pygame.display.update()
pygame.quit()








