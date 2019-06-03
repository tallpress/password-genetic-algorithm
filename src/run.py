from spawner import Spawner
from genetic_algo import GeneticAlgo

population_size = 1000

a = Spawner()
generation = a.spawn_generation('tomallpress', population_size)

c = GeneticAlgo(population_size, 0.01, 'tomallpress', 100, 1)
for i in range(20):
    generation = c.get_next_generation(generation)

print(generation.display())
