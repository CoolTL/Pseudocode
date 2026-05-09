from nicegui import ui
from view.sudoku_view_abc import SudokuView
import numpy as np

class SolverView(SudokuView):
    """ View for the sudoku games """
    def __init__(self):
        super().__init__()

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
                                                    lbl = ui.label("").classes('text-[12px] leading-none text-black m-auto')
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
            # Solve button
            with ui.card():
                ui.button("Solve sudoku", on_click=lambda: self.controller.solve_sudoku())

    def numpad_num_pressed(self, num):
        """ Change the selected cells number """
        if self.selected_cell:
            self.change_num(self.selected_cell_x, self.selected_cell_y, num)

    def solve_completed(self, bool):
        """ Notifies whether solving suceeded or not """
        if bool:
            ui.notify("Solve suceeded!")
        else:
            ui.notify("Solve failed, sudoku invalid.")

    def unselect_button(self):
        """ Used for unselecting the final button when solved """
        if self.selected_cell:
            self.selected_cell.set_background_color("#5898D4")

    def place_num(self, x, y, num):
        """ Method that doesn't toggle numbers, used by the controller when the sudoku is solved """
        self.main_labels[(x, y)].set_text(str(num))
