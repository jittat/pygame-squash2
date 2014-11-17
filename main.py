import pygame
from pygame.locals import *

import gamelib
from elements import Ball, Player

class SquashGame(gamelib.SimpleGame):
    BLACK = pygame.Color('black')
    WHITE = pygame.Color('white')
    GREEN = pygame.Color('green')
    
    def __init__(self):
        super(SquashGame, self).__init__('Squash', SquashGame.BLACK)
        self.ball = Ball(radius=10,
                         color=SquashGame.WHITE,
                         pos=(self.window_size[0]/2,
                              self.window_size[1]/2),
                         speed=(200,50))
        self.player = Player(pos=100,
                             color=SquashGame.GREEN)
        self.score = 0


    def init(self):
        super(SquashGame, self).init()
        self.render_score()

    def update(self):
        self.ball.move(1./self.fps, self.surface, self.player)

        if pygame.key.get_pressed()[K_UP]:
            self.player.pos -= 5
        elif pygame.key.get_pressed()[K_DOWN]:
            self.player.pos += 5
        
        if self.player.can_hit(self.ball):
            self.score += 1
            self.render_score()
            print "HIT"
            self.ball.bounce_player()
        
    def render_score(self):
        self.score_image = self.font.render("Score = %d" % self.score, 0, SquashGame.WHITE)

    def render(self, surface):
        self.ball.render(surface)
        self.player.render(surface)
        surface.blit(self.score_image, (10,10))

def main():
    game = SquashGame()
    game.run()

if __name__ == '__main__':
    main()
