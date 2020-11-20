# Import relevant libraries
import pygame
import neat
import time
import os
import random

Window_Width = 600
Window_Height = 800

Bird_Images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird1.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird2.png"))), pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird3.png")))]
Pipe_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")))
Base_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")))
Background_Image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bg.png")))

class Bird:
    Images = Bird_Images
    Max_Rotation = 25
    Rot_Vel = 20
    Animation_Time = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tilt = 0
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.Images[0]

    def jump(self):
        self.vel = -10.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        self.tick_count += 1

        d = self.vel*self.tick_count + 1.5*self.tick_count**2

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
                self.tilt -= self.Rot_Vel

    def draw(self, win):
        self.img_count += 1

        if self.img_count < self.Animation_Time:
            self.img = self.Images[0]
        elif self.img_count < self.Animation_Time*2:
            self.img = self.Images[1]
        elif self.img_count < self.Animation_Time*3:
            self.img = self.Images[2]
        elif self.img_count < self.Animation_Time*4:
            self.img = self.Images[1]
        elif self.img_count == self.Animation_Time*4 + 1:
            self.img = self.Images[0]
            self.img_count = 0

while True:
    bird.move()