import Image
import math
import itertools

class Classifier:
    def __init__(self, training_labels, training_features, test_labels, test_features, classes, epochs):
        self.classes = classes
        self.training_labels = training_labels
        self.training_features = training_features
        self.test_labels = test_lables
        self.test_features = test_features
        self.epochs = epochs
        self.weights = {}

        # Initialize weights and bias
        for c in classes:
            vector = []
            for i in range(len(training_features) + 1):
                vector.append(0)
            self.weights[c] = vector

    def train(self):
        # Cycle through interations
        for i in range(0, self.epochs):


            # Multiclass Perceptron Learning Rule
            for c in self.classes:
                
