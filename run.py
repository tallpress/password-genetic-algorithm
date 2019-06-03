from password_cracker import PasswordCracker
password = 'tomallpres'
a = PasswordCracker(password, 1000, 0.001)
population = a.generate_populus(len(password))
i = 0
while (i < 10000):
    computed_population = a.compute_population(population)
    selection = a.select_from_population(computed_population, 10,1)
    population = a.create_next_generation(selection)
    i+=1
print(population)
count = 0
for word in population:
    if word == password:
        count+=1

print(count *100 / 500)

a = PasswordCracker(target, population, mutation_rate)

    population = a.generate_populus(len(target))
    i = 0
    while (i < epochs):
        computed_population = a.compute_population(population)
        selection = a.select_from_population(computed_population, 10,1)
        population = a.create_next_generation(selection)
        i+=1

    count = 0
    for word in population:
        if word == target:
            count+=1

    correct_percentage = count *100 / 500
