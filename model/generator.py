from abc import ABC, abstractmethod
from seeds import *
from random import randrange
import numpy as np

class Generator(ABC):
    """ Abstract base class for sudoku generators. """

    def __init__(self):
        seed = EASY_SEED_SOLVED
        self.convert_to_matrix(self.convert_to_numbers(self.prepare_seed(HARD_SEED_SOLVED)))
        
    def prepare_seed(self, seed):
        """ Turns the seed into the letters a-i so it the numbers can be scrambled """
        letters = "abcdefghi"
        for i in range(0, len(letters)):
            seed = seed.replace(str(i+1), letters[i])
        return seed
    
    def generate_lookup_table(self):
        """ Randomly picks which number is correspondent to which letter """
        nums = np.linspace(start=1, stop=9, num=9, dtype=int)
        lookup = []
        for i in nums:
            choice = randrange(0, len(nums))
            lookup.append(int(nums[choice]))
            nums = np.delete(nums, choice)
        return lookup

    def convert_to_numbers(self, seed):
        """ Converts the list of letters into numbers """
        lookup = self.generate_lookup_table()
        letters = "abcdefghi"
        for i in range(0, len(letters)):
            seed = seed.replace(letters[i], str(lookup[i]))            
        return seed

    def rotate_matrix(self, matrix):
        """ Rotate the matrix randomly between its 4 sides """
        return np.rot90(matrix, randrange(0, 4), axes=(0,1))

    def flip_matrix(self, matrix):
        """ Flip the matrix either horizontally, vertically or not at all """
        if randrange(0, 2) == 1:
            matrix = np.flipud(matrix)
        if randrange(0, 2) == 1:
            matrix = np.fliplr(matrix)
        return matrix

    def convert_to_matrix(self, seed):
        """ This function converts the list of numbers back into the backend format we use """
        sudoku = np.empty((9, 9), dtype=int)
        counter = 0
        for i in range(0, 9):
            for j in range(0, 9):
                sudoku[i][j] = seed[counter]
                counter += 1
        # Flip or rotate the sudokus for more randomness
        sudoku = self.flip_matrix(sudoku)
        sudoku = self.rotate_matrix(sudoku)
        print(sudoku)

# https://gamedev.stackexchange.com/questions/56149/how-can-i-generate-sudoku-puzzles
test = Generator()
