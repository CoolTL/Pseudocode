from nicegui import ui

class NiceguiMain:
    def __init__(self):
        self.cells = {}
        self.num_pad_buttons = []
        self.setup_screen()

    def setup_screen(self):
        with ui.row():
            # Sudoku grid
            with ui.card():
                with ui.grid(columns=9):
                    for row in range(0, 9):
                        for col in range(0, 9):
                            self.cells[(row, col)] = ui.button("")
            # Number pad
            with ui.card():
                with ui.grid(columns=3):
                    for i in range (0, 9):
                        button = ui.button(f"{i+1}")
                        self.num_pad_buttons.append(button)

    def sudoku_num_pressed(self):
        """ Selects a button on the sudoku grid """
        pass

    def get_sudoku(self):
        """ This method returns a full numpy matrix of the sudoku for the controller/checker """
        pass

    def change_num(self, x, y, num):
        """ This gets called by the controller to change numbers on the sudoku grid """
        self.cells[x,y].set_text(f"{num}")
