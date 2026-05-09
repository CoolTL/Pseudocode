from nicegui import ui
from abc import ABC, abstractmethod
import numpy as np

class SudokuView(ABC):
    """ Abstract base class for sudoku view """
    
    def __init__(self):
        self.controller = None

        # We have dictionaries for each cell, each main label, which is the label containing the final number, and a dictionary for notes which is the small numbers
        self.cells = {}
        self.main_labels = {}
        self.notes = {}
        self.note_enabled = False
        self.selected_cell = None
        self.selected_cell_x = None
        self.selected_cell_y = None
        self.num_pad_buttons = []
        self.setup_screen()

    def set_controller(self, controller):
        self.controller = controller

    @abstractmethod
    def setup_screen(self):
        raise NotImplementedError

    @abstractmethod
    def numpad_num_pressed(self, num):
        """ Change the selected cells number """
        raise NotImplementedError


    def sudoku_num_pressed(self, button, x, y):
        """ Selects a button on the sudoku grid """
        # Highlight the button and unhighlight the previous
        if self.selected_cell:
            self.selected_cell.set_background_color("#5898D4")
        button.set_background_color("green")
        if button == self.selected_cell:
            button.set_background_color("#5898D4")
            self.selected_cell = None
            self.selected_cell_x = None
            self.selected_cell_y = None
        else:
            self.selected_cell = button
            self.selected_cell_x = x
            self.selected_cell_y = y

    def get_sudoku(self):
        """ This method returns a full numpy matrix of the sudoku for the controller/checker """
        sudoku = np.empty((9, 9), dtype=int)
        for row in range(0, 9):
            for col in range(0, 9):
                if self.main_labels[(row, col)].text == "":
                    sudoku[row][col] = 0
                else:
                    sudoku[row][col] = int(self.main_labels[(row, col)].text)
        return sudoku

    def note_toggle(self):
        """ Toggles if note taking is enabled or not """
        self.note_enabled = not self.note_enabled

    def add_note(self, x, y, num):
        """ This takes coordinates and a number and adds it as a note to a cell """
        # Dont add notes if a main number is in the cell
        if self.main_labels[(x, y)].text != "":
            return
        label = self.notes.get((x, y, num))
        if label:
            # This toggles whether the note is there or not
            if label.text == num:
                label.set_text("")
            else:
                label.set_text(num)

    def remove_all_notes(self, x, y):
        """ This removes all the notes for when you choose a number for a cell """
        for n in range(1, 10):
            self.notes[(x, y, n)].set_text("")

    def change_num(self, x, y, num):
        """ This gets called by the controller to change numbers on the sudoku grid """
        # First we remove all the notes
        self.remove_all_notes(x, y)
        # Make it so the number gets removed if the same number is inputted twice
        if self.main_labels[(x, y)].text == str(num):
            self.main_labels[(x, y)].set_text("")
        else:
            self.main_labels[(x, y)].set_text(str(num))

    def disable_num(self, x, y):
        """ Disables a button for use in setting up the board """
        self.cells[x,y].disable()

    def game_updated(self):
        """ This tells the controller when the board has changed """
        self.controller.game_update()
