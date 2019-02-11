from password_cracker import PasswordCracker

cracker = PasswordCracker('ab', 100)
population = cracker.generate_populus(2)
computed_population = cracker.compute_population(population)
selection = cracker.select_from_population(computed_population, 8,2)
next_generation = cracker.create_next_generation(selection)
print(next_generation)
