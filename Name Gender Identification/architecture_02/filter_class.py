#!/usr/bin/python

class Filterset:
    def __init__(self, label, random, size):
        self.random = random
        self.label = label
        self.size = size
        self.charset = self.charsetInitializer(self.size)
        self.charset_aux = []
        self.generation_counter = 0
        self.fitness = 0.0

    # Returns a single patterns within charset.
    def getSinglePattern(self, index):
        return self.charset[index]

    # Resets the current charset.
    # @new_charset - new list of patterns.
    def hardresetCharset(self, new_charset):
        self.charset = []
        self.charset = new_charset
        return

    # Gets the filterset relative frequency.
    def getFitness(self):
        return self.fitness

    # Chages the start or and of a patern with length 3 by a vowel with 50% probability.
    # @pattern - string of characters of length 3.
    def normalize(self, pattern):
        vowels = 'aeiou'
        if ((pattern[0] in vowels) or (pattern[2] in vowels)):
            return pattern
        else:
            if self.random.uniform(0, 1) > 0.5:
                return vowels[self.random.randint(0,4)] + pattern[1] + pattern[2]
            else:
                return pattern[1] + pattern[2] + vowels[self.random.randint(0,4)]
        return

    # Generates a random list of random alphabet characters.
    def charsetInitializer(self, size):
        charset = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(size):
            rand = self.random.uniform(0, 1)
            aux = alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)]
            if rand >= 0.5:
                aux = self.normalize(alphabet[self.random.randint(0,25)] +
                alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)])
            chr = {
            "pattern": aux,
            "frequency": 0.0
            }
            charset.append(chr)

        return charset

    # Checks whether a given pattern is found within a string.
    # @name - string where the pattern is to be searched for.
    def countPatternsMatch(self, name):
        for chr in range(len(self.charset)):
            if (self.charset[chr]['pattern'] in name):
                self.charset[chr]['frequency'] += 1.0
        return

    # Calculates the average frequency each pattern within the charset was matched during processing.
    # @sample_size - number of processed test intances.
    def calculatePattenrsAvgFrequencies(self, sample_size):
        for i in range(0, len(self.charset)):
            self.charset[i]['frequency'] = self.charset[i]['frequency'] / sample_size
        return

    # Prins patterns within charset with non-zero frequency.
    def printCharset(self):
        for chr in range(len(self.charset)):
            print(self.charset[chr])
        return

    # Prins patterns within charset_aux with non-zero frequency.
    def printCharsetAux(self):
        for chr in self.charset_aux:
            print(str(chr))
        return

    # Makes charset equals to charset_aux when the number of wanted patterns is met.
    # @num_of_wanted_patterns - number of wanted non-zero frequency pattenrs.
    def getCharsetAuxLength(self, num_of_wanted_patterns):
        cur_length = len(self.charset_aux)
        correct_length = True
        if cur_length == num_of_wanted_patterns:
            self.charset = self.charset_aux
            self.charset_aux = []
            correct_length = False
        return correct_length

    # Returns the chromosome current certainty.
    def getCertainty(self):
        return self.relative_frequency

    # Increases charset length by adding the current best frequency within charset_aux.
    def selectBestPattern(self):
        chr_best = {
        "pattern": self.charset[0]['pattern'],
        "frequency": self.charset[0]['frequency']
        }

        for i in range(1, len(self.charset)):
            if self.charset[i]['frequency'] > chr_best['frequency']:
                chr_best = self.charset[i]

        right_frequency = False

        if chr_best['frequency'] > 0.0:
            right_frequency = True

        if right_frequency:
            not_present = True
            for chr in self.charset_aux:
                if chr['pattern'] == chr_best['pattern']:
                    not_present = False
            if not_present:
                self.charset_aux.append(chr_best)

        self.charset = []
        self.charset = self.charsetInitializer(self.size)

        return

    # Updates the filter's relative frequency.
    def updateFitness(self):
        frequency_sum = 0
        for pattern in self.charset:
            frequency_sum += pattern['frequency']
        self.fitness = frequency_sum / len(self.charset)
        return self.fitness
