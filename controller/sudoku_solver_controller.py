import numpy as np

class SolverController:
    """ Controller for the solver screen """
    
    def __init__(self, view, solver):
        self.view = view
        self.solver = solver

    def solve_sudoku(self):
        """ Calls the solver to try to solve the current sudoku """
        grid = self.view.get_sudoku()
        if self.solver.solve(grid):
            # Fill out the completed sudoku
            row_num = 0
            col_num = 0
            for row in grid:
                for num in row:
                    if num != 0:
                        self.view.place_num(row_num, col_num, num)
                        self.view.disable_num(row_num, col_num)
                    col_num += 1
                col_num = 0
                row_num += 1
            # Unselect the final button and notify of solved
            self.view.unselect_button()
            self.view.solve_completed(True)
        else:
            # Notify the view that the solve failed
            self.view.solve_completed(False)
