from dataclasses import dataclass
import json
import numpy as np

@dataclass
class Config:
    def __init__(self):
        self.chromosome_length : int = 10
        self.population_size: int = 100
        self.mutation_rate: float = 0.01
        self.crossover_rate: float = 0.7
        self.max_generations: int = 10
        self.choose_best: float = 0.2
        

        with open('config.json') as f:
            self.config = json.load(f)
        self.__dict__.update(self.config)

        self.target = np.array([[i, i] for i in range(self.chromosome_length)])