import random

import FileLoader as fl
from GenAlgorithm import GenAlgorithm
from GreedyAlgorithm import GreedyAlgorithm
import time

from RandAlgorithm import RandAlgorithm

if __name__ == "__main__":
    cities, type = fl.load_cities("Data/berlin52.tsp")
    greedy_alg = GreedyAlgorithm(cities, type)
    rand_alg = RandAlgorithm(cities, type, 1000)
    start = time.time()
    greedy_alg.run()
    print(greedy_alg.Best_solution.Fitness)
    #print(greedy_alg.Best_solution.Genotype)
    end = time.time()
    print(end - start)
    #print(random.uniform(0,1))


    print("\n\n-----------random:--------------------")
    start = time.time()
    rand_alg.run()
    print(rand_alg.Best_solution.Fitness)
    end = time.time()