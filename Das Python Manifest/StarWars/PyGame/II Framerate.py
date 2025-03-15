import pygame

pygame.init()

window_with = 800
window_height = 600
window = pygame.display.set_mode((window_with, window_height))

running = True
while running:
    for event in pygame.event.get():    #Frame abfrage 60 sekunde
        if event.type == pygame.QUIT:   #x für schließen
            running = False

pygame.quit()








