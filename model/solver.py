from sudoku import Sudoku
import numpy as np
class solver():
    
    def __init__(self, sudokugrid):

        self.sudoku = self.sudokugrid

    def box_check(n, m, grid):
        box_num = {}
        # Checking each value in a box
        for l in range((n-3), n):
            for p in range((m-3), m):
            # Checking if the number has already appeared or not, if not then it adds it to numbers seen
                if grid[p][l] not in box_num:
                    box_num.append(grid[p][l])
        return box_num 
    
    def col_check(grid, k):
        # Creating a list to keep track of numbers in colloumns
        col_num = {}
        # Checking each value in a colloumn
        for r in range(9):
            # Checks if the number has alreadey appeared or not, if not then it adds it to numbers seen
            if grid[r][k] not in col_num:
                col_num.append(grid[r][k])
        return col_num

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
            col = col_check(grid, k)
            # Checks if there are nine numbers, if yes then adds it to correct colloumns
            if len(col_num) == 9:
                cor_col.append(col_num)
        # Checking each box
        for o in range(9):
            box = check_box(n, m, grid)
           # Checks if there are nine numbers, if yes adds it to correct colloumns
            if len(box) == 9:
                cor_box.append(box)
                # Box variables 
                if m == 9:
                    m = 3
                    n += 3
                else:
                    m += 3
        if len(cor_box) == 9 and len(cor_rows) == 9 and len(cor_col) == 9:
            return True

    def solve(self, sudoku):
        cor_nums = {1,2,3,4,5,6,7,8,9}
        counter = 0

        while True:
            for i in sudoku:
                for j in len(i):
                    if i[j] != "":
                        pass
                    else:
                        counter += 1
                        if soduku.index(i) => 7:
                            a = 9
                        elif sudoku.index(i) => 4:
                            a = 6
                        else:
                            a = 3
                        
                        if i[j] => 7:
                            b = 9
                        elif i[j] => 4:
                            b = 6
                        else:
                            b = 3

                        m = col_check(sudoku, j) 
                        l = box_check(a, b, sudoku)
                        n = cor_nums-i
                        n = n-m
                        n = n-l

                        if len(n) == 1:
                            k = n[0]
                            self.sudoku.change_num(j, k)
                            j = k
                            counter -= 1
                if counter == 0:
                    break

                    

