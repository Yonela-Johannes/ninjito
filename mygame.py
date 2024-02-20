import sys
import pygame

class Game:
    def __init__(self):  
        pygame.init() # pygame instance

        pygame.display.set_caption('Ninjito')
        self.screen = pygame.display.set_mode((640, 480)) # set window/screen width x height [screen orientation]

        self.clock = pygame.time.Clock()
        self.img =pygame.image.load('data/images/clouds/cloud_1.png')
        self.img_pos = [160, 260] # setting the image position
        self.movement = [False, False] # Movement for the cloud false at the beginning

    def run(self):
        while True:
            self.screen.fill((135,206,235)) #clearing the screen after every cloud movement
            self.img_pos[1] += self.movement[1] - self.movement[0]
            self.screen.blit(self.img, self.img_pos) # display image to screen with the position
            self.img.set_colorkey((0, 0, 0)) # removing the black background from the cloud
            
            # listening for any events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # if the event is exit
                    pygame.quit() # exit the game
                    sys.exit() # exit the game
                    
                if event.type == pygame.KEYDOWN: # if any key is pressed(key pressed)
                    if event.key == pygame.K_UP: # if you press the up key
                        self.movement[0] = True # 0 == move up
                    if event.key == pygame.K_DOWN: # if you press the down key
                        self.movement[1] = True # 1 == move down
                if event.type == pygame.KEYUP:# if any key is lifted up(done pressed)
                    if event.key == pygame.K_UP: # if you press the up key
                        self.movement[0] = False # 0 == move up
                    if event.key == pygame.K_DOWN: # if you press the down key
                        self.movement[1] = False # 1 == move down
            
            
            pygame.display.update()
            self.clock.tick(60)
            
Game().run()