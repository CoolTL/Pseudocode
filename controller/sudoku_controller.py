class SudokuController:
    """ Connects the model and view """
    
    def __init__(self, model, view, seeds):
        self.model = model
        self.view = view
        self.seeds = seeds

    def get_seed(self):
        """ This method gets the start game setup from the model """
        seed = self.model.prepare_seed(self.seeds.EASY_SEED_SOLVED)
        seed = self.model.convert_to_numbers(seed)
        return self.model.convert_to_matrix(seed)

    def setup_game(self):
        """ Function for setting up the game """
        pass

