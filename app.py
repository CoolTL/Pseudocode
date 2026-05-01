from nicegui import ui

import seeds

from model.generator import Generator
from view.nicegui import NiceguiMain
from controller.sudoku_controller import SudokuController
from model.solver import Solver

SEEDS = seeds

solver = Solver()
sudoku_generator = Generator()
game_page = NiceguiMain()
sudoku_controller = SudokuController(sudoku_generator, game_page, SEEDS, solver)
game_page.get_controller(sudoku_controller)

ui.run()
