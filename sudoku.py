import numpy as np

class Sudoku:
    def __init__(self):
        self.grid = [["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""],
                     ["","","","","","","","",""]]
    def rem_num(self, x, y):
        self.grid[x][y] = ""

    def change_num(self, x, y, *n):
        n = int(n[0])
        if n:
            
            if n == self.grid[x][y]:
                self.rem_num(x, y)
            else:
                self.grid[x][y] = n
        else:
            self.rem_num(x,y)

test = Sudoku()

test.change_num(2,3,5)
print(test.grid)
print(type(test.grid[2][3]))
