import random
import numpy as np

class Individual:

    def __init__(self, genotype):
        self.Genotype = genotype
        self.Fitness = -1
        self.Genotype_length = len(genotype)

    def mutate(self, mut_prob, swap=False, inverse=False):
        if swap:
            self.__swap_mutate(mut_prob)
        if inverse:
            self.__inverse_mutate_circular(mut_prob)

    def __swap_mutate(self, mut_prob):
        mutations = np.array(np.random.rand(self.Genotype_length) < mut_prob)
        mutations_indices = np.argwhere(mutations == True).reshape(-1)
        for gene_ind in mutations_indices:
                sec_gene = random.randint(0, self.Genotype_length-1)
                self.Genotype[gene_ind], self.Genotype[sec_gene] = self.Genotype[sec_gene], self.Genotype[gene_ind]

    def __inverse_mutate_flat(self, mut_prob):
        mutations = np.array(np.random.rand(self.Genotype_length) < mut_prob)
        mutations_indices = np.argwhere(mutations == True).reshape(-1)
        for gene_ind in mutations_indices:
            sec_gene = random.randint(0, self.Genotype_length - 1)
            if gene_ind > sec_gene:
                tmp = sec_gene
                sec_gene = gene_ind
                gene_ind = sec_gene
            reversed_part = self.Genotype[gene_ind:sec_gene+1]
            self.Genotype[gene_ind:sec_gene+1] = np.flip(reversed_part)

    #mutacja poprzez inwersję, ale pozwalająca na to, by odwracany segment zawierał kolejno końcowe i początkowe odcinki
    def __inverse_mutate_circular(self, mut_prob):
        mutations = np.array(np.random.rand(self.Genotype_length) < mut_prob)
        mutations_indices = np.argwhere(mutations == True).reshape(-1)
        for gene_ind in mutations_indices:
            sec_gene = random.randint(0, self.Genotype_length - 1)
            if gene_ind > sec_gene:
                first_rev_part = self.Genotype[gene_ind:]
                sec_rev_part = self.Genotype[:sec_gene+1]
                reversed_part = np.flip(np.concatenate((first_rev_part, sec_rev_part)))
                self.Genotype[gene_ind:] = reversed_part[:len(first_rev_part)]
                self.Genotype[:sec_gene+1] = reversed_part[len(first_rev_part):]
            else:
                reversed_part = self.Genotype[gene_ind:sec_gene+1]
                self.Genotype[gene_ind:sec_gene+1] = np.flip(reversed_part)

