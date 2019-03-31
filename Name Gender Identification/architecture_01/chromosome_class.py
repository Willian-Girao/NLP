#!/usr/bin/python

import random

class Crhomosome:
    def __init__(self, label, random):
        self.random = random
        self.label = label
        self.charset = self.charsetInitializer()
        self.charset_aux = []
        self.correct = 0
        self.wrong = 0
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
        for i in range(300):
            rand = self.random.uniform(0, 1)
            aux = alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)]
            if rand >= 0.5:
                aux = self.normalize(alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)] + alphabet[self.random.randint(0,25)])
            chr = {
            "pattern": aux,
            "frequency": 0.0
            }
            charset.append(chr)

        return charset

    def searchPatterns(self, name, label):
        for chr in range(len(self.charset)):
            if (self.charset[chr]['pattern'] in name):
                self.charset[chr]['frequency'] += 1.0
        return

    def calculateAvgFrequencies(self, sample_size):
        for i in range(0, len(self.charset)):
            self.charset[i]['frequency'] = self.charset[i]['frequency'] / sample_size
        return

    def printCharset(self):
        for chr in self.charset:
            if (chr['frequency'] > 0.0):
                print(str(chr))
        return

    def printCharsetAux(self):
        for chr in self.charset_aux:
            if (chr['frequency'] > 0.0):
                print(str(chr))
        return

    def getCharsetAuxLength(self, defined_length):
        cur_length = len(self.charset_aux)
        if cur_length == defined_length:
            self.charset = self.charset_aux
            self.charset_aux = []
        return cur_length

    def getCertainty(self):
        return self.certainty

    def updateCertainty(self, sample_size, generation):
        total = (self.certainty / sample_size) / generation
        self.certainty += total

    def updateCharset(self):
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
        self.charset = self.charsetInitializer()

        return

    # def predict(self, name):
    #     matches_count = 0
    #     frequency_sum = 0.0
    #     for chr in self.charset:
    #         frequency_sum += chr['frequency']
    #         if (chr['pattern'] in name):
    #             matches_count += 1
    #
    #     matches_avg = frequency_sum / len(self.charset)
    #     if matches_avg > 0.5:
    #         self.correct += 1
    #         print('\nlabel: ' + self.label)
    #         print('\ncertainty: ' + str(matches_avg))
    #         return self.label
    #     else:
    #         self.wrong += 1
    #         print('female')


a = Crhomosome('male', random)

while a.getCharsetAuxLength(3) < 3:
    a.searchPatterns('mark', 'male')
    a.searchPatterns('john', 'male')
    a.searchPatterns('jonathan', 'male')
    a.searchPatterns('aaron', 'male')
    a.searchPatterns('rony', 'male')
    a.searchPatterns('johnson', 'male')
    a.searchPatterns('jonny', 'male')

    a.calculateAvgFrequencies(5)
    a.updateCharset()

a.printCharset()
# a.predict('jonathan')
#
#
# a.printCharset()
# b.printCharset()
#
# print(a.getCertainty())


# After here ill get the best half ->
