from nicegui import ui
import seeds

from model.generator import Generator
from view.sudoku_view import NiceguiMain
from controller.sudoku_controller import SudokuController
from model.solver import Solver
from controller.start_controller import SeedController
from view.title_screen import Titlescreen

SEEDS = seeds
solver = Solver()
sudoku_generator = Generator()
seed_controller = SeedController()

@ui.page('/')
def main_page():
    Titlescreen()

@ui.page('/easy')
def easy_page():
    game_page = NiceguiMain()
    seed = seed_controller.get_random_seed("EASY_SEED")
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.get_controller(sudoku_controller)

@ui.page('/medium')
def medium_page():
    game_page = NiceguiMain()
    seed = seed_controller.get_random_seed("MEDIUM_SEED")
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.get_controller(sudoku_controller)

@ui.page('/hard')
def hard_page():
    game_page = NiceguiMain()
    seed = seed_controller.get_random_seed("HARD_SEED")
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.get_controller(sudoku_controller)

ui.run()
