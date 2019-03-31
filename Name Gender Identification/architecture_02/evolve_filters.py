#!/usr/bin/python

import random
from filter_class import Filterset



male_names_list = []
input = open('male_dataset_03.txt', 'r')
for name in input:
    male_names_list.append((name.rstrip()).lower())

alpha = 6 # Wanted number of patterns.

a = Filterset('male', random)

while a.getCharsetAuxLength(alpha):
    for name in male_names_list:
        a.searchPatterns(name)

    a.calculateAvgFrequencies(len(male_names_list))
    a.updateCharset()

a.printCharset()
print(a.updateRelativeFrequency())
