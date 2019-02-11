from password_cracker import PasswordCracker

a = PasswordCracker('ab')
population = a.generate_populus(5000, 2)
print(a.computePopulation(population))
