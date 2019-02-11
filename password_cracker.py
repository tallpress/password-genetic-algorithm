import random
import string
from operator import itemgetter

class PasswordCracker(object):
    def __init__(self, password):
        self.password = password

    def test_word(self, word_to_test):
        score = 0
        if (len(word_to_test) != len(self.password)):
            return score
        else:
            i = 0
            while (i < len(self.password)):
                score = 0
                if (self.password[i] == word_to_test[i]):
                    score+=1
                i+=1
            return score * 100 / len(self.password)

    def generate_populus(self, number_of_individuals, word_length):
        population = []
        for i in range(number_of_individuals):
            population.append(self.generateWord(word_length))
        return population

    def generateWord(self, word_length):
        # choice_of_characters = string.ascii_letters + string.digits
        choice_of_characters = string.ascii_letters
        return ''.join(random.choice(choice_of_characters)
            for _ in range(word_length))

    def computePopulation(self, population):
        calculated_population = {}
        for word in population:
            score = self.test_word(word)
            calculated_population[word] = score
        return sorted(calculated_population.items(), key = itemgetter(1), reverse=True)

