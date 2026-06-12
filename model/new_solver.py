from model.solver import Solver

class NewSolver(Solver):
    def __init__(self):
        super.__init__()

    def find_empty(self, grid):
        best_cell = None
        best_candidates = None
        for row in range(9):
            for col in range(9):
                if grid[row][col] == self.empty:
                    candidates = get_candidates(grid, row, col)
                    if best_candidates is None or len(candidates) < len(best_candidates):
                        best_cell = row, col
                        best_candidates = candidates
        return best_cell, best_candidates

    def solve(self, grid):



