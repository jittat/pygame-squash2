import pygame
from pygame.locals import *

import gamelib

class SquashGame(gamelib.SimpleGame):
    def onKeyUp(self,k):
        print 'UP: ',k
        
    def onKeyDown(self,k):
        print 'DOWN: ',k
        

def main():
    game = SquashGame('Test')
    game.run()

if __name__ == '__main__':
    main()
