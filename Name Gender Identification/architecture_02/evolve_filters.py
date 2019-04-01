#!/usr/bin/python

import random, time

class Population:
    def __init__(self, size, filterset, alpha, beta, generations, class_label):
        self.size = size
        self.filterset = filterset
        self.num_of_wanted_patterns = alpha
        self.elit_size = beta
        self.generations = generations
        self.class_label = class_label
        self.P = self.initializePopulation()

    # Initializes the population filters randomly.
    def initializePopulation(self):
        population = []
        for i in range(self.size):
            a = self.filterset('male', random, self.num_of_wanted_patterns)
            population.append(a)
        return population

    # Finds the position the filter should be within the population based on its fintess.
    # @curr_index - index of the filter within the population to be put in the right place.
    def sortFilters(self, curr_index):
        for i in range(len(self.P)):
            if (self.P[curr_index].getFitness()) > (self.P[i].getFitness()):
                save_temp = self.P[i]
                self.P[i] = self.P[curr_index]
                self.P[curr_index] = save_temp

    # Go through the data and updates each p's charset in P.
    # @names_list - list containing all the names to be processed.
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

    # Combines two filter's charset to create a single one with their best elements.
    # @a - filter 1
    # @b - filter 2
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

    # Returns 10% of the elit solutions found at the end of the process.
    def returnFilters(self):
        output = open('male_filters.txt', 'w+')
        best_filters = []
        for i in range(int(self.elit_size/10)):
            self.P[i].clearFrequency()
            best_filters.append(self.P[i].retrieveCharset())
            output.write(str(self.P[i].retrieveCharset()) + "\n")

        return best_filters

    # Performs the evolutionary process to find filters.
    def findOptimalFilters(self, male_names_list):
        for i in range(self.generations):
            self.consumeNames(male_names_list)
            self.selectCombineAndComplete()
        filters = self.returnFilters()
        return filters
