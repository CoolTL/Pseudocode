import numpy as np

class SudokuController:
    """ Connects the model and view """
    
    def __init__(self, model, view, seed, solver):
        self.model = model
        self.view = view
        self.seed = seed
        self.solver = solver
        self.completed = None
        self.setup_game()

    def get_seed(self):
        """ This method gets the start game setup from the model """
        seed = self.model.prepare_seed(self.seed)
        seed = self.model.convert_to_numbers(seed)
        return self.model.convert_to_matrix(seed)

    def game_update(self):
        """ Checks if the sudoku is solved, and tells the view if so"""
        grid = self.view.get_sudoku()
        if np.array_equal(self.completed, grid):
            self.view.complete()

    def give_hint(self, x, y):
        """ Return the correct value at the given coordinates """
        return self.completed[x][y]

    def setup_game(self):
        """ Function for setting up the game """
        layout = self.get_seed()
        # Now we call the the method in the view to put the numbers into the grid
        row_num = 0
        col_num = 0
        for row in layout:
            for num in row:
                if num != 0:
                    self.view.change_num(row_num, col_num, num)
                    self.view.disable_num(row_num, col_num)
                col_num += 1
            col_num = 0
            row_num += 1
        grid = self.view.get_sudoku()
        self.completed = grid
        # Debug code:
        if self.solver.solve(grid):
            print(self.completed)
            print("Der er en løsning")
        else:
            print("ingen løsning")
