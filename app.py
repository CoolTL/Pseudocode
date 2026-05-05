from nicegui import ui
import seeds

from model.generator import Generator
from view.sudoku_view import NiceguiMain
from controller.sudoku_controller import SudokuController
from model.solver import Solver
from view.title_screen import Titlescreen

SEEDS = seeds
solver = Solver()
sudoku_generator = Generator()

@ui.page('/')
def main_page():
    Titlescreen()

@ui.page('/easy')
def easy_page():
    game_page = NiceguiMain()
    sudoku_controller = SudokuController(sudoku_generator, game_page, SEEDS, solver)
    game_page.get_controller(sudoku_controller)

ui.run()
