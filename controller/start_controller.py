import json
import os
import random as rng

class DifficultyController:
    def __init__(self):

    def get_seed_file(self, difficulty):
        with open(seeds.json, 'r') as file:
            return json.load(file)
    def get_seed(self, difficulty):
        return self.get_seed_file(resource_path("seeds.json"))[difficulty] 
        
        
