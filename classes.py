__author__ = 'Thomas'
"""Defining classes Cell anaaaad Game used in the Minesweeper"""

import sys
from random import randrange

from properties import *


class Cell:
    """Each Cell has a tuple of position, a value between 0 and 8 (>=9 for a
    mined cell), and booleans hasFlag if the player marked the cell as mined
    and isRevealed if the player revealed the cell"""

    def __init__(self, position):
        self.position = position
        self.value = 0
        self.hasFlag = False
        self.isRevealed = False

    def is_clicked(self):
        self.isRevealed = True

    def is_marked(self):
        self.hasFlag = not self.hasFlag
        return self.hasFlag


class Game:
    """A game has a string difficulty, a grid of cells stored as a dictionary
     {position: cell} and the number of remaining cells (non clicked)"""

    def __init__(self, difficulty):
        self.grid = {}
        self.remaining_cells = []
        self.flagged_cells = 0

        try:
            if difficulty == "easy":
                self.nb_mines = NB_MINES_EASY
                self.field_size = FIELD_SIZE_EASY
            elif difficulty == "medium":
                self.nb_mines = NB_MINES_MEDIUM
                self.field_size = FIELD_SIZE_MEDIUM
            elif difficulty == "hard":
                self.nb_mines = NB_MINES_HARD
                self.field_size = FIELD_SIZE_HARD
            else:
                raise ValueError

        except ValueError:
            print("Incorrect difficulty parameter while creating the game")
            sys.exit(0)

        else:
            for x in range(self.field_size[0]):
                for y in range(self.field_size[1]):
                    self.grid[(x, y)] = Cell((x, y))
                    self.remaining_cells.append((x, y))

            # Placing the mines in the field
            for i in range(self.nb_mines):
                index = randrange(len(self.remaining_cells))
                mine_position = self.remaining_cells[index]
                self.grid[mine_position].value = 9
                del (self.remaining_cells[index])

                # Determining cell values
                for cell in self.get_neighbors(mine_position):
                    cell.value += 1

    def is_clicked(self, cell_position):

        if cell_position in self.remaining_cells:
            del(self.remaining_cells[self.remaining_cells.index(cell_position)])
        self.grid[cell_position].is_clicked()

        if self.grid[cell_position].value == 0:  # Discovering adjacent cells if this one is empty
            return self.grid[cell_position].value, {cell.position: 0 for cell in self.get_neighbors(cell_position)
                                                    if not cell.isRevealed}
        else:
            return self.grid[cell_position].value, {}

    def is_marked(self, cell_position):
        """Change the flag state on the cell and returns its new value, updates the flagged_cells value"""
        flag = self.grid[cell_position].is_marked()
        if flag:
            self.flagged_cells += 1
            return True
        else:
            self.flagged_cells -= 1
        return False

    def has_flag(self, cell_position):
        """Returns a boolean showing if the cell has a flag"""
        return self.grid[cell_position].hasFlag

    def is_revealed(self, cell_position):
        """Returns a boolean showing if the cell is already revealed"""
        return self.grid[cell_position].isRevealed

    def get_neighbors(self, cell_position):
        """Returns the adjacent cells to the one in the parameters"""
        neighbors = []
        for i in range(-1, 2):
                for j in range(-1, 2):
                    if (cell_position[0] + i, cell_position[1] + j) in self.grid:
                        neighbors.append(self.grid[(cell_position[0] + i, cell_position[1] + j)])
        return neighbors


class Button:
    def __init__(self, image):
        self.image = image
        self.position = (0, 0)
        self.size = (0, 0)

    def is_clicked(self, click_position):
        return self.position[0] <= click_position[0] <= self.position[0] + self.size[0] \
            and self.position[1] <= click_position[1] <= self.position[1] + self.size[1]
