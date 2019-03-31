#!/usr/bin/python

import random
from filter_class import Filterset

class Population:
    def __init__(self, size, filterset, alpha, beta):
        self.size = size
        self.filterset = filterset
        self.num_of_wanted_patterns = alpha
        self.elit_size = beta
        self.P = self.initializePopulation()

    # Initializes the population filters randomly.
    def initializePopulation(self):
        population = []
        for i in range(self.size):
            a = self.filterset('male', random, 2)
            population.append(a)
        return population

    # Finds the position the filter should be within the population based on its fintess.
    def sortFilters(self, curr_index):
        for i in range(len(self.P)):
            if (self.P[curr_index].getFitness()) > (self.P[i].getFitness()):
                save_temp = self.P[i]
                self.P[i] = self.P[curr_index]
                self.P[curr_index] = save_temp

    # Go through the data and updates each p's charset in P.
    def consumeNames(self, names_list):
        for i in range(len(self.P)):
            while self.P[i].getCharsetAuxLength(self.num_of_wanted_patterns):
                for name in names_list:
                    self.P[i].countPatternsMatch(name)
                self.P[i].calculatePattenrsAvgFrequencies(len(names_list))
                self.P[i].selectBestPattern()
            self.P[i].updateFitness()
            self.sortFilters(i)

    # Gets the n best filters in the current population.
    def getTopNFilters(self):
        for i in range(self.elit_size):
            print(self.P[i].getFitness())

def main():
    pop = Population(100, Filterset, 6, 4)
    male_names_list = []
    input = open('male_dataset_03.txt', 'r')
    for name in input:
        male_names_list.append((name.rstrip()).lower())

    pop.consumeNames(male_names_list)
    pop.getTopNFilters()
    # while a.getCharsetAuxLength(alpha):
    #     for name in male_names_list:
    #         a.searchPatterns(name)
    #
        # a.calculateAvgFrequencies(len(male_names_list))
        # a.updateCharset()
    #
    # a.printCharset()
    # print(a.updateRelativeFrequency())
    print("End.")

if __name__ == '__main__':
    main()
