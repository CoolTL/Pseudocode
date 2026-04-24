from nicegui import ui

class NiceguiMain:
    def __init__(self):
        self.cells = {}
        self.num_pad_buttons = []
        self.setup_screen()
        #self.cells[1,5].set_text("test")

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
