from nicegui import ui
import numpy as np

class NiceguiMain:
    def __init__(self):
        self.controller = None

        self.cells = {}
        self.selected_cell = None
        self.num_pad_buttons = []
        self.setup_screen()
    def get_controller(self, controller):
        self.controller = controller

    def setup_screen(self):
        with ui.row():
            # Sudoku grid
            with ui.card():
                with ui.grid(columns=9):
                    for row in range(0, 9):
                        for col in range(0, 9):
                            self.cells[(row, col)] = ui.button("", on_click=lambda r=row, c=col: self.sudoku_num_pressed(self.cells[(r,c)]))
            # Number pad
            with ui.card():
                with ui.grid(columns=3):
                    for i in range (0, 9):
                        button = ui.button(f"{i+1}", on_click=lambda n=i+1: self.numpad_num_pressed(n))
                        self.num_pad_buttons.append(button)

    def numpad_num_pressed(self, num):
        """ Change the selected cells number """
        if self.selected_cell:
            self.selected_cell.set_text(num)

    def sudoku_num_pressed(self, button):
        """ Selects a button on the sudoku grid """
        self.selected_cell = button
        # Tell the controller something has happened
        self.game_updated()

    def get_sudoku(self):
        """ This method returns a full numpy matrix of the sudoku for the controller/checker """
        sudoku = np.empty((9, 9), dtype=int)
        for row in range(0, 9):
            for col in range(0, 9):
                if self.cells[row, col].text == "":
                    sudoku[row][col] = 0
                else:
                    sudoku[row][col] = int(self.cells[row, col].text)
        return sudoku

    def change_num(self, x, y, num):
        """ This gets called by the controller to change numbers on the sudoku grid """
        self.cells[x,y].set_text(f"{num}")

    def disable_num(self, x, y):
        """ Disables a button for use in setting up the board """
        self.cells[x,y].disable()

    def game_updated(self):
        """ This tells the controller when the board has changed """
        self.controller.game_update()
