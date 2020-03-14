import numpy as np

from Individual import Individual
from haversine import haversine


class Algorithm:

    def __init__(self, cities, coord_type):
        #array of cities coords
        self.Cities = cities
        self.Num_of_cities = len(cities)
        if coord_type.__contains__("GEO"):
            self.dist_method = self.__calc_distance_geo
        else:
            self.dist_method = self.__calc_distance_norm

        # matrix of distances, f.e. at Distances[0][2] is the distance between first and third city
        self.Distances = np.zeros((self.Num_of_cities, self.Num_of_cities), float)

    def generate_random_individual(self):
        #     rng = np.random.default_rng()
        #     return rng.choice(genotypeLength, size=genotypeLength, replace=False)
        return Individual(np.random.choice(self.Num_of_cities, self.Num_of_cities, replace=False))

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
            dist_sum = 0
            for i in range(self.Num_of_cities - 1):
                dist = self.Distances[individual.Genotype[i]][individual.Genotype[i+1]]
                if dist == 0:
                    dist = self.dist_method(individual.Genotype[i], individual.Genotype[i + 1])
                    self.Distances[individual.Genotype[i]][individual.Genotype[i+1]] = dist
                dist_sum += dist
            individual.Fitness = dist_sum + self.dist_method(individual.Genotype[self.Num_of_cities-1], individual.Genotype[0])
            #print(dist_sum)
        return individual.Fitness
