import numpy as np

from Algorithm import Algorithm
from Individual import Individual


class RandAlgorithm(Algorithm):

    def __init__(self, cities, coord_type, num_of_iterations):
        super(RandAlgorithm, self).__init__(cities, coord_type)
        self.Num_of_iterations = num_of_iterations
        self.Best_solution = self.generate_random_individual()
        self.evaluate_solution(self.Best_solution)

    def run(self):
        for i in range (0, self.Num_of_iterations):
            individual = self.generate_random_individual()
            self.evaluate_solution(individual)
            if individual.Fitness < self.Best_solution.Fitness:
                self.Best_solution = individual

