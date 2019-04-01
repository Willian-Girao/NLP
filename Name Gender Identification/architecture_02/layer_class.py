#!/usr/bin/python

import time
from math import e

from evolve_filters import Population
from neuron_class import Neuron
from filter_class import Filterset

class Layer:
    def __init__(self, Population, Neuron, Filterset, NameList):
        self.population = Population
        self.neuron = Neuron
        self.female_filters = []
        self.filterset = Filterset
        self.male_names_list = NameList
        self.male_filters = self.buildFilters()

    def buildFilters(self):
        # Population(size_of_pop, Filters_class, charset_length, elite_size, number_of_generations)
        pop = self.population(100, self.filterset, 2, 40, 1, 'male')
        filter = pop.findOptimalFilters(self.male_names_list)
        return filter

    def printMaleFilters(self):
        for filter in self.male_filters:
            print(filter)


def main():
    male_names_list = []
    input = open('male_dataset_03.txt', 'r')
    for name in input:
        male_names_list.append((name.rstrip()).lower())

    layer_j = Layer(Population, Neuron, Filterset, male_names_list)
    layer_j.printMaleFilters()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Execution time (s): ", end = "")
    print(end - start)
