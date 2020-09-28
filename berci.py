import pygame
import sys
import numpy
import os

pygame.init()
# Window
WIDTH, HEIGHT = 600, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Caption
pygame.display.set_caption('KRK: TicTacToe')
# Font
game_font = pygame.font.Font('assets/ka1.ttf', 40)

# Lines
LINE_WIDTH = 15
WIN_LINE_WIDTH = 15

# Board
BOARD_ROWS = 3
BOARD_COLS = 3
CELL_SIZE = 200
SPACE = 55

# O AND X
CIRCLE_RADIUS = 100
CIRCLE_WIDTH = 100
CROSS_WIDTH = 25

# Images
X = pygame.image.load(os.path.join("assets", "X.png"))
O = pygame.image.load(os.path.join("assets", "O.png"))

# Colors
RED = (255, 0, 0)
BG_COLOR = (255, 255, 255)
LINE_COLOR = (0, 0, 0)
CIRCLE_COLOR = (255, 0, 0)
CROSS_COLOR = (0, 0, 0)

# Buttons
color_light = (170,170,170)
color_dark = (100,100,100)
text = game_font.render('quit' , True , (255,255,255))

# Screen
screen.fill(BG_COLOR)

# Menu BackGround
BG = pygame.image.load(os.path.join("assets", "background.png"))
# Board
board = numpy.zeros((BOARD_ROWS, BOARD_COLS))

def cell_click(row, col, player):
    board[row][col] = player


def is_cell_available(row, col):
    return board[row][col] == 0


def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 0:
                return False

    return True


def check_winner(player):
    # vertical
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_win_line(col, player)
            return True

    # horizontal
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_win_line(row, player)
            return True

    # cross right diagonal (növekvő átló)
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal(player)
        return True

    # cross left diagonal (csökkenő átló)
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True

    return False

