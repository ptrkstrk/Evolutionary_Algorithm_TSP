import time

import numpy as np
import random
from Algorithm import Algorithm
from Individual import Individual
import itertools


class GreedyAlgorithm(Algorithm):

    def __init__(self, cities, coord_type):
        super(GreedyAlgorithm, self).__init__(cities, coord_type)
        self.Best_solution = None

    def run(self):
        closest_city = 0
        dist = 0
        best_individual = None
        best_fitness = np.inf
        #func = self.__run_for_start_point
        #solutions = map(self.__run_for_start_point, list(range(self.Num_of_cities)))
        #solutions = [func(curr_city) for curr_city in list(range(self.Num_of_cities))]
        #solutions = itertools.chain([], (func(iter) for iter in list(range(self.Num_of_cities))))
        #print(list(solutions).Fitness)
        #iterator = (print(self.__run_for_start_point(curr_city).Fitness) for curr_city in range(self.Num_of_cities))
        #itertools.chain(Solutions, self.__run_for_start_point(curr_city) for curr_city in self.Cities)
        for curr_city in range(self.Num_of_cities):
            individual = self.run_for_start_point(curr_city)
            if individual.Fitness < best_fitness:
                best_fitness = individual.Fitness
                best_individual = individual
        self.Best_solution = best_individual





