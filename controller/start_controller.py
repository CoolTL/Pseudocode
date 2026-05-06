import json
import random
from pathlib import Path


class SeedController:
    def __init__(self):
        self.seed_file = Path(__file__).resolve().parent.parent / "seeds.json"
        self.seeds = self.load_seeds()

    def load_seeds(self):
        with open(self.seed_file, "r", encoding="utf-8") as file:
            return json.load(file)

    def get_random_seed(self, difficulty):
        """
        Returnerer et tilfældig seed + dens løsning
        fx: ("EASY1", seed, solved_seed)
        """

        difficulty_data = self.seeds[difficulty]

        # Filtrer kun "rigtige" seeds (ikke *_SOLVED)
        seed_names = [
            key for key in difficulty_data.keys()
            if not key.endswith("_SOLVED")
        ]

        # Vælg en tilfældig
        chosen_name = random.choice(seed_names)

        seed = difficulty_data[chosen_name]
        solved = difficulty_data[f"{chosen_name}_SOLVED"]

        return chosen_name, seed, solved 
        
        
