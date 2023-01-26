import numpy as np
import matplotlib.pyplot as plt
from genetic import GeneticAlgorithm
from config import Config
class Main (object):
    def __init__(self, **kwargs):
        self.config = Config()
        self.genetic = GeneticAlgorithm()

    def run(self):
        print(self.genetic.get_result())
        plt.figure()
        plt.plot(self.genetic.get_result().get_chromosome()[:, 0], self.genetic.get_result().get_chromosome()[:, 1], 'ro')
        plt.plot(self.config.target[:, 0], self.config.target[:, 1], 'bo')
        plt.show()
    
if __name__ == "__main__":
    main = Main()
    main.run()