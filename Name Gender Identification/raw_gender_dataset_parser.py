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

        if not self.os.path.exists("subdivided_gender_dataset"):
            self.os.makedirs("subdivided_gender_dataset")

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
        return

    @staticmethod
    def getFileLine(file_name, line_index, max_lines):
        count_aux = 0
        for j in file_name:
            if (count_aux == line_index):
                return j
                break
            else:
                count_aux += 1
        return

    def generateTrainingTestIndexes(self, training_size, test_size):
        # random.randint(x,y) - number between x and y-1
        training_indexes = []
        test_indexes = []
        aux_indexes_list = []

        for i in range((training_size + test_size)):
            aux_indexes_list.append(i)

        # while ((len(test_indexes) != test_size-1) and (len(training_indexes) != training_size-1)):
        for i in range(len(aux_indexes_list)):
            rand = self.random.uniform(0, 1)
            append_to_trainning = True
            if rand >= 0.5:
                append_to_trainning = False
            if append_to_trainning:
                if (not(aux_indexes_list[i] in training_indexes) and not(aux_indexes_list[i] in test_indexes) and (len(training_indexes) < training_size)):
                    training_indexes.append(aux_indexes_list[i])
            else:
                if (not(aux_indexes_list[i] in training_indexes) and not(aux_indexes_list[i] in test_indexes)  and (len(test_indexes) < test_size)):
                    test_indexes.append(aux_indexes_list[i])

        if len(training_indexes) < training_size:
            count = 0
            while len(training_indexes) < training_size:
                if ((count in training_indexes) or (count in test_indexes)):
                    count += 1
                else:
                    training_indexes.append(count)

        if len(test_indexes) < test_size:
            count = 0
            while len(test_indexes) < test_size:
                if ((count in training_indexes) or (count in test_indexes)):
                    count += 1
                else:
                    test_indexes.append(count)


        # print(str(training_indexes) + " -> " + str(len(training_indexes)) + " / " + str(training_size))
        # print(str(test_indexes) + " -> " + str(len(test_indexes)) + " / " + str(test_size))
        return [training_indexes, test_indexes]


    def devideTrainingTestData(self, training_percentage):
        if not self.os.path.exists("training_set"):
            self.os.makedirs("training_set")
        if not self.os.path.exists("test_set"):
            self.os.makedirs("test_set")

        script_dir = self.os.path.dirname(__file__)
        trainig_path = "training_set/"
        test_path = "test_set/"

        total_trainning_samples = 0
        total_test_samples = 0

        for i in range(26):
            s = chr((i + 65)) + "_dataset.txt"
            final_path = "subdivided_gender_dataset/" + s
            abs_file_path = self.os.path.join(script_dir, final_path)
            single_dataset_file = open(abs_file_path, "r")

            tr_out_path = self.os.path.join(script_dir, "training_set/training_data.txt")
            ts_out_path = self.os.path.join(script_dir, "test_set/test_data.txt")

            output_trainning_file = open(tr_out_path, "a+")
            output_test_file = open(ts_out_path, "a+")

            lines_count = 0
            for i in single_dataset_file:
                lines_count += 1

            training_sample_amount = int((lines_count * training_percentage) / 100)
            test_sample_amount = (lines_count - training_sample_amount)

            print("\nDataset: " + s)
            print("Dataset partition: Training " + str(training_sample_amount) + " / Test " + str(test_sample_amount))
            total_trainning_samples += training_sample_amount
            total_test_samples += test_sample_amount

            training_indexes = []
            test_indexes = []
            count_aux = 0

            indexes_lists = self.generateTrainingTestIndexes(training_sample_amount, test_sample_amount)

            print("Generating training data...", end = '')
            for i in range(len(indexes_lists[0])):
                single_dataset_file = open(abs_file_path, "r")
                output_trainning_file.write(self.getFileLine(single_dataset_file, indexes_lists[0][i], lines_count))
            print("[ DONE ]")

            print("Generating test data...", end = '')
            for i in range(len(indexes_lists[1])):
                single_dataset_file = open(abs_file_path, "r")
                output_test_file.write(self.getFileLine(single_dataset_file, indexes_lists[1][i], lines_count))
            print("[ DONE ]")

        print("\nTotal TRAINNING samples: " + str(total_trainning_samples+1))
        print("Total TEST samples: " + str(total_test_samples+1))


        return



decideLettersCount = FirstLetterSegmentation(str(sys.argv[1]), str(sys.argv[2]), os, random)

decideLettersCount.individualWordCountPerGender()
decideLettersCount.generateSubdividedDataset()
decideLettersCount.devideTrainingTestData(75)
