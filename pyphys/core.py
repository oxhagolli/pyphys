"""
    @author: oxhagolli
    pyphys core file that helps give pygame more of a game engine feel
"""
import abc
import pygame
import time


class EngineBase:
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        pygame.init()
        self.screen = None
        self.frame_rate = -1  # Max frame rate
        self.clock = pygame.time.Clock()
        self.timedelta = 0  # Use to avoid skip-frames
        self.last_check = time.time()

        self.setup()
        loop_flag = True
        while loop_flag:
            self.update()
            self.timedelta = time.time() - self.last_check
            self.last_check = time.time()
            if self.frame_rate >= 0:
                self.clock.tick(self.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop_flag = False
        pygame.quit()

    @abc.abstractmethod
    def setup(self):
        pass

    @abc.abstractmethod
    def update(self):
        pass
