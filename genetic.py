from config import Config
from individual import Individual
from population import Population


class GeneticAlgorithm():
    def __init__(self) -> None:
        self.config = Config()
        self.population = Population()
        self.result = self.population.get_best_individual()
        

    def evolve(self, generations : int) -> Population:
        for _ in range(generations):
            self.population.evolve_population()
            print(self.population.get_best_individual().get_grade())
        self.result = self.population.get_best_individual()
    
    def get_result(self):
        return self.result