import Classifier
import timeit

# Read and format the training data
image_size_x = 28
image_size_y = 28
raw_train_features = open("data/trainingimages.txt", 'r')
raw_train_labels = open("data/traininglabels.txt", 'r')

# Convert training labels to array
training_labels = []
for label in raw_train_labels.read().splitlines():
    training_labels.append(label)

# Convert traing feature set to array
training_features = []
feature = {}
i = 0
j = 0
for line in raw_train_features.read().splitlines():
    if (i+1) % (image_size_y) == 0:
        for c in line:
            if c == ' ':
                feature[j] = 0
            else:
                feature[j] = 1
            j += 1
        training_features.append(feature)
        feature = {}
        j = 0
    else:
        for c in line:
            if c == ' ':
                feature[j] = 0
            else:
                feature[j] = 1
            j += 1
    i += 1

# Read and format testing data
raw_test_features = open("data/testimages.txt", 'r')
raw_test_labels = open("data/testlabels.txt", 'r')

# Convert test labels to array
test_labels = []
for label in raw_test_labels.read().splitlines():
    test_labels.append(label)

# Convert traing feature set to array
test_features = []
feature = {}
i = 0
j = 0
for line in raw_test_features.read().splitlines():
    if (i+1) % (image_size_y) == 0:
        for c in line:
            if c == ' ':
                feature[j] = 0
            else:
                feature[j] = 1
            j += 1
        test_features.append(feature)
        feature = {}
        j = 0
    else:
        for c in line:
            if c == ' ':
                feature[j] = 0
            else:
                feature[j] = 1
            j += 1
    i += 1

# Class array
classes = []
for i in range(0, 10):
    classes.append(i)
