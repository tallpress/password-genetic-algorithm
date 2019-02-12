from password_cracker import PasswordCracker

a = PasswordCracker('cd', 100)
population = a.generate_populus(2)
computed_population = a.compute_population(population)
selection = a.select_from_population(computed_population, 8,2)
next_generation = a.create_next_generation(selection)
print(computed_population)
