#!/usr/bin/python

import random

class Crhomosome:
    def __init__(self, label, random):
        self.random = random
        self.label = label
        self.charset = self.charsetInitializer()
        self.correct_avg = 0.0
        self.wrong_avg = 0.0
        self.generation_counter = 0
        self.fitness = 0.0

    def normalize(self, pattern):
        vouls = 'aeiou'
        if ((pattern[0] in vouls) or (pattern[2] in vouls)):
            return pattern
        else:
            if self.random.uniform(0, 1) > 0.5:
                return vouls[self.random.randint(0,4)] + pattern[1] + pattern[2]
            else:
                return pattern[1] + pattern[2] + vouls[self.random.randint(0,4)]




    def charsetInitializer(self):
        charset = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(100):
            rand = self.random.uniform(0, 1)
            aux = alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)]
            if rand >= 0.5:
                aux = self.normalize(alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)])

            charset.append(aux)
        print(charset)
        return charset

    def updateChromosome(self, name):
        updated_charset = []
        for chr in range(len(self.charset)):
            if (self.charset[chr] in name):
                updated_charset.append(self.charset[chr])
        self.charset = updated_charset
        return

    def printCharset(self):
        print(self.charset)
        return



single_chromosome = Crhomosome('male', random)
single_chromosome.updateChromosome('mark')
single_chromosome.printCharset()
