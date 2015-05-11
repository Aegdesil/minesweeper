__author__ = 'Thomas'
"""Main file of the program.
Tested with Python 3.2.5 and Pygame 1.9."""

import pygame.time
import pygame.event
from time import sleep

import display
from classes import *
from properties import *


def minesweeper():
    """Main function of the game"""
    display.initialize()

    game_running = True
    home_screen = True
    difficulty_screen = False
    game_screen = False
    help_screen = False
    end_screen = False
    play_btn = Button(PLAY_BTN)
    help_btn = Button(HELP_BTN)
    quit_btn = Button(QUIT_BTN)
    easy_btn = Button(EASY_BTN)
    medium_btn = Button(MEDIUM_BTN)
    hard_btn = Button(HARD_BTN)
    home_btn = Button(HOME_BTN)
    quit_replay_btn = Button(QUIT_BTN)

    # Main loop of the game
    while game_running:
        if not home_screen:
            game_running = False

        display.display_home_screen(play_btn, help_btn, quit_btn)

        # Loop of the Home screen
        while home_screen:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    home_screen = False
                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    home_screen, difficulty_screen, help_screen, game_running = \
                        display.menu_click(pygame.mouse.get_pos(), "home", play_btn, help_btn, quit_btn)
            if difficulty_screen:

                display.display_difficulty_screen(easy_btn, medium_btn, hard_btn)
            elif help_screen:
                display.display_help_screen()

        while help_screen:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    help_screen = False
                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    home_screen, help_screen = True, False
                    display.display_home_screen(play_btn, help_btn, quit_btn)

        while difficulty_screen:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    difficulty_screen = False
                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    difficulty_screen, game_screen, difficulty = \
                        display.menu_click(pygame.mouse.get_pos(), "difficulty", easy_btn, medium_btn, hard_btn)
            if game_screen:
                display.display_game_screen(difficulty)
                my_game = Game(difficulty)

        while game_screen:
            # Loop while playing
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    game_screen = False

                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    cell_clicked = display.pixel_to_cell(pygame.mouse.get_pos())
                    value = 0

                    # If there is a flag or the cell is already revealed, left click does nothing
                    if cell_clicked and not(my_game.has_flag(cell_clicked[0]) or my_game.is_revealed(cell_clicked[0])):
                        # Loop to discover nearby cells if clicked cell is empty
                        while cell_clicked:
                            cells_to_discover = {}
                            for cell in cell_clicked:
                                if not(my_game.has_flag(cell) or my_game.is_revealed(cell)):
                                    value, new_cells = my_game.is_clicked(cell)
                                    cells_to_discover.update(new_cells)
                                    display.reveal_cell(value, cell)

                            cell_clicked = cells_to_discover.keys()
                    # Mine is clicked
                    if value >= 9:
                        sleep(1)
                        game_screen, end_screen = False, True
                        display.display_end_screen(False, home_btn, quit_replay_btn)
                    # Game won
                    elif not my_game.remaining_cells:
                        game_screen, end_screen = False, True
                        display.display_end_screen(True, home_btn, quit_replay_btn)
                # Right click to flag a mine
                elif event.type == MOUSEBUTTONUP and event.button == 3:
                    cell_clicked = display.pixel_to_cell(pygame.mouse.get_pos())
                    if cell_clicked and not my_game.is_revealed(cell_clicked[0]):
                        display.flag_cell(my_game.is_marked(cell_clicked[0]), cell_clicked[0])
                        display.show_mines_left(my_game.nb_mines - my_game.flagged_cells)

        while end_screen:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    game_running = False
                    end_screen = False
                elif event.type == MOUSEBUTTONUP and event.button == 1:
                    end_screen, home_screen, game_running = \
                        display.menu_click(pygame.mouse.get_pos(), "end", home_btn, quit_btn, None)
            if home_screen:
                display.display_home_screen(play_btn, help_btn, quit_btn)

    pygame.quit()


if __name__ == '__main__':
    minesweeper()