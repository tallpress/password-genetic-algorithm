import string
from individual import Individual

class Generation(object):
    def __init__(self, population):
        self.population = population

    def display(self):
        for individual in self.population:
            print(individual.display())

    def score(self, target):
        for individual in self.population:
            individual.test_fitness(target)
        self.population.sort(key=lambda i: i.fitness, reverse=True)
        return self
