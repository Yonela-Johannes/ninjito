import sys
import pygame
from scripts.entities import PhysicsEntity
from scripts.utils import load_image

class Game:
    def __init__(self):  
        pygame.init() # pygame instance

        pygame.display.set_caption('Ninjito')
        self.screen = pygame.display.set_mode((640, 480)) # set window/screen width x height [screen orientation]
        self.display = pygame.Surface((320, 240))


        self.clock = pygame.time.Clock()
        
        self.assets = {
            'player': load_image('entities/player.png')
        }
        self.movement = [False, False] # Movement for the cloud false at the beginning
        
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))
        
    def run(self):
        while True:
            self.display.fill((135,206,235)) #clearing the display after every cloud movement
                        
            self.player.update((self.movement[1] -  self.movement[0], 0))
            self.player.render(self.display)
            
                     
            # listening for any events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if the event is exit
                    pygame.quit() # exit the game
                    sys.exit() # exit the game
                    
                if event.type == pygame.KEYDOWN: # if any key is pressed(key pressed)
                    if event.key == pygame.K_LEFT: # if you press the up key
                        self.movement[0] = True # 0 == move up
                    if event.key == pygame.K_RIGHT: # if you press the down key
                        self.movement[1] = True # 1 == move down
                if event.type == pygame.KEYUP:# if any key is lifted up(done pressed)
                    if event.key == pygame.K_LEFT: # if you press the up key
                        self.movement[0] = False # 0 == move up
                    if event.key == pygame.K_RIGHT: # if you press the down key
                        self.movement[1] = False # 1 == move down
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()