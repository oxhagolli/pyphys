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
        self.backgrounds = []
        self.object_groups = {}
        self.setup()
        loop_flag = True
        while loop_flag:
            self.pressed = pygame.key.get_pressed()
            self.update()
            for background in self.backgrounds:
                background.render()
            for key in sorted(self.object_groups):
                for item in self.object_groups[key]:
                    item.render()
            pygame.display.flip()
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

    def register_object(self, o, level):
        if level in self.object_groups.keys():
            self.object_groups[level].append(o)
        else:
            self.object_groups[level] = [o]

    def destroy_object(self, o, level):
        self.object_groups[level].remove(o)

    def register_background(self, o):
        self.backgrounds.append(o)
