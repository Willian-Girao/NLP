#!/usr/bin/python

import random, time
from math import e
from evolve_filters import Population

class Neuron:
    def __init__(self, class_1_filter, class_2_filter, class_1_label, class_2_label):
        self.class_1_filter = class_1_filter # Patterns for class 1.
        self.class_2_filter = class_2_filter # Patterns for class 2.
        self.class_1_label = class_1_label # Label for class 1.
        self.class_2_label = class_2_label # Label for class 2.
        self.n_ij = 0.0 # Prediction certainty.
        self.predicted_label = "none" # The label the neuron has predicted.
        self.sig_p_nxj = 0.0 # Activation function value.

    # Calculates the averge matchs in 'target' using 'class_filter'.
    # @class_filter - set of characters to be matched.
    # @target - string where the patterns will try to be matched against.
    def classPrediction(class_filter, target):
        match_avg = 0.0
        for chr in class_filter:
            if chr['pattern'] in target:
                match_avg += 1.0
        return (match_avg / len(class_filter))

    # Decides which label should be given to the target sample to be classified.
    # @target - data to be classified.
    def predict(self, target):
        class_1_certainty = classPrediction(self.class_1_filter, target)
        class_2_certainty = classPrediction(self.class_2_filter, target)

        self.n_ij = max(class_1_certainty, class_2_certainty)

        if class_1_certainty == class_2_certainty:
            self.predicted_label = "undecidable"
        elif class_1_certainty > class_2_certainty:
            self.predicted_label = self.class_1_label
        else:
            self.predicted_label = self.class_2_label
