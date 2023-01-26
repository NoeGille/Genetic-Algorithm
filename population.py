import numpy as np
from individual import Individual
from config import Config

class Population():
    def __init__(self):
        self.config = Config()

        self.population = [Individual() for _ in range(self.config.population_size)]
        self.grades = np.array([self.config.population_size for _ in range(self.config.population_size)])
        self.mating_pool = []
        self.generation = 0
    
    # REQUESTS

    def get_population(self):
        return self.population

    def get_fitness(self):
        return self.fitness

    def get_mating_pool(self):
        return self.mating_pool

    def get_generation(self):
        return self.generation
    
    def get_best_individual(self):
        self.select_population()
        return self.population[0]

    # COMMANDS

    def set_population(self, population):
        self.population = population
    
    def set_fitness(self, fitness):
        self.fitness = fitness
    
    def set_mating_pool(self, mating_pool):
        self.mating_pool = mating_pool
    
    def set_generation(self, generation):
        self.generation = generation

    def evolve_population(self):
        self.grades = np.array([individual.get_grade() for individual in self.population])
        self.select_population()
        self.mate_population()
        self.mutate_population()
        self.generation += 1

    def select_population(self):
        self.mating_pool = self.population[:self.config.population_size]

    def mate_population(self):
        offspring = []
        for _ in range(self.config.population_size):
            parent1 = np.random.choice(self.mating_pool)
            parent2 = np.random.choice(self.mating_pool)
            offspring.append(parent1.crossover(parent2))
        self.population = offspring
    
    def mutate_population(self):
        for individual in self.population:
            individual.mutate()
