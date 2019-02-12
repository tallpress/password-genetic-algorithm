import random
import string
from operator import itemgetter

class PasswordCracker(object):
    def __init__(self, password, population_size, mutation_rate):
        self.password = password
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.available_genes = string.ascii_letters
        # self.available_genes = string.ascii_letters + string.digits

    def test_word(self, word_to_test):
        score = 0
        if (len(word_to_test) != len(self.password)):
            return score
        else:
            i = 0
            score = 0
            while (i < len(self.password)):
                if (self.password[i] == word_to_test[i]):
                    score+=1
                i+=1
            return score * 100 / len(self.password)

    def generate_populus(self, word_length):
        population = []
        for i in range(self.population_size):
            population.append(self.generate_word(word_length))
        return population

    def generate_word(self, word_length):
        return ''.join(random.choice(self.available_genes)
            for _ in range(word_length))

    def compute_population(self, population):
        calculated_population = {}
        for word in population:
            score = self.test_word(word)
            calculated_population[word] = score
        return sorted(calculated_population.items(), key = itemgetter(1), reverse=True)

    def select_from_population(self, population, good_sample_size, random_sample_size):
        good_samples = population[:good_sample_size]
        remaining_population = population[good_sample_size:]
        random.shuffle(remaining_population)
        random_samples = remaining_population[:random_sample_size]
        concat_list = good_samples + random_samples
        return concat_list

    def create_next_generation(self, population):
        population = [x[0] for x in population]
        next_generation = []
        for i in range(self.population_size):
            index_1 = random.randint(0, len(population) - 1)
            index_2 = random.randint(0, len(population) - 1)
            child = self.breed(population[index_1], population[index_2])
            next_generation.append(child)
        return next_generation

    def breed(self, parent_a, parent_b):
        child = ""
        for i in range(len(parent_a)):
            random_number = random.random()
            if random_number < self.mutation_rate:
                child += random.choice(self.available_genes)
            elif random_number < 0.5:
                child += parent_a[i]
            else:
                child += parent_b[i]
        return child
