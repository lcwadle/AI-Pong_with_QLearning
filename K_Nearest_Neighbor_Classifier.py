import copy
import math

class K_Nearest_Neighbor_Classifier:
    def __init__(self, training_labels, training_features, test_labels, test_features, feature_list, classes, k):
        self.classes = classes
        self.training_labels = training_labels
        self.training_features = training_features
        self.test_labels = test_labels
        self.test_features = test_features
        self.feature_list = feature_list
        self.k = k

    def test(self):
        print()
        print("Beginning training...")

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

        # Cycle through testing set
        correct = 0
        for j in range(0, len(self.test_features)):
            label = self.test_labels[j]

            # Initialize lowest distances list
            lowest_distances = []
            for l in range(0, self.k):
                lowest_distances.append((float("inf"), self.classes[0]))

            # Cycle through training set
            distance = 0
            for i in range (0, len(self.training_features)):

                # Cycle through features
                for feature in self.feature_list:

                    # Calculate distance
                    distance += (self.test_features[j][feature] - self.training_features[i][feature]) ** 2
                distance = math.sqrt(distance)

                # If least k distances
                for d, c in lowest_distances:
                    if distance < d:
                        lowest_distances.append((distance, self.training_labels[i]))
                        lowest_distances.sort()
                        del lowest_distances[len(lowest_distances) - 1]

                #print(lowest_distances)

            # Calculate best label
            nearest_neightbor_dict = {}
            for i in range(0, self.k):
                if lowest_distances[i][1] in nearest_neightbor_dict:
                    nearest_neightbor_dict[lowest_distances[i][1]] += 1
                else:
                    nearest_neightbor_dict[lowest_distances[i][1]] = 1

            predicted_class = max(nearest_neightbor_dict, key=(lambda key: nearest_neightbor_dict[key]))

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
