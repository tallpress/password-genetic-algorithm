from password_cracker import PasswordCracker

cracker = PasswordCracker('ab')
population = cracker.generate_populus(100, 2)
computed_population = cracker.computePopulation(population)
print(cracker.selectFromPopulation(computed_population, 5, 1))
