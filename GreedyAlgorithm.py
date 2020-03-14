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
            individual = self.__run_for_start_point(curr_city)
            if individual.Fitness < best_fitness:
                best_fitness = individual.Fitness
                best_individual = individual
        self.Best_solution = best_individual

    def __run_for_start_point(self, start_point):
        solution = []
        curr_city = start_point
        cities_left_to_visit = set(range(self.Num_of_cities))
        dist_sum = 0
        closest_city = 0
        append = solution.append
        dist_method = self.dist_method
        for i in range(0, self.Num_of_cities - 1):
            append(curr_city)
            cities_left_to_visit.remove(curr_city)
            shortest_dist = np.inf
            # przeanalizuj dystans do kazdego miasta i wybierz najblizsze
            for considered_city in cities_left_to_visit:
                dist = dist_method(curr_city, considered_city)

                if dist < shortest_dist:
                    shortest_dist = dist
                    closest_city = considered_city
            curr_city = closest_city
            dist_sum += shortest_dist
        dist_sum += dist_method(curr_city, start_point)

        best_solution = Individual(solution)
        best_solution.Fitness = dist_sum
        #print(best_solution.Genotype, best_solution.Fitness)
        return best_solution





