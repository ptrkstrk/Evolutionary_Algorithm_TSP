import random
import numpy as np

class Individual:

    def __init__(self, genotype):
        self.Genotype = genotype
        self.Fitness = -1

    def mutate(self, mut_prob, swap=False, inverse=False):
        if swap:
            self.__swap_mutate(mut_prob)
        else:
            self.__inverse_mutate(mut_prob)

    def __swap_mutate(self, mut_prob):
        for gene_ind in (0, len(self.Genotype)):
            if random.uniform(0, 1) < mut_prob:
                sec_gene = random.randint(0, len(self.Genotype))
                self.Genotype[gene_ind], self.Genotype[sec_gene] = self.Genotype[sec_gene], self.Genotype[gene_ind]

    def __inverse_mutate(self, mut_prob):
        pass

