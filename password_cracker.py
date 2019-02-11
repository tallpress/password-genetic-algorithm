import random
import string

class PasswordCracker(object):
    def test_word(self, password, word_to_test):
        score = 0
        if (len(word_to_test) != len(password)):
            return score
        else:
            i = 0
            while (i < len(password)):
                if (password[i] == word_to_test[i]):
                    score+=1
                i+=1
            return score * 100 / len(password)

    def generate_populus(self, number_of_individuals, word_length):
        population = []
        for i in range(number_of_individuals):
            population.append(self.generateWord(word_length))
        return population

    def generateWord(self, word_length):
        choice_of_characters = string.ascii_letters + string.digits
        return ''.join(random.choice(choice_of_characters)
            for _ in range(word_length))


