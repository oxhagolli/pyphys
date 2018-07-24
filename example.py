import pygame

from pyphys import core


class Example(core.EngineBase):

    def setup(self):
        pygame.display.set_mode((640, 480))
        self.frame_rate = 60

    def update(self):
        pass


if __name__ == "__main__":
    game = Example()
