import pygame
import os

Ground_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))


class Ground:
    """
    Moving ground in the game
    """
    Velocity = 5
    Width = Ground_Image.get_width()
    Image = Ground_Image

    def __init__(self, y):
        """
        initializes ground
        :param y: Int
        :return: None
        """
        self.y = y
        self.x1 = 0
        self.x2 = self.Width

    def move(self):
        """
        move the floor, looks like scrolling
        :return: None
        """
        self.x1 -= self.Velocity
        self.x2 -= self.Velocity

        if self.x1 + self.Width < 0:
            self.x1 = self.x2 + self.Width

        if self.x2 + self.Width < 0:
            self.x2 = self.x1 + self.Width

    def draw(self, win):
        """
        Draws ground, two images moving together.
        :param win:
        :return: None
        """
        win.blit(self.Image, (self.x1, self.y))
        win.blit(self.Image, (self.x2, self.y))

