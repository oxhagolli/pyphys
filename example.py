import pygame

from pyphys import core


class Example(core.EngineBase):

    def setup(self):
        pygame.display.set_mode((640, 480))

    def update(self):
        pass


if __name__ == "__main__":
    game = Example()
