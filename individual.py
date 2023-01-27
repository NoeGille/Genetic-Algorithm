import numpy as np
from config import Config

class Individual():

    # CONSTRUCTOR

    def __init__(self, chromosome : np.ndarray = None):
        self.config = Config()
        self.chromosome = chromosome
        self.grade = self.get_grade()
    
    # REQUESTS

    def get_chromosome(self):
        return self.chromosome

    def get_grade(self):
        grade = 0
        for i in range(self.config.chromosome_length):
            gene = self.chromosome[i]
            target_gene = self.config.target[i]
            grade += self.__euclidean_distance(gene, target_gene)
        self.grade = grade
        return grade
            
    def __euclidean_distance(self, point1, point2):
        return np.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    # COMMANDS

    def set_chromosome(self, chromosome):
        self.chromosome = chromosome

    def crossover(self, partner: 'Individual'):
        child_chromosome = []
        for i in range(len(self.chromosome)):
            if np.random.random() < self.config.crossover_rate:
                child_chromosome.append(self.chromosome[i])
            else:
                child_chromosome.append(partner.chromosome[i])
        return Individual(np.array(child_chromosome))

    def mutate(self):
        for i in range(len(self.chromosome)):
            if np.random.random() < self.config.mutation_rate:
                self.chromosome[i] = np.random.randint(0, self.config.population_size)
    
