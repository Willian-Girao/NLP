#!/usr/bin/python

import random

class Crhomosome:
    def __init__(self, label, random):
        self.random = random
        self.label = label
        self.charset_aux = self.charsetInitializer()
        self.charset = []
        self.correct_avg = 0.0
        self.wrong_avg = 0.0
        self.generation_counter = 0
        self.certainty = 0.0
        self.previous_certainty = 0.0

    def normalize(self, pattern):
        vouls = 'aeiou'
        if ((pattern[0] in vouls) or (pattern[2] in vouls)):
            return pattern
        else:
            if self.random.uniform(0, 1) > 0.5:
                return vouls[self.random.randint(0,4)] + pattern[1] + pattern[2]
            else:
                return pattern[1] + pattern[2] + vouls[self.random.randint(0,4)]
        return

    def charsetInitializer(self):
        charset = []
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(100):
            rand = self.random.uniform(0, 1)
            aux = alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)]
            if rand >= 0.5:
                aux = self.normalize(alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)])

            charset.append(aux)

        return charset

    def updateChromosome(self, name, label):
        updated_charset = []
        current_charset = self.charset
        for chr in range(len(self.charset_aux)):
            if (self.charset_aux[chr] in name):
                updated_charset.append(self.charset_aux[chr])
        self.charset = updated_charset + current_charset

        completing_list = []

        for i in range((99 - len(self.charset))+1):
            alphabet = 'abcdefghijklmnopqrstuvwxyz'
            aux = alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)]
            if self.random.uniform(0, 1) >= 0.5:
                aux = self.normalize(alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)])
            completing_list.append(aux)

        self.charset_aux = []
        self.charset_aux = self.charset + completing_list

        cleaned_charset = []
        for pattern in self.charset:
            if not(pattern in cleaned_charset):
                cleaned_charset.append(pattern)

        self.charset = []
        self.charset = cleaned_charset

        self.certainty = len(cleaned_charset)

        return

    def printCharsetAux(self):
        print(self.charset_aux)
        return

    def printCharset(self):
        print(self.charset)
        return

    def getCertainty(self):
        return self.certainty

    def updateCertainty(self, sample_size, generation):
        total = (self.certainty / sample_size) / generation
        self.certainty += total



a = Crhomosome('male', random)
b = Crhomosome('male', random)

a.updateChromosome('mark', 'male')
a.updateChromosome('john', 'male')
a.updateChromosome('jonathan', 'male')
a.updateChromosome('aaron', 'male')
a.updateChromosome('rony', 'male')

b.updateChromosome('mark', 'male')
b.updateChromosome('john', 'male')
b.updateChromosome('jonathan', 'male')
b.updateChromosome('aaron', 'male')
b.updateChromosome('rony', 'male')

a.printCharset()
b.printCharset()

print(a.getCertainty())
print(b.getCertainty())

a.updateChromosome('mark', 'male')
a.updateChromosome('john', 'male')
a.updateChromosome('jonathan', 'male')
a.updateChromosome('aaron', 'male')
a.updateChromosome('rony', 'male')

b.updateChromosome('mark', 'male')
b.updateChromosome('john', 'male')
b.updateChromosome('jonathan', 'male')
b.updateChromosome('aaron', 'male')
b.updateChromosome('rony', 'male')

a.printCharset()
b.printCharset()

print(a.getCertainty())
print(b.getCertainty())

# After here ill get the best half ->
