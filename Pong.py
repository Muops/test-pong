import random
import pygame
import sys
from pygame import *
from easygui import *

image = "/usr/share/muops/muopsstart/MuopsLogoSunSet.gif"
msg = "                           Welcome to Pong \n\n\n Rules of Pong \n\n\n Player 1 \n\n Arrow up = UP \n Arrow down = DOWN\n\n Player 2 \n\n Z = UP \n S = Down"
choices = ["OK"]
buttonbox(msg, image=image, choices=choices)

pygame.init()
fps = pygame.time.Clock()


WHITE = (255, 255, 255)
ORANGE = (255, 140, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH // 2
HALF_PAD_HEIGHT = PAD_HEIGHT // 2
ball_pos = [0, 0]
ball_vel = [0, 0]
paddle1_vel = 0
paddle2_vel = 0
l_score = 0
r_score = 0


window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption("Muops Pong")

