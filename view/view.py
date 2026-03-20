import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QObject

loader = QUiLoader()

class View(QObject):
    def __init__(self):
        super().__init__()
        self.ui = loader.load("game.ui", None)

        # Create list of all cell buttons
        self.cells = []
        for i in range(0, 9):
            for j in range(0, 9):
                # This doesn't work
                self.cells.append(f"self.ui.s{i}{j}")
        print(self.cells)

        # Connect all buttons
        for cell in self.cells:
            cell.clicked.connect( lambda checked, cell=cell : self.pressed(cell))
        
        # This variable stores which button the user has selected
        self.selected_cell = None

    def pressed(self, cell):
        pass

    def cell_selected(self, cell):
        """ Change which cell is selected """
        # self.selected_cell = cell
        pass

    def change_number(self, cell):
        """ Change the number in the selected cell to the one picked by the user """
        pass

# This stuff might get removed later
program = QApplication.instance()
if program == None:
    program = QApplication(sys.argv)
sudoku = View()
sudoku.ui.show()
program.exec()
