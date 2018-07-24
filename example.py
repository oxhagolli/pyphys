import pygame

from pyphys import core


class Example(core.EngineBase):

    def setup(self):
        pygame.display.set_mode((640, 480))  # Set the size of the screen
        self.frame_rate = 60  # Set the desired frame rate (remove this if you'd like max frame rate)

    def update(self):
        pass


if __name__ == "__main__":
    game = Example()
