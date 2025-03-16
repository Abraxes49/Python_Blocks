import pygame
import VIIII_2_Player
import VIIII_1_Coin

class Game:

    def __init__(self):
        pygame.init()
        self.window_width = 800
        self.window_height = 600
        self.window = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Coin Collector")
        self.clock = pygame.time.Clock()
        self.player = VIIII_2_Player.Player(self, 64, 64)        # also das der Pdfad sozuasgen die klasse Player
        self.coins = [VIIII_1_Coin.Coin(self, 150, 150),            # List e mit Coin objecten
                      VIIII_1_Coin.Coin(self, 250, 150),
                      VIIII_1_Coin.Coin(self, 150, 250)]
        self.run()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

            self.delta_time = self.clock.tick(60)/1000
            self.window.fill((25, 25, 25))
            self.player.update()         #selbiges
            #self.coin.update()             #singel object

            for coin in self.coins:            #Multible Objecte
                coin.update()
                if coin.is_destroyed:           #zerstören
                    self.coins.remove(coin)

            pygame.display.update()



game = Game()

pygame.quit()