import string

class Organism(object):
    def __init__(self, parent_a, parent_b):
        self.genes = self.__generate_genes(parent_a, parent_b)
        self.available_gene_pool = string.ascii_letters

    def __str__(self):
        return self.genes

    def __generate_genes(self, parent_a, parent_b):
        child_genes = ""
        for i in range(len(parent_a.genes)):
            random_number = random.random()
            if random_number < self.mutation_rate:
                child_genes += random.choice(self.available_gene_pool)
            elif random_number < 0.5:
                child_genes += parent_a.genes[i]
            else:
                child_genes += parent_b.genes[i]
        self.genes = child_genes
        return child_genes
