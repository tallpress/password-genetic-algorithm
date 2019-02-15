import string

class Organism(object):
    def __init__(self, parent_a, parent_b, gene_pool, mutation_rate=0.01):
        self.parent_a = parent_a
        self.parent_b = parent_b
        self.gene_pool = gene_pool
        self.mutation_rate = mutation_rate
        self.genes = self.generate_genes()
        pass

    def generate_genes(self):
        genes = ""
        for i in range(len(self.parent_a)):
            random_number = random.random()
            if random_number < self.mutation_rate:
                genes += random.choice(self.gene_pool)
            elif random_number < 0.5:
                genes += self.parent_a[i]
            else:
                genes += self.parent_b[i]
        return genes


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
