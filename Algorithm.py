import numpy as np
import random

from Individual import Individual
from haversine import haversine


class Algorithm:

    def __init__(self, cities, coord_type):
        #array of cities coords
        self.Cities = cities
        self.Num_of_cities = len(cities)
        self.Cities_in_order = np.arange(self.Num_of_cities, dtype=np.float32)
        if coord_type.__contains__("GEO"):
            self.dist_method = self.__calc_distance_geo
        else:
            self.dist_method = self.__calc_distance_norm

        # matrix of distances, f.e. at Distances[0][2] is the distance between first and third city
        self.Distances = np.zeros((self.Num_of_cities, self.Num_of_cities), dtype=np.float32)

    def generate_random_individual(self):
        #     rng = np.random.default_rng()
        #     return rng.choice(genotypeLength, size=genotypeLength, replace=False)
        return Individual(np.random.choice(self.Cities_in_order, self.Num_of_cities, replace=False))

    def generate_greedy_individual(self):
        start_point = random.randint(0, self.Num_of_cities-1)
        return self.run_for_start_point(start_point)

    def run_for_start_point(self, start_point):
        solution = []
        curr_city = start_point
        cities_left_to_visit = set(range(self.Num_of_cities))
        dist_sum = 0
        closest_city = 0
        append = solution.append
        dist_method = self.dist_method
        for i in range(0, self.Num_of_cities -1):
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
        append(curr_city)
        best_solution = Individual(solution)
        best_solution.Fitness = dist_sum
        #print(best_solution.Genotype, best_solution.Fitness)
        return best_solution

    def generate_random_city(self):
        return np.random.randint(0, self.Num_of_cities-1)

    def __calc_distance_norm(self, ind_from, ind_to):
        dist = self.Distances[ind_from, ind_to]
        if dist == 0:
            dist = np.linalg.norm(self.Cities[ind_from] - self.Cities[ind_to])
            self.Distances[ind_from][ind_to] = dist
            self.Distances[ind_from][ind_to] = dist
        return dist

    def __calc_distance_geo(self, ind_from, ind_to):
        dist = self.Distances[ind_from, ind_to]
        if dist == 0:
            dist = haversine(self.Cities[ind_from], self.Cities[ind_to])
            self.Distances[ind_from][ind_to] = dist
            self.Distances[ind_from][ind_to] = dist
        return dist

    def evaluate_solution(self, individual):
        if individual.Fitness == -1:
            if len(np.unique(individual.Genotype)) != len(individual.Genotype):
                individual.Fitness = 0
            else:
                dist_sum = 0
                for i in range(self.Num_of_cities - 1):
                    dist = self.Distances[int(individual.Genotype[i])][int(individual.Genotype[i+1])]
                    if dist == 0:
                        dist = self.dist_method(int(individual.Genotype[i]), int(individual.Genotype[i + 1]))
                        self.Distances[int(individual.Genotype[i])][int(individual.Genotype[i+1])] = dist
                    dist_sum += dist
                individual.Fitness = dist_sum + \
                    self.dist_method(int(individual.Genotype[self.Num_of_cities-1]), int(individual.Genotype[0]))
        return individual.Fitness
