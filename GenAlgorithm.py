import time

import numpy as np

from Algorithm import Algorithm
from Individual import Individual


class GenAlgorithm(Algorithm):

    def __init__(self, cities, coord_type, pop_size, mut_prob, cross_prob, num_of_tournament_contestants):
        super(GenAlgorithm, self).__init__(cities, coord_type)
        self.Pop_size = pop_size
        self.population = []
        self.Best_solution = None
        self.Best_Fitness = np.inf
        self.Mut_prob = mut_prob
        self.Cross_prob = cross_prob
        self.Num_of_tournament_contestants = num_of_tournament_contestants

#czas jak chcemy porownac rozne algorytmy, liczba iteracji jak chcemy analizować (wykresy itp)
    #w wykresach jakie robimy ma byc widoczna eksploracja i eksploatacj
    def run(self, exec_time):
        self.init_population()
        self.evaluate_population()
        passed_time = 0
        next_gen = []
        while(passed_time < exec_time):
            while(len(next_gen) < self.Pop_size):
                father = self.perform_selection()
                mother = self.perform_selection()
            self.perform_crossover()
            self.mutate_population()
            passed_time += time.time()
        #print(self.evaluate_solution(individual))

    def init_population(self):
        for i in (0, self.Pop_size):

            self.population.append(self.generate_random_individual())

    def mutate_population(self):
        for individual in self.population:
            individual.mutate(self.Mut_prob)

    def evaluate_population(self):
        for individual in self.population:
            self.evaluate_solution(individual)
            if individual.Fitness < self.Best_Fitness:
                self.Best_solution = individual
                self.Best_Fitness = individual.Fitness

    def perform_selection(self):
        contestants = np.random.randint(0, self.Num_of_cities, self.Num_of_tournament_contestants)
        best_fitness = np.inf
        best_contestant = None
        for contestant in contestants:
            if self.population[contestant].Fitness > best_fitness:
                best_contestant = self.population[contestant]
                best_fitness = best_contestant.Fitness
        return best_contestant

    def perform_crossover(self):
        pass

