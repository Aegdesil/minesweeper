__author__ = 'Thomas'
"""Defining constants used in the game"""

import pygame.image
from pygame.locals import *

# Size of the Field (number of cells)
FIELD_SIZE = (15, 10)
FIELD_SIZE_EASY = (9, 9)
FIELD_SIZE_MEDIUM = (16, 16)
FIELD_SIZE_HARD = (30, 16)

# Number of mines on the field on each difficulty setting
NB_MINES_EASY = 10
NB_MINES_MEDIUM = 40
NB_MINES_HARD = 99

# Size of the window (pixels)
WINDOW_SIZE = (600, 480)
HEADER_SIZE = 80

pygame.init()
WINDOW = pygame.display.set_mode(WINDOW_SIZE, DOUBLEBUF)
# Image files names
WINDOW_ICON = pygame.image.load("images/icon.png").convert_alpha()

# Cells images
MINE_IMG = pygame.image.load("images/mine.png").convert()
FLAG_IMG = pygame.image.load("images/flag.png").convert()
CELL_IMG = pygame.image.load("images/cell.png").convert()
ZERO_IMG = pygame.image.load("images/0.png").convert()
ONE_IMG = pygame.image.load("images/1.png").convert()
TWO_IMG = pygame.image.load("images/2.png").convert()
THREE_IMG = pygame.image.load("images/3.png").convert()
FOUR_IMG = pygame.image.load("images/4.png").convert()
FIVE_IMG = pygame.image.load("images/5.png").convert()
SIX_IMG = pygame.image.load("images/6.png").convert()
SEVEN_IMG = pygame.image.load("images/7.png").convert()
EIGHT_IMG = pygame.image.load("images/8.png").convert()

# Buttons images & position
# Home screen

PLAY_BTN = pygame.image.load("images/play_btn.png").convert_alpha()
HELP_BTN = pygame.image.load("images/help_btn.png").convert_alpha()
QUIT_BTN = pygame.image.load("images/quit_btn.png").convert_alpha()

# Difficulty screen

EASY_BTN = pygame.image.load("images/easy.png").convert_alpha()
MEDIUM_BTN = pygame.image.load("images/medium.png").convert_alpha()
HARD_BTN = pygame.image.load("images/hard.png").convert_alpha()

# End screen
HOME_BTN = pygame.image.load("images/home_btn.png").convert_alpha()

# Text properties
POLICE = 'Arial'
TXT_SIZE = 40
