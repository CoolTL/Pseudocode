from abc import ABC, abstractmethod
from seeds import *
from random import randrange
import numpy as np

class Generator(ABC):
    """ Abstract base class for sudoku generators. """

    def __init__(self):
        seed = EASY_SEED_SOLVED
        self.convert_to_numbers(seed)
        
    # @abstractmethod
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
        sudoku = seed
        for i in range(0, len(letters)):
            sudoku = sudoku.replace(letters[i], str(lookup[i]))            
        return sudoku

    def turn_into_sudoku(self):
        """ This function converts the list of numbers back into the backend format we use """
        pass

# https://gamedev.stackexchange.com/questions/56149/how-can-i-generate-sudoku-puzzles
# Numpy methods I can use
# .rot90 to rotate the sudoku seed
# .flip/flipud/fliplr to flip the sudoku seed
test = Generator()
print(test.generate_lookup_table())
