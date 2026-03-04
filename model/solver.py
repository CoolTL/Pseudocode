from sudoku import Sudoku
class solver():
    def __init__(self, sudokugrid):
        self.sudoku = self.sudokugrid

    def check(grid):
        # Setting up variables
        cor_rows = []
        cor_col = []
        cor_box = []
        n = 3
        m = 3
        # Checking each row
        for i in grid:
            # Creating a list to keep track of numbers in rows
            row_num = []
            # Checking each value in a row
            for j in i:
                # Checks if the number has already appeared or not, if not adds it to numbers seen
                if j not in row_num:
                    row_num.append(j)
            # Checks if there are nine numbers, if yes then it adds it to correct rows
            if len(row_num) == 9:
                cor_rows.append(row_num)
        # Checking each colloumn
        for k in range(9):
            # Creating a list to keep track of numbers in colloumns
            col_num = []
            # Checking each value in a colloumn
            for r in range(9):
                # Checks if the number has alreadey appeared or not, if not then it adds it to numbers seen
                if grid[r][k] not in col_num:
                    col_num.append(grid[r][k])
            # Checks if there are nine numbers, if yes then adds it to correct colloumns
            if len(col_num) == 9:
                cor_col.append(col_num)
        # Checking each box
        for o in range(9):
            # Creating a list to keep track of numbers in a box
            box_num = []
            # Checking each value in a box
            for l in range((n-3), n):
                for p in range((m-3), m):
                    # Checking if the number has already appeared or not, if not then it adds it to numbers seen
                    if grid[p][l] not in box_num:
                        box_num.append(grid[p][l])
                # Checks if there are nine numbers, if yes adds it to correct colloumns
                if len(box_num) == 9:
                    cor_box.append(box_num)
                    # Checks
                    if m == 9:
                        m = 3
                        n += 3
                    else:
                        m += 3
                    
