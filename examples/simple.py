import pygame

from pyphys import core, gameobjects


class Example(core.EngineBase):

    def setup(self):
        self.screen = pygame.display.set_mode((640, 480))  # Set the size of the screen
        self.frame_rate = 60  # Set the desired frame rate (remove this if you'd like max frame rate)

        background = gameobjects.Background((255, 255, 255), self.screen)
        self.register_background(background)

        car = gameobjects.VisibleObject("shared/car.png", self.screen, x=100, y=100, theta=0)
        self.register_object(car, 1)

    def update(self):
        pass


if __name__ == "__main__":
    game = Example()
