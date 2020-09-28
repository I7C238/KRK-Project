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

def draw_board_lines():
    # Horizontal
    pygame.draw.line(screen, LINE_COLOR, (0, CELL_SIZE), (WIDTH, CELL_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * CELL_SIZE), (WIDTH, 2 * CELL_SIZE), LINE_WIDTH)

    # Vertical
    pygame.draw.line(screen, LINE_COLOR, (CELL_SIZE, 0), (CELL_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * CELL_SIZE, 0), (2 * CELL_SIZE, HEIGHT), LINE_WIDTH)


def draw_marks():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                screen.blit(O, (int(col * CELL_SIZE + CELL_SIZE // 2) - 50, int(row * CELL_SIZE + CELL_SIZE // 2) - 50))
            elif board[row][col] == 2:
                screen.blit(X, (int(col * CELL_SIZE + CELL_SIZE // 2) - 50, int(row * CELL_SIZE + CELL_SIZE // 2) - 50))


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


def draw_vertical_win_line(col, player):
    posX = col * CELL_SIZE + CELL_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (posX, 15), (posX, HEIGHT - 15), LINE_WIDTH)


def draw_horizontal_win_line(row, player):
    posY = row * CELL_SIZE + CELL_SIZE // 2

    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, posY), (WIDTH - 15, posY), WIN_LINE_WIDTH)


def draw_asc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, HEIGHT - 15), (WIDTH - 15, 15), WIN_LINE_WIDTH)


def draw_desc_diagonal(player):
    if player == 1:
        color = CIRCLE_COLOR
    elif player == 2:
        color = CROSS_COLOR

    pygame.draw.line(screen, color, (15, 15), (WIDTH - 15, HEIGHT - 15), WIN_LINE_WIDTH)


def restart_game():
    screen.fill(BG_COLOR)
    draw_board_lines()
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

def back_menu():
    screen.fill(BG_COLOR)
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0

# Main
def main():
    screen.fill(BG_COLOR)
    run = True

    draw_board_lines()

    # Player 1 = X 2 = O
    player = 1

    # Game Over
    game_over = False

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:

                mouseX = event.pos[0]  # x
                mouseY = event.pos[1]  # y

                clicked_row = int(mouseY // CELL_SIZE)
                clicked_col = int(mouseX // CELL_SIZE)

                if is_cell_available(clicked_row, clicked_col):

                    cell_click(clicked_row, clicked_col, player)
                    if check_winner(player):
                        game_over = True
                    player = player % 2 + 1

                    draw_marks()
            # Restart
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    restart_game()
                    player = 1
                    game_over = False
            # Back to Menu
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    back_menu()

        pygame.display.update()


def main_menu():
    run = True
    while run:
        screen.blit(BG, (0,0))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()
    pygame.mixer.stop()
    pygame.quit()


main_menu()