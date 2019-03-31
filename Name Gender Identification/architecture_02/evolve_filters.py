#!/usr/bin/python

import random, time
from filter_class import Filterset

class Population:
    def __init__(self, size, filterset, alpha, beta, generations):
        self.size = size
        self.filterset = filterset
        self.num_of_wanted_patterns = alpha
        self.elit_size = beta
        self.generations = generations
        self.P = self.initializePopulation()

    # Initializes the population filters randomly.
    def initializePopulation(self):
        population = []
        for i in range(self.size):
            a = self.filterset('male', random, self.num_of_wanted_patterns)
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
        return

    # Print the fitness of the current filter in the population.
    def printPopulationFitness(self):
        for filter in self.P:
            print(filter.getFitness())

    def combineBestPatterns(self, a, b):
        best_patterns = []
        for i in range(self.num_of_wanted_patterns):
            a_pattern = a.getSinglePattern(i)
            b_pattern = b.getSinglePattern(i)

            if a_pattern['frequency'] > b_pattern['frequency']:
                best_patterns.append(a_pattern)
            else:
                best_patterns.append(b_pattern)

        n = self.filterset('male', random, self.num_of_wanted_patterns)
        n.hardresetCharset(best_patterns)
        n.updateFitness()
        self.P.append(n)

        return


    # Gets the n best filters in the current population.
    def selectCombineAndComplete(self):
        best_filters = []

        for i in range(self.elit_size):
            best_filters.append(self.P[i])
        self.P = []
        self.P = best_filters

        for i in range(0, self.elit_size, 2):
            self.combineBestPatterns(self.P[i], self.P[i+1])

        for i in range((self.size - len(self.P))):
            a = self.filterset('male', random, self.num_of_wanted_patterns)
            self.P.append(a)

        return

    def printBest(self):
        best_filters = []
        for i in range(self.elit_size):
            best_filters.append(self.P[i])

        for filter in best_filters:
            print(filter.getFitness())

    def findOptimalFilters(self, male_names_list):
        for i in range(self.generations):
            print("Generation " + str(i))
            self.consumeNames(male_names_list)
            self.selectCombineAndComplete()
        self.printBest()
        return

def main():
    male_names_list = []
    input = open('male_dataset_03.txt', 'r')
    for name in input:
        male_names_list.append((name.rstrip()).lower())

    # Population(size_of_pop, Filters class, charset_length, elite_size, number_of_generations)
    pop = Population(100, Filterset, 9, 40, 100)
    pop.findOptimalFilters(male_names_list)

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Execution time (s): ", end = "")
    print(end - start)
