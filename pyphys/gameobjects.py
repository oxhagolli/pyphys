"""
    @author: oxhagolli
    Game objects stuff
"""
import abc
import pygame


class GameObject:
    def __init__(self, source, screen):
        self.image = pygame.image.load(source)
        self.screen = screen

    @abc.abstractmethod
    def render(self):
        pass


class VisibleObject(GameObject):
    def __init__(self, source, screen, x=0, y=0, theta=0):
        super().__init__(source, screen)
        self.x = x
        self.y = y
        self.theta = theta

    def render(self):
        rotate = pygame.transform.rotate(self.image, self.theta)
        self.screen.blit(rotate, (self.x, self.y))


class Background(GameObject):
    def __init__(self, source, screen):
        if isinstance(source, str):
            super().__init__(source, screen)
        else:
            self.image = source
            self.screen = screen

    def render(self):
        if isinstance(self.image, pygame.Surface):
            self.screen.blit(self.image, (0, 0))
        else:
            self.screen.fill(self.image)
