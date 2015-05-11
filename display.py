__author__ = 'Thomas'
"""Contains functions used for the display"""
import pygame.display
import pygame.font

from properties import *

cell_size = 1
# Pixel area covered by cells (top left/bottom right corners)
field_coord = ((0, 0), (0, 0))
# Images to be resized
cell_img = CELL_IMG
flag_img = FLAG_IMG
mine_img = MINE_IMG
zero_img = ZERO_IMG
one_img = ONE_IMG
two_img = TWO_IMG
three_img = THREE_IMG
four_img = FOUR_IMG
five_img = FIVE_IMG
six_img = SIX_IMG
seven_img = SEVEN_IMG
eight_img = EIGHT_IMG


def initialize():
    """Creates the program window"""

    # Icon
    pygame.display.set_icon(WINDOW_ICON)
    pygame.display.set_caption("My Minesweeper")

    # Background
    display_clear()

    pygame.display.flip()


def display_clear():
    """Erases everything on the screen"""
    background = pygame.Surface(WINDOW_SIZE).convert()
    background.fill((250, 250, 250))
    WINDOW.blit(background, (0, 0))

    pygame.display.flip()


def draw_button(button):
    """Draws the button on screen"""
    WINDOW.blit(pygame.transform.scale(button.image, button.size), button.position)
    pygame.display.flip()


def display_home_screen(play_btn, help_btn, quit_btn):
    """Displays the home screen"""
    display_clear()

    play_btn.size = help_btn.size = quit_btn.size = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//3 - 30)
    play_btn.position = ((WINDOW_SIZE[0] - play_btn.size[0])//2, 20)
    help_btn.position = ((WINDOW_SIZE[0] - help_btn.size[0])//2, play_btn.size[1] + 45)
    quit_btn.position = ((WINDOW_SIZE[0] - quit_btn.size[0])//2, play_btn.size[1] + help_btn.size[1] + 70)

    draw_button(play_btn)
    draw_button(help_btn)
    draw_button(quit_btn)


def display_difficulty_screen(easy_btn, medium_btn, hard_btn):
    """Displays the screen to choose the game difficulty"""
    display_clear()

    font = pygame.font.SysFont(POLICE, 2 * TXT_SIZE)

    text_title = font.render("Chose a difficulty", 1, (0, 0, 0))

    WINDOW.blit(text_title, (WINDOW_SIZE[0]//2 - text_title.get_width()//2, TXT_SIZE + 10))

    easy_btn.size = medium_btn.size = hard_btn.size = (WINDOW_SIZE[0]//3 - 10, int(WINDOW_SIZE[1]//4.8))
    easy_btn.position = (5, (WINDOW_SIZE[1] - easy_btn.size[1])//2)
    medium_btn.position = (15 + easy_btn.size[0], (WINDOW_SIZE[1] - medium_btn.size[1])//2)
    hard_btn.position = (25 + easy_btn.size[0] + medium_btn.size[0], (WINDOW_SIZE[1] - hard_btn.size[1])//2)

    draw_button(easy_btn)
    draw_button(medium_btn)
    draw_button(hard_btn)


def display_help_screen():
    """Displays the help screen"""
    display_clear()

    font = pygame.font.SysFont(POLICE, TXT_SIZE)
    text_title = font.render("HOW TO PLAY", 1, (0, 0, 0))
    text_help = font.render("Left click to reveal a cell.", 1, (0, 0, 0))
    text_help_2 = font.render("Right click to flag a cell.", 1, (0, 0, 0))
    text_help_3 = font.render("Click to go back.", 1, (0, 0, 0))

    WINDOW.blit(text_title, (WINDOW_SIZE[0]//2 - text_title.get_width()//2, TXT_SIZE + 10))
    WINDOW.blit(text_help, (10, 2 * TXT_SIZE + 70))
    WINDOW.blit(text_help_2, (10, 3 * TXT_SIZE + 130))
    WINDOW.blit(text_help_3, (WINDOW_SIZE[0]//2 - text_help_3.get_width()//2, 4 * TXT_SIZE + 240))
    pygame.display.flip()


def display_game_screen(difficulty):
    """Displays the playing screen at the beginning of a game"""
    global cell_size, field_coord
    display_clear()

    font = pygame.font.SysFont(POLICE, TXT_SIZE)
    # Displaying difficulty
    text_diff = font.render("Difficulty: ", 1, (0, 0, 0))
    if difficulty == "easy":
        text_diff_2 = font.render("Easy", 1, (0, 255, 0))
        show_mines_left(NB_MINES_EASY)
        cell_size = min(WINDOW_SIZE[0]//FIELD_SIZE_EASY[0], (WINDOW_SIZE[1] - HEADER_SIZE)//FIELD_SIZE_EASY[1])
        field_coord = (((WINDOW_SIZE[0] - cell_size * FIELD_SIZE_EASY[0])//2,
                        (WINDOW_SIZE[1] + HEADER_SIZE - cell_size * FIELD_SIZE_EASY[1])//2),
                       ((WINDOW_SIZE[0] + cell_size * FIELD_SIZE_EASY[0])//2,
                        (HEADER_SIZE + WINDOW_SIZE[1] + cell_size * FIELD_SIZE_EASY[1])//2))
        resize_cell_img()
        for x in range(FIELD_SIZE_EASY[0]):
            for y in range(FIELD_SIZE_EASY[1]):
                WINDOW.blit(cell_img, cell_to_pixel((x, y)))

    elif difficulty == "medium":
        text_diff_2 = font.render("Medium", 1, (255, 255, 0))
        show_mines_left(NB_MINES_MEDIUM)
        cell_size = min(WINDOW_SIZE[0]//FIELD_SIZE_MEDIUM[0], (WINDOW_SIZE[1] - HEADER_SIZE)//FIELD_SIZE_MEDIUM[1])
        field_coord = (((WINDOW_SIZE[0] - cell_size * FIELD_SIZE_MEDIUM[0])//2,
                       (WINDOW_SIZE[1] + HEADER_SIZE - cell_size * FIELD_SIZE_MEDIUM[1])//2),
                       ((WINDOW_SIZE[0] + cell_size * FIELD_SIZE_MEDIUM[0])//2,
                        (HEADER_SIZE + WINDOW_SIZE[1] + cell_size * FIELD_SIZE_MEDIUM[1])//2))
        resize_cell_img()
        for x in range(FIELD_SIZE_MEDIUM[0]):
            for y in range(FIELD_SIZE_MEDIUM[1]):
                WINDOW.blit(cell_img, cell_to_pixel((x, y)))

    else:
        text_diff_2 = font.render("Hard", 1, (255, 0, 0))
        show_mines_left(NB_MINES_HARD)
        cell_size = min(WINDOW_SIZE[0]//FIELD_SIZE_HARD[0], (WINDOW_SIZE[1] - HEADER_SIZE)//FIELD_SIZE_HARD[1])
        field_coord = (((WINDOW_SIZE[0] - cell_size * FIELD_SIZE_HARD[0])//2,
                        (WINDOW_SIZE[1] + HEADER_SIZE - cell_size * FIELD_SIZE_HARD[1])//2),
                       ((WINDOW_SIZE[0] + cell_size * FIELD_SIZE_HARD[0])//2,
                        (HEADER_SIZE + WINDOW_SIZE[1] + cell_size * FIELD_SIZE_HARD[1])//2))
        resize_cell_img()
        for x in range(FIELD_SIZE_HARD[0]):
            for y in range(FIELD_SIZE_HARD[1]):
                WINDOW.blit(cell_img, cell_to_pixel((x, y)))

    WINDOW.blit(text_diff, (10, (HEADER_SIZE - TXT_SIZE)/2))
    WINDOW.blit(text_diff_2, (153, (HEADER_SIZE - TXT_SIZE)/2))

    pygame.display.flip()


def display_end_screen(win, home_btn, quit_btn):
    """Displays the screen at the end of a game (won or lost), win is a boolean to indicate the result of the game"""
    display_clear()

    font = pygame.font.SysFont(POLICE, 2 * TXT_SIZE)

    if win:
        text_title = font.render("YOU WON !", 1, (0, 0, 0))
    else:
        text_title = font.render("YOU LOST...", 1, (0, 0, 0))

    WINDOW.blit(text_title, (WINDOW_SIZE[0]//2 - text_title.get_width()//2, TXT_SIZE + 10))

    home_btn.size = quit_btn.size = (WINDOW_SIZE[0]//2, WINDOW_SIZE[1]//3 - 30)
    home_btn.position = ((WINDOW_SIZE[0] - home_btn.size[0])//2, home_btn.size[1] + 45)
    quit_btn.position = ((WINDOW_SIZE[0] - quit_btn.size[0])//2, 2 * home_btn.size[1] + 70)

    draw_button(home_btn)
    draw_button(quit_btn)


def menu_click(position, screen, first_btn, second_btn, third_btn):
    """Returns booleans based on context if a button is clicked, used to navigate in the menu"""
    if screen == "home":
        # Play button
        if first_btn.is_clicked(position):
            return False, True, False, True  # home_screen, difficulty_screen, help_screen, game_running

        # Help button
        elif second_btn.is_clicked(position):
            return False, False, True, True  # home_screen, difficulty_screen, help_screen, game_running

        # Quit button
        elif third_btn.is_clicked(position):
            return False, False, False, False  # home_screen, difficulty_screen, help_screen, game_running

        # No button clicked
        else:
            return True, False, False, True

    elif screen == "difficulty":
        # Easy button
        if first_btn.is_clicked(position):
            return False, True, "easy"  # difficulty_screen, game_screen, difficulty
        # Medium button
        elif second_btn.is_clicked(position):
            return False, True, "medium"  # difficulty_screen, game_screen, difficulty
        # Hard button
        elif third_btn.is_clicked(position):
            return False, True, "hard"  # difficulty_screen, game_screen, difficulty

        # No button clicked
        else:
            return True, False, ""

    elif screen == "end":
        # Home button
        if first_btn.is_clicked(position):
            return False, True, True  # end_screen, home_screen, game_running
        # Quit button
        elif second_btn.is_clicked(position):
            return False, False, False  # end_screen, home_screen, game_running

        # No button clicked
        else:
            return True, False, True


def pixel_to_cell(position):
    """Converts a tuple of pixel coordinates to a tuple of cell position in a list"""
    global cell_size, field_coord

    if field_coord[0][0] <= position[0] <= field_coord[1][0] and field_coord[0][1] <= position[1] <= field_coord[1][1]:
        return [((position[0] - field_coord[0][0]) // cell_size, (position[1] - field_coord[0][1]) // cell_size)]
    else:
        return []


def cell_to_pixel(position):
    """Converts a cell position to top left corner pixel coordinates"""
    global cell_size, field_coord
    return field_coord[0][0] + position[0] * cell_size, field_coord[0][1] + position[1] * cell_size


def reveal_cell(value, position):
    """Displays the image of the cell in the grid based on its value"""
    global cell_size, mine_img, cell_img, zero_img, one_img, two_img, three_img, four_img, five_img, six_img,\
        seven_img, eight_img, field_coord

    if value == 0:
        cell_image = zero_img
    elif value == 1:
        cell_image = one_img
    elif value == 2:
        cell_image = two_img
    elif value == 3:
        cell_image = three_img
    elif value == 4:
        cell_image = four_img
    elif value == 5:
        cell_image = five_img
    elif value == 6:
        cell_image = six_img
    elif value == 7:
        cell_image = seven_img
    elif value == 8:
        cell_image = eight_img
    else:
        cell_image = mine_img

    WINDOW.blit(cell_image, (field_coord[0][0] + position[0] * cell_size, field_coord[0][1] + position[1] * cell_size))
    pygame.display.flip()


def flag_cell(flag, position):
    """Displays/removes a flag on the clicked cell"""
    global cell_size, flag_img, cell_img

    if flag:
        flag_image = flag_img
    else:
        flag_image = cell_img
    WINDOW.blit(flag_image, (field_coord[0][0] + position[0] * cell_size, field_coord[0][1] + position[1] * cell_size))
    pygame.display.flip()


def show_mines_left(nb_mines_left):
    """Displays the number of mines left (not flagged)"""

    eraser = pygame.Surface((212, TXT_SIZE)).convert()
    eraser.fill((250, 250, 250))
    WINDOW.blit(eraser, (WINDOW_SIZE[0] - 222, (HEADER_SIZE - TXT_SIZE)/2))

    font = pygame.font.SysFont(POLICE, TXT_SIZE)
    text_mines_left = font.render("Mines left: {}".format(nb_mines_left), 1, (0, 0, 0))
    WINDOW.blit(text_mines_left, (WINDOW_SIZE[0] - 222, (HEADER_SIZE - TXT_SIZE)/2))

    pygame.display.flip()


def resize_cell_img():
    """Resizes all cells images to fit screen"""
    global cell_size, flag_img, mine_img, cell_img, zero_img, one_img, two_img, three_img, four_img, five_img, six_img,\
        seven_img, eight_img

    flag_img = pygame.transform.scale(FLAG_IMG, (cell_size, cell_size))
    mine_img = pygame.transform.scale(MINE_IMG, (cell_size, cell_size))
    cell_img = pygame.transform.scale(CELL_IMG, (cell_size, cell_size))
    zero_img = pygame.transform.scale(ZERO_IMG, (cell_size, cell_size))
    one_img = pygame.transform.scale(ONE_IMG, (cell_size, cell_size))
    two_img = pygame.transform.scale(TWO_IMG, (cell_size, cell_size))
    three_img = pygame.transform.scale(THREE_IMG, (cell_size, cell_size))
    four_img = pygame.transform.scale(FOUR_IMG, (cell_size, cell_size))
    five_img = pygame.transform.scale(FIVE_IMG, (cell_size, cell_size))
    six_img = pygame.transform.scale(SIX_IMG, (cell_size, cell_size))
    seven_img = pygame.transform.scale(SEVEN_IMG, (cell_size, cell_size))
    eight_img = pygame.transform.scale(EIGHT_IMG, (cell_size, cell_size))
