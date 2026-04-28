class SudokuController:
    """ Connects the model and view """
    
    def __init__(self, model, view, seeds):
        self.model = model
        self.view = view
        self.seeds = seeds
        self.setup_game()

    def get_seed(self):
        """ This method gets the start game setup from the model """
        seed = self.model.prepare_seed(self.seeds.EASY_SEED)
        seed = self.model.convert_to_numbers(seed)
        return self.model.convert_to_matrix(seed)

    def setup_game(self):
        """ Function for setting up the game """
        layout = self.get_seed()
        # Now we call the the method in the view to put the numbers into the grid
        row_num = 0
        col_num = 0
        for row in layout:
            for num in row:
                if num != 0:
                    self.view.change_num(row_num, col_num, num)
                    self.view.disable_num(row_num, col_num)
                col_num += 1
            col_num = 0
            row_num += 1

