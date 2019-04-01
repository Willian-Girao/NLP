#!/usr/bin/python

import random, time
from math import e
from evolve_filters import Population

class Neuron:
    def __init__(self, e, class_1_filter, class_2_filter, class_1_label, class_2_label,
    training_set_size, number_of_traning_steps):
        self.euler_number = e
        self.class_1_filter = class_1_filter # Patterns for class 1
        self.class_2_filter = class_2_filter # Patterns for class 2
        self.class_1_label = class_1_label # Label for class 1
        self.class_2_label = class_2_label # Label for class 2
        self.n_ij = 0.0 # Prediction certainty
        self.p_k = [] # Number of correct answers during training step k - [0,...,k].
        self.t_k = training_set_size # Number of samples in the training set k.
        self.lambda = number_of_traning_steps # Defined number of traning rounds.

    # Calculates an activation function that decides if the neuron should fire or not.
    # @n_ij_sum - the sum of all prediction certainties of the neurons within layer j.
    # @p_cik - the sum of all
    # @quocient_j - sum of all dividers for each neuron within layer j.
    def checkActivation(self, n_ij_sum, quocient_j):
        a = self.n_ij / n_ij_sum
        b_aux = 0.0
        for i in range(len(self.p_k)):
            b_aux += self.p_k[i] / self.t_k
        b = b_aux / self.lambda

        divider_j = (a * b)
        x = divider_j / quocient_j

        return 1 / (1 + (self.euler_number ** (-x)))
