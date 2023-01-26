from config import Config
from individual import Individual
from population import Population


class GeneticAlgorithm():
    def __init__(self) -> None:
        self.config = Config()
        self.population = Population()
        self.result = self.population.get_best_individual()
        

    def evolve(self, population: Population, generations : int) -> Population:
        for _ in range(generations):
            self.population = self.evolve_population(self.population)
        self.result = self.population.get_best_individual()
    
    def get_result(self):
        return self.result