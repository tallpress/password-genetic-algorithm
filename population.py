from organism import Organism
class Population(object):
    def __init__(self, size, organism_complexity, gene_pool, winning_genes):
        self.size = size
        self.organism_complexity = organism_complexity
        self.gene_pool = gene_pool
        self.populus = self.generate_initial_populus()
        self.winning_genes = winning_genes
        pass

    def generate_initial_populus(self):
        population = []
        for i in range(self.size):
            population.append(self.__spawn_organism(word_length))
        return population

    def __spawn_organism(self):
        return ''.join(random.choice(self.gene_pool)
            for _ in range(self.organism_complexity))

    def fitness_test(self):
        calculated_population = {}
        for organism in population:
            fitness = self.__test_fitness(organism)
            calculated_population[organism] = fitness
        return sorted(calculated_population.items(), key = itemgetter(1), reverse=True)

    def __test_fitness(self, organism):
        fitness = 0
        if (len(word_to_test) != len(self.winning_genes)):
            return fitness
        else:
            i = 0
            fitness = 0
            while (i < len(self.winning_genes)):
                if (self.winning_genes[i] == word_to_test[i]):
                    fitness+=1
                i+=1
            return fitness * 100 / len(self.winning_genes)
