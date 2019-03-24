#!/usr/bin/python

import sys
import os
import random

class FirstLetterSegmentation:
    def __init__(self, male_list, female_list, os, random):
        self.male_list = male_list
        self.female_list = female_list
        self.os = os
        self.random = random

    @staticmethod
    def nameLabel(name, label):
        s = ""
        for x in range(len(name)-1):
            s += name[x]
        s += ";"
        for x in range(len(label)):
            s += label[x]
        return s

    @staticmethod
    def toMetaInfo(letter, initial_amount, final_amount):
        return ("Starting with " + letter + ": " + str(final_amount) + "/" + str(initial_amount) + "\n")

    @staticmethod
    def countFirstLetterOccurances(letter, list):
        try:
            list[(ord(letter) - 65)]['count'] += 1
            return
        except IndexError:
            obj = {
            "letter": letter,
            "count": 1
            }
            list.insert((ord(letter) - 65), obj)
            return

    def firstLettersToFile(self, file_name):
        name_list = open(file_name, "r")
        output_name = "word_counter_" + file_name
        output = open(output_name, "w")

        list = []

        for name in name_list:
            self.countFirstLetterOccurances(name[0], list)

        for index in list:
            output.write(str(index))
            output.write("\n")

        print("File '" + file_name + "' has finished being processed.")

        return

    def firstLetterCountoList(self, file_name):
        name_list = open(file_name, "r")
        list = []

        for name in name_list:
            self.countFirstLetterOccurances(name[0], list)

        return list

    def individualWordCountPerGender(self):
        print("\nProcessing text files...")
        self.firstLettersToFile(self.male_list)
        self.firstLettersToFile(self.female_list)
        print("[ DONE ]\n")

    def saveWordToFile(self, input_male_file, input_female_file, letter, total_count):
        current_count_male = 0
        current_count_female = 0

        script_dir = self.os.path.dirname(__file__)
        final_path = "subdivided_gender_dataset/" + letter + "_dataset.txt"
        output_file = open(final_path, "a+")

        male_names = []
        female_names = []

        for name in input_male_file:
            if ((letter == name[0]) and not("-" in name) and (current_count_male < total_count)):
                male_names.append(name)
                current_count_male += 1

        for name in input_female_file:
            if ((letter == name[0]) and not("-" in name) and (current_count_female < total_count)):
                female_names.append(name)
                current_count_female += 1

        if len(male_names) == len(female_names):
            for i in range(len(male_names)):
                rand = self.random.uniform(0, 1)
                if rand >= 0.5:
                    output_file.write(self.nameLabel(male_names[i], 'male')+"\n")
                else:
                    output_file.write(self.nameLabel(female_names[i], 'female')+"\n")

        return [current_count_male, current_count_female]

    def generateSubdividedDataset(self):
        print("\nDefining sample set for each letter...")
        male_list_aux = self.firstLetterCountoList(self.male_list)
        female_list_aux = self.firstLetterCountoList(self.female_list)
        if not self.os.path.exists("subdivided_gender_dataset"):
            self.os.makedirs("subdivided_gender_dataset")

        if (len(male_list_aux) == len(female_list_aux)):
            script_dir = self.os.path.dirname(__file__)
            final_path = "subdivided_gender_dataset/metada.txt"
            abs_file_path = self.os.path.join(script_dir, final_path)
            meta_file = open(abs_file_path, "a+")
            for index in range(len(male_list_aux)):
                male_file = open(self.male_list, "r")
                female_file = open(self.female_list, "r")

                if (male_list_aux[index]['count'] <
                female_list_aux[index]['count']):
                    total_count = self.saveWordToFile(
                    male_file,
                    female_file,
                    male_list_aux[index]['letter'],
                    male_list_aux[index]['count']
                    )
                else:
                    total_count = self.saveWordToFile(
                    male_file,
                    female_file,
                    female_list_aux[index]['letter'],
                    female_list_aux[index]['count']
                    )

                meta_file.write(self.toMetaInfo(
                male_list_aux[index]['letter'],
                (male_list_aux[index]['count'] + female_list_aux[index]['count']),
                (total_count[0] + total_count[1])
                ))
        print("[ DONE ]\n")



decideLettersCount = FirstLetterSegmentation(str(sys.argv[1]), str(sys.argv[2]), os, random)
decideLettersCount.individualWordCountPerGender()
decideLettersCount.generateSubdividedDataset()
