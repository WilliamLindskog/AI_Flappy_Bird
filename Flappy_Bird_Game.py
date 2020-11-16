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

while True:
    bird.move()