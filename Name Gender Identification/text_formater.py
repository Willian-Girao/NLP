#!/usr/bin/python

import sys
import os

def format(file_name, output_name):
    input_file = open(file_name, "r")
    output_file = open(output_name, "a+")
    for line in input_file:
        x = line.split()
        name = x[1]
        s = ""
        is_first = True
        for l in name:
            if is_first:
                s += l.upper()
                is_first = False
            else:
                s += l
        output_file.write(s + "\n")
    return

def removeReplicates(file_name, output_name):
    input_file = open(file_name, "r")
    output_file = open(output_name, "a+")
    name_list = []
    final_list = []

    for name in input_file:
        name_list.append(name)

    for name in name_list:
        if not(name in final_list):
            final_list.append(name)

    for name in final_list:
        output_file.write(name)

    return

def sort(file_name, output_name):
    output_file = open(output_name, "a+")
    letters_list = []

    for i in range(26):
        letters_list.append(i)

    for index in letters_list:
        input_file = open(file_name, "r")
        for name in input_file:
            if name[0] == chr((index + 65)):
                output_file.write(name)


format("White-Female-Names.txt", "female_dataset_01.txt")
format("White-Male-Names.txt", "male_dataset_01.txt")

removeReplicates("female_dataset_01.txt", "female_dataset_02.txt")
removeReplicates("male_dataset_01.txt", "male_dataset_02.txt")

sort("female_dataset_02.txt", "female_dataset_03.txt")
sort("male_dataset_02.txt", "male_dataset_03.txt")
