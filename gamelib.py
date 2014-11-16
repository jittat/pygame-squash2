import pygame
from pygame.locals import *

class SimpleGame:

    def __init__(self,
                 title,
                 window_size=(640,480),
                 fps=60):
        self.title = title
        self.window_size = window_size
        self.fps = fps

        self.terminated = False

    def game_init(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.display = pygame.display.set_mode(self.window_size)
        pygame.display.set_caption(self.title)
        self.font = pygame.font.SysFont("monospace", 20)        

    def terminate(self):
        self.terminated = True

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.terminate()
            elif event.type == KEYDOWN:
                self.onKeyUp(event.key)
            elif event.type ==KEYUP:
                self.onKeyDown(event.key)

    def run(self):
        self.game_init()
        while not self.terminated:
            self.handle_events()

            self.update()
            self.render()
            self.clock.tick(self.fps)
    
    def init(self):
        pass

    def update(self):
        pass

    def render(self):
        pass

    def onKeyDown(self, key):
        pass

    def onKeyUp(self, key):
        pass
