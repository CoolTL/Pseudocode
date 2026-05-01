class Solver:

    def __init__(self):
        # Sets the rigid variables
        self.correct_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.empty = 0

    # Gets the colomn
    def col_check(self, grid, col):
        return {grid[row][col] for row in range(9)}

    # Gets the numbers in the box
    def box_check(self, row, col, grid):
        box_nums = set()

        start_row = (row // 3) * 3
        start_col = (col // 3) * 3

        for r in range(start_row, start_row + 3):
            for c in range(start_col, start_col + 3):
                box_nums.add(grid[r][c])

        return box_nums
    # Gets all numbers from a row, colomn and box, and then removes it from the correct numbers to find the remaing candidates
    def get_candidates(self, grid, row, col):
        row_nums = set(grid[row])
        col_nums = self.col_check(grid, col)
        box_nums = self.box_check(row, col, grid)

        return self.correct_numbers - row_nums - col_nums - box_nums

    # Finds the empty squares
    def find_empty(self, grid):
        for row in range(9):
            for col in range(9):
                if grid[row][col] == self.empty:
                    return row, col
        return None

    def solve(self, grid):
        # Finding the empty squares in the grid
        empty = self.find_empty(grid)
        # If there are none, then it is solved
        if empty is None:
            return True
        # Getting the rows and colomn position of the empty squares
        row, col = empty
        # Getting the getting the candiate of the square, and then inserting the value
        for value in self.get_candidates(grid, row, col):
            grid[row][col] = value
            # Function calls itself and if its true, then returns true until its done
            if self.solve(grid):
                return True
            # Resets the number to zero, if there wasnt found a solution
            grid[row][col] = self.empty

        return False

    def get_grid(self, sudoku):
        self.sudoku = sudoku
