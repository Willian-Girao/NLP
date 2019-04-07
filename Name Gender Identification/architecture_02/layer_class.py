#!/usr/bin/python

import time
from math import e

from evolve_filters import Population
from neuron_class import Neuron
from filter_class import Filterset

class Layer:
    def __init__(self, Population, Neuron, Filterset, MaleNameList, FemaleNameList, neurons_num, charset_length):
        self.population = Population
        self.neuron = Neuron
        self.filterset = Filterset
        self.neurons_num = neurons_num
        self.charset_length = charset_length
        self.male_names_list = MaleNameList
        self.male_filters = self.maleBuildFilters()
        self.female_names_list = FemaleNameList
        self.female_filters = self.femaleBuildFilters()
        self.neuron_array = self.synthesizeNeurons(self.male_filters, self.female_filters)

    def maleBuildFilters(self):
        print("Optimizing male filters...")
        # Population(size_of_pop, Filters_class, charset_length, elite_size, number_of_generations, label)
        pop = self.population(100, self.filterset, self.charset_length, (self.neurons_num * 10), 50, 'male')
        filter = pop.findOptimalFilters(self.male_names_list)
        return filter

    def femaleBuildFilters(self):
        print("Optimizing female filters...")
        # Population(size_of_pop, Filters_class, charset_length, elite_size, number_of_generations, label)
        pop = self.population(100, self.filterset, self.charset_length, (self.neurons_num * 10), 50, 'female')
        filter = pop.findOptimalFilters(self.female_names_list)
        return filter

    def synthesizeNeurons(self, male_filters, female_filters):
        print("Synthesizing neurns...")
        print("\n")
        neurons = []
        for i in range(self.neurons_num):
            neuron_i = self.neuron(male_filters[i], female_filters[i], "male", "female")
            neurons.append(neuron_i)
        return neurons

    def printMaleFilters(self):
        count = 0
        for filter in self.male_filters:
            print("Male filter: " + str(count))
            for f in filter:
                print(f)
            count += 1
            print("\n")

    def printFemaleFilters(self):
        count = 0
        for filter in self.female_filters:
            print("Female filter: " + str(count))
            for f in filter:
                print(f)
            count += 1
            print("\n")

    def printSingleNeuron(self, index):
        self.neuron_array[index].printLabels()

    def layerFoward(self, target):
        for neuron in self.neuron_array:
            neuron.predict(target)

    def printNeuronsPredictions(self):
        for neuron in self.neuron_array:
            neuron.printPrediction()

    def printAverageValues(self):
        man = 0.0
        women = 0.0
        for neuron in self.neuron_array:
            if neuron.getPredictedLabel() == "male":
                man += neuron.getPredictedCertainty()
            elif neuron.getPredictedLabel() == "female":
                women += neuron.getPredictedCertainty()
            else:
                pass

        print("Male: " + str(man) + " - Female: " + str(women))


def main():
    male_names_list = []
    female_names_list = []

    male_inpute_file = open('male_dataset_03.txt', 'r')
    for name in male_inpute_file:
        male_names_list.append((name.rstrip()).lower())

    female_inpute_file = open('female_dataset_03.txt', 'r')
    for name in female_inpute_file:
        female_names_list.append((name.rstrip()).lower())

    layer_j = Layer(Population, Neuron, Filterset, male_names_list, female_names_list, 8, 12)
    # layer_j.printMaleFilters()
    # layer_j.printFemaleFilters()
    # layer_j.printSingleNeuron(0)
    layer_j.layerFoward("suzan")
    layer_j.printNeuronsPredictions()
    print("\n")
    layer_j.printAverageValues()
    layer_j.layerFoward("rebecca")
    layer_j.printNeuronsPredictions()
    print("\n")
    layer_j.printAverageValues()

if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print("Execution time (s): ", end = "")
    print(end - start)
