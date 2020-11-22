import pygame
import os
import random

Pipe_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))


class Pipe:
    """
    Pipe object
    """
    Gap = 200
    Velocity = 5

    def __init__(self, x):
        """
        Create pipe object
        :param x: int
        :return: None
        """
        self.x = x
        self.height = 0
        self.gap = 100

        self.top = 0
        self.bottom = 0
        self.Pipe_Top = pygame.transform.flip(Pipe_Image, False, True)
        self.Pipe_Bottom = Pipe_Image

        self.passed = False
        self.set_height()

    def set_height(self):
        """
        sets height of the pipe, from top of screen
        :return: None
        """
        self.height = random.randrange(50, 450)
        self.top = self.height - self.Pipe_Top.get_height()
        self.bottom = self.height + self.Gap

    def move(self):
        """
        move pipe depending on velocity of the game
        :return: None
        """
        self.x -= self.Velocity

    def draw(self, win):
        """
        draws pipes from bottom and top
        :param win: window/ground
        :return: None
        """
        win.blit(self.Pipe_Top, (self.x, self.top))
        win.blit(self.Pipe_Bottom, (self.x, self.bottom))

    def crash(self, bird):
        """
        returns True if bord collides with pipe
        :param bird: The Bird
        :return: Bool
        """
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.Pipe_Top)
        bottom_mask = pygame.mask.from_surface(self.Pipe_Bottom)

        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask, top_offset)

        if t_point or b_point:
            return True

        return False
