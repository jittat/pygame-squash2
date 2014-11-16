import pygame
from pygame.locals import *

import gamelib

class SquashGame(gamelib.SimpleGame):
    def on_key_up(self,k):
        print 'UP: ',k
        
    def on_key_down(self,k):
        print 'DOWN: ',k
        

def main():
    game = SquashGame('Test')
    game.run()

if __name__ == '__main__':
    main()
