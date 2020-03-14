import time

import numpy as np

from Algorithm import Algorithm
from Individual import Individual
import math
import random


class GenAlgorithm(Algorithm):

    def __init__(self, cities, coord_type, pop_size_factor,
                 mut_prob_factor, cross_prob, num_of_tournament_contestants,
                 num_of_elites=0):
        super(GenAlgorithm, self).__init__(cities, coord_type)
        #rozmiar populacji zaokrąglony do najbliżej liczby parzystej, a jeśli liczba elit jest nieparzysta to do nieparzystej
        self.Pop_size = math.ceil(pop_size_factor * self.Num_of_cities / 2.) * 2 + num_of_elites % 2
        self.population = []
        self.Best_solution = None
        self.Num_of_elites = num_of_elites
        self.Worst_solutions = []
        self.Best_solutions = []
        self.Avg_fitnesses = []
        self.next_gen = []
        self.Best_Fitness = np.inf
        self.Mut_prob = mut_prob_factor * (1./self.Num_of_cities)
        self.Greedy_init_prob = min(self.Num_of_cities/self.Pop_size, 0.1)
        self.Cross_prob = cross_prob
        self.Num_of_tournament_contestants = num_of_tournament_contestants

#czas jak chcemy porownac rozne algorytmy, liczba iteracji jak chcemy analizować (wykresy itp)
    #w wykresach jakie robimy ma byc widoczna eksploracja i eksploatacja
    def run(self, exec_time):
        start_time = time.time()
        self.init_population()
        passed_time = time.time() - start_time
        while passed_time < exec_time:
            start_time = time.time()
            self.evaluate_population()
            self.next_gen = []
            elites_indices = self.select_elites()
            for i in elites_indices:
                self.next_gen.append(self.population[i])
            # self.next_gen.extend(self.population[elites_indices])
            while len(self.next_gen) < self.Pop_size:
                mother_ind = self.perform_selection()
                father_ind = mother_ind
                while father_ind == mother_ind:
                    father_ind = self.perform_selection()
                cross = random.uniform(0, 1) < self.Cross_prob
                if cross:
                    children = self.perform_crossover(father_ind, mother_ind)
                    self.next_gen.extend(children)
                else:
                    self.next_gen.append(self.population[mother_ind])
                    self.next_gen.append(self.population[father_ind])
            self.population = self.next_gen
            self.mutate_population()
            passed_time += (time.time() - start_time)
            #-------------TEST----------------------------
            #print("best:", self.Best_solution.Fitness)


    def init_population(self):
        greedy_inits = np.array(np.random.rand(self.Pop_size) < self.Greedy_init_prob)
        self.population = [self.generate_greedy_individual() if gr_init
                        else self.generate_random_individual()
                        for gr_init in greedy_inits]

    def mutate_population(self):
        [individual.mutate(self.Mut_prob, inverse=True) for individual in self.population]

    def evaluate_population(self):
        gen_worst = self.population[0]
        gen_best = self.population[0]
        for individual in self.population:
            self.evaluate_solution(individual)
            if individual.Fitness < self.Best_Fitness:
                self.Best_solution = individual
                self.Best_Fitness = individual.Fitness
            if individual.Fitness < gen_best.Fitness:
                gen_best = individual
            if individual.Fitness > gen_worst.Fitness:
                gen_worst = individual

        self.Worst_solutions.append(gen_worst)
        self.Best_solutions.append(gen_best)
        self.Avg_fitnesses.append(np.average([sol.Fitness for sol in self.population]))

    def perform_selection(self):
        contestants_indices = np.random.choice(self.Pop_size, self.Num_of_tournament_contestants, replace=False)
        best_contestant_ind = contestants_indices[0]
        for cont_ind in contestants_indices[1:]:
            if self.population[cont_ind].Fitness < self.population[best_contestant_ind].Fitness:
                best_contestant_ind = cont_ind
        return best_contestant_ind

    #Ordered crossover
    def perform_crossover(self, dad_ind, mom_ind):
        first_child = Individual(np.empty(self.Num_of_cities, dtype=np.float32))
        second_child = Individual(np.empty(self.Num_of_cities, dtype=np.float32))
        first_ind = random.randint(0, self.Num_of_cities-1)
        second_ind = first_ind
        # while second_ind == first_ind:
        second_ind = random.randint(0, self.Num_of_cities-1)
        if second_ind < first_ind:
            tmp = first_ind
            first_ind = second_ind
            second_ind = tmp

        passed_fragment = self.population[dad_ind].Genotype[first_ind:second_ind+1]
        ordered_other_genes = [gene for gene in self.population[mom_ind].Genotype if gene not in passed_fragment]
        first_child.Genotype[0:first_ind] = ordered_other_genes[0:first_ind]
        first_child.Genotype[first_ind:second_ind + 1] = passed_fragment
        first_child.Genotype[second_ind+1:] = ordered_other_genes[first_ind:]

        passed_fragment = self.population[mom_ind].Genotype[first_ind:second_ind + 1]
        ordered_other_genes = [gene for gene in self.population[dad_ind].Genotype if gene not in passed_fragment]
        second_child.Genotype[0:first_ind] = ordered_other_genes[0:first_ind]
        second_child.Genotype[first_ind:second_ind + 1] = passed_fragment
        second_child.Genotype[second_ind + 1:] = ordered_other_genes[first_ind:]

        return first_child, second_child









    def select_elites(self):
        fitnesses = np.array([ind.Fitness for ind in self.population])
        return fitnesses.argsort()[:self.Num_of_elites]



