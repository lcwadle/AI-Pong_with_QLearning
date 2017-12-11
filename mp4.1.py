import Classifier
import K_Nearest_Neighbor_Classifier
import timeit

# Read and format the training data
image_size_x = 28
image_size_y = 28
raw_train_features = open("data/trainingimages.txt", 'r')
raw_train_labels = open("data/traininglabels.txt", 'r')

print("Loading Training Labels...")
# Convert training labels to array
training_labels = []
for label in raw_train_labels.read().splitlines():
    training_labels.append(int(label))

print("Loading Training Features...")
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

print("Loading Testing Labels...")
# Convert test labels to array
test_labels = []
for label in raw_test_labels.read().splitlines():
    test_labels.append(int(label))

print("Loading Testing Features...")
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

print("Building Class Array...")
# Class array
classes = []
for i in range(0, 10):
    classes.append(i)

print("Building Feature List...")
# Feature List
feature_list = []
for i in range(image_size_x * image_size_y):
    feature_list.append(i)

# Create Classifier
#classifier = Classifier.Classifier(training_labels, training_features, test_labels, test_features, feature_list, classes, 40)
#classifier.train()
#classifier.test()
classifier = K_Nearest_Neighbor_Classifier.K_Nearest_Neighbor_Classifier(training_labels, training_features, test_labels, test_features, feature_list, classes, 5)

start = timeit.default_timer()

classifier.test()

stop = timeit.default_timer()

print()
print("Running time: " + str(stop - start))
