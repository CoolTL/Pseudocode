from nicegui import ui
import seeds

from model.generator import Generator
from model.solver import Solver
from view.sudoku_view import SudokuGameView
from view.solver_view import SolverView
from view.title_screen import Titlescreen
from controller.sudoku_controller import SudokuController
from controller.sudoku_solver_controller import SolverController
from controller.start_controller import SeedController

SEEDS = seeds
solver = Solver()
sudoku_generator = Generator()
seed_controller = SeedController()

@ui.page('/')
def main_page():
    Titlescreen()

@ui.page('/easy')
def easy_page():
    game_page = SudokuGameView()
    seed, seed_name = seed_controller.get_random_seed("EASY_SEED")
    print(seed_name)
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.set_controller(sudoku_controller)

@ui.page('/medium')
def medium_page():
    game_page = SudokuGameView()
    seed, seed_name = seed_controller.get_random_seed("MEDIUM_SEED")
    print(seed_name)
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.set_controller(sudoku_controller)

@ui.page('/hard')
def hard_page():
    game_page = SudokuGameView()
    seed, seed_name = seed_controller.get_random_seed("HARD_SEED")
    print(seed_name)
    sudoku_controller = SudokuController(sudoku_generator, game_page, seed, solver)
    game_page.set_controller(sudoku_controller)

@ui.page('/solver')
def solver_page():
    solver_page = SolverView()
    solver_controller = SolverController(solver_page, solver)
    solver_page.set_controller(solver_controller)

ui.run(title="Sudoku TOR")
