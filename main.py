import random

import FileLoader as fl
from GenAlgorithm import GenAlgorithm
from GreedyAlgorithm import GreedyAlgorithm
import time
import numpy as np

from RandAlgorithm import RandAlgorithm

if __name__ == "__main__":
    cities, coord_type = fl.load_cities("Data/gr666.tsp")
    greedy_alg = GreedyAlgorithm(cities, coord_type)
    rand_alg = RandAlgorithm(cities, coord_type, 1000)
    # init best: pop_size 50, mut_prob 0.08, cross_prob: 0.7

    pop_sizes_factors = [1]
    mut_probs_factors = [0.08]
    cross_probs = [0.7]
    fitnesses = 0.
    for pop_size in pop_sizes_factors:
        for mut_prob in mut_probs_factors:
            for cross_prob in cross_probs:
                #for i in range(5):
                genetic_alg = GenAlgorithm(cities, coord_type, pop_size, mut_prob, cross_prob, 5, 1)
                genetic_alg.run(60)
                print("pop_size:", pop_size, "mut prob:",mut_prob, "cross_prob:", cross_prob)
                print("Fitness:", genetic_alg.Best_solution.Fitness)
                #fitnesses+=genetic_alg.Best_solution.Fitness
    print("avg:", fitnesses / 5.)


    # start = time.time()
    # #print(genetic_alg.Best_solution.Fitness)
    # #print(genetic_alg.Best_solution.Fitness)
    # end = time.time()
    # print("time:", end - start)
    #
    #
    #
    # print("\n\n-----------greedy:--------------------")
    # greedy_alg.run()
    # print(greedy_alg.Best_solution.Fitness)
    # #print(random.uniform(0,1))
    #
    #
    # print("\n\n-----------random:--------------------")
    # start = time.time()
    # rand_alg.run()
    # print(rand_alg.Best_solution.Fitness)
    # end = time.time()