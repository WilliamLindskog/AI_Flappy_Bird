import pygame
import os

Bird_Images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))),
               pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]


class Bird:
    """
    Bird class - the Flappy Bird and its attributes
    """
    Images = Bird_Images
    Max_Rotation = 25
    Rotation_Velocity = 20
    Animation_Time = 5

    def __init__(self, x, y):
        """
        :param x: starting x (int) position
        :param y: starting y (int) position
        :return: None
        """
        self.x = x
        self.y = y
        self.tilt = 0  # tilt degrees
        self.tick_count = 0
        self.velocity = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.Images[0]

    def jump(self):
        """
        bird jumps
        :return: None
        """
        self.velocity = -10.5  # Negative due to window characteristics
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """
        bird moves
        :return: None
        """
        self.tick_count += 1
        d = self.velocity * self.tick_count + 1.5 * self.tick_count ** 2

        if d >= 16:
            d = 16

        if d < 0:
            d -= 2

        self.y = self.y + d

        if d < 0 or self.y < self.height + 50:
            if self.tilt < self.Max_Rotation:
                self.tilt = self.Max_Rotation
        else:
            if self.tilt > -90:
                self.tilt -= self.Rotation_Velocity

    def draw(self, win):
        """
        draws bird
        :param win: the window or ground
        :return: None
        """
        self.img_count += 1

        if self.img_count < self.Animation_Time:
            self.img = self.Images[0]
        elif (self.img_count < self.Animation_Time * 2) or (self.img_count < self.Animation_Time * 4):
            self.img = self.Images[1]
        elif self.img_count < self.Animation_Time * 3:
            self.img = self.Images[2]
        elif self.img_count == self.Animation_Time * 4 + 1:
            self.img = self.Images[0]
            self.img_count = 0

        if self.tilt <= -80:
            self.img = self.Images[1]
            self.img_count = self.Animation_Time * 2

        rotated_image = pygame.transform.rotate(self.img, self.tilt)
        new_rect = rotated_image.get_rect(center=self.img.get_rect(topleft=(self.x, self.y)).center)
        win.blit(rotated_image, new_rect.topleft)

    def get_mask(self):
        """
        gets the mask for the current image of the bird
        :return:
        """
        return pygame.mask.from_surface(self.img)
