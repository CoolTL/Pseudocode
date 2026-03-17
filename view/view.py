import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject

loader = QUiLoader()

class View(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("game.ui", None)

        # This variable stores which button the user has selected
        self.selected_cell = None

    def setup_game(self):
        """ Function for setting up the game """
        pass

    def cell_selected(self, cell):
        """ Change which cell is selected """
        # self.selected_cell = cell
        pass

    def change_number(self):
        """ Change the number in the selected cell to the one picked by the user """
        pass

# This stuff might get removed later
program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
sudoku = View()
sudoku.ui.show()
program.exec()
