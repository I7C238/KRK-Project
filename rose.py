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