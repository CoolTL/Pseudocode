from nicegui import ui
import numpy as np

class NiceguiMain:
    def __init__(self):
        self.controller = None

        # We have dictionaries for each cell, each main label, which is the label containing the final number, and a dictionary for notes which is the small numbers
        self.cells = {}
        self.main_labels = {}
        self.notes = {}
        self.selected_cell = None
        self.num_pad_buttons = []
        self.setup_screen()
        self.note_enabled = False
    def get_controller(self, controller):
        self.controller = controller

    def setup_screen(self):
        # Back button
        ui.button(icon='arrow_back', on_click=lambda: ui.navigate.to('/'))
        with ui.row():
            # Sudoku grid
            with ui.card():
                with ui.grid(columns=3).classes('gap-2 bg-white border-4 border-white'):
                    for block_row in range(0, 3):
                        for block_col in range(0, 3):
                            with ui.grid(columns=3).classes('gap-0'):
                                for row in range(0, 3):
                                    for col in range(0, 3):
                                        actual_row = block_row * 3 + row
                                        actual_col = block_col * 3 + col
                                        btn = ui.button("", on_click=lambda r=actual_row, c=actual_col: self.sudoku_num_pressed(self.cells[(r,c)], r, c)).classes('w-[60px] h-[60px] p-0 relative overflow-hidden')
                                        self.cells[(actual_row, actual_col)] = btn
                                        # Add a 3x3 grid inside the button for notes
                                        with btn:
                                            with ui.grid(columns=3).classes('w-full h-full gap-0 p-1'):
                                                for n in range(1, 10):
                                                    # Store label text is empty by default
                                                    lbl = ui.label("").classes('text-[8px] leading-none text-gray-500 m-auto')
                                                    self.notes[(actual_row, actual_col, n)] = lbl
                                            # This is the main labels for big numbers in the cells
                                            main_lbl = ui.label("").classes('absolute-center text-xl text-black font-bold')
                                            self.main_labels[(actual_row, actual_col)] = main_lbl
            # Number pad
            with ui.card():
                with ui.grid(columns=3):
                    for i in range (0, 9):
                        button = ui.button(f"{i+1}", on_click=lambda n=i+1: self.numpad_num_pressed(n)).classes('w-[50px] h-[50px]')
                        self.num_pad_buttons.append(button)
            # Hint button
            with ui.card():
                self.hint_button = ui.button("Hint", on_click=lambda: self.change_num(self.selected_cell_x, self.selected_cell_y, self.controller.give_hint(self.selected_cell_x, self.selected_cell_y)))
                ui.toggle(["Normal", "Notes"], value="Normal")
    def complete(self):
        with ui.dialog() as dialog, ui.card():
            ui.label("You did it! Now kill yourself")
            ui.button("OK", on_click=dialog.close)
        dialog.open()

    def numpad_num_pressed(self, num):
        """ Change the selected cells number """
        if self.selected_cell:
            if self.note_enabled:
                self.add_note(self.selected_cell_x, self.selected_cell_y, num)
            else:
                self.change_num(self.selected_cell_x, self.selected_cell_y, num)
                self.controller.game_update()


    def sudoku_num_pressed(self, button, x, y):
        """ Selects a button on the sudoku grid """
        self.selected_cell = button
        self.selected_cell_x = x
        self.selected_cell_y = y

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

    def note_toggle(self):
        """ Toggles if note taking is enabled or not """
        self.note_enabled = True

    def add_note(self, x, y, num):
        """ This takes coordinates and a number and adds it as a note to a cell """
        label = self.notes.get((x, y, num))
        if label:
            # This toggles whether the note is there or not
            label.set_text(num if label.text == "" else "")

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
