"""
    @author: oxhagolli
    pyphys core file that helps give pygame more of a game engine feel
"""
import abc
import pygame


class EngineBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pygame.init()
        self.screen = None

        self.setup()
        loop_flag = True
        while loop_flag:
            self.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop_flag = False

    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
