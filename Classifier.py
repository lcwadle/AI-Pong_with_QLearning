import Image
import math
import itertools
import numpy as np
import copy

class Classifier:
    def __init__(self, training_labels, training_features, test_labels, test_features, feature_list, classes, epochs):
        self.classes = classes
        self.training_labels = training_labels
        self.training_features = training_features
        self.test_labels = test_labels
        self.test_features = test_features
        self.feature_list = feature_list
        self.epochs = epochs
        self.weights_vector = {}

        print("Initializing weights...")
        # Initialize weights and bias
        for c in classes:
            vector = []
            for i in range(len(self.feature_list) + 1):
                vector.append(np.random.randn())
            self.weights_vector[c] = np.array(vector)

    def train(self):
        print()
        print("Beginning Training...")
        # Bias Initialize
        bias = 1.0

        # Cycle through interations
        for i in range(0, self.epochs):
            correct = 0
            # alpha = 1 / (self.epochs - i)
            alpha = 0.5

            # Cycle through training data
            for j in range(0, len(self.training_labels)):
                feature_dict = self.training_features[j]
                label = self.training_labels[j]

                # Get feature value for each pixel
                feature_list = []
                for value in self.feature_list:
                    feature_list.append(float(feature_dict[value]))
                feature_list.append(float(bias))
                feature_vector = np.array(feature_list)

                # Initialize arg_,ax and predicted_class
                arg_max = 0
                predicted_class = self.classes[0]

                # Multiclass Perceptron Learning Rule
                for c in self.classes:
                    activation = np.dot(feature_vector, self.weights_vector[c])
                    if activation > arg_max:
                        arg_max = activation
                        predicted_class = c

                # Update weights
                if not (label == predicted_class):
                    self.weights_vector[label] += feature_vector * alpha
                    self.weights_vector[predicted_class] -= feature_vector * alpha
                else:
                    correct += 1

            # Display training accuracy
            print("Epoch " + str(i) + ": " + str(correct/len(self.training_labels)))

    def test(self):
        print()
        print("Beginning Testing...")
        # Bias Initialize
        bias = 1

        # Temporary dictionaries
        temp_dict = {}
        for c in self.classes:
            temp_dict[c] = 0

        # Initialize confusion matrix dictionaries
        accuracy_dict = {}
        total_dict = {}
        for c in self.classes:
            accuracy_dict[c] = copy.deepcopy(temp_dict)
            total_dict[c] = 0

        # Cycle through testing data
        correct = 0
        for j in range(0, len(self.test_labels)):
            feature_dict = self.test_features[j]
            label = self.test_labels[j]

            # Get feature value for each pixel
            feature_list = []
            for value in self.feature_list:
                feature_list.append(feature_dict[value])
            feature_list.append(bias)
            feature_vector = np.array(feature_list)

            # Initialize arg_,ax and predicted_class
            arg_max = 0
            predicted_class = self.classes[0]

            # Multiclass Perceptron Learning Rule
            for c in self.classes:
                activation = np.dot(feature_vector, self.weights_vector[c])
                if activation > arg_max:
                    arg_max = activation
                    predicted_class = c

            # Count number of accurate classifications
            if int(predicted_class) == label:
                correct += 1

            accuracy_dict[label][predicted_class] += 1

            # Count total test cases with class
            total_dict[label] += 1

        # Display testing accuracy
        print()
        print("Accuracy: " + str(correct/len(self.test_labels)))

        # Display confusion matrix
        print()
        print("Confusion Matrix:")
        print("        ", end="")
        for c1 in self.classes:
            print(c1, "     ", end="")
        print()
        for c1 in self.classes:
            print(str(c1) + "  |", end="")
            for c2 in self.classes:
                print("  " + "{0:.3f}".format(accuracy_dict[c1][c2]/total_dict[c1]), end="")
            print("  |")
