import pygame
from pygame.locals import *

import gamelib

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')

    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
        self.x = 0

    def on_key_up(self,k):
        print 'UP: ',k
        
    def on_key_down(self,k):
        print 'DOWN: ',k

    def update(self):
        self.x += 1

    def render(self, surface):
        pygame.draw.circle(surface, SquashGame.WHITE, (self.x, 100), 10, 0)


def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()
