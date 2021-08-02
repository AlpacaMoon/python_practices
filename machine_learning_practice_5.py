# K nearest neighbors by hand - testing

from numpy.core.numeric import full
import pandas as pd
import random
import numpy as np
import warnings
from collections import Counter


def k_nearest_neighbors(dataset, predict, k=3):
    if len(dataset) >= k:
        warnings.warn("K should be less than the amount of groups in the dataset. ")
        return
    
    distances = []
    for group in dataset:
        for feature in dataset[group]:
            distances.append([np.linalg.norm(np.array(feature) - np.array(predict)), group])

    votes = [i[1] for i in sorted(distances)][:k]
    result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k
    return result, confidence

df = pd.read_csv("datasets/Breast Cancer Wisconsin (Original) Data Set/breast-cancer-wisconsin.data")
df.replace("?", -99999, inplace=True)
df.drop('id', axis=1, inplace=True)

full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

train_set, test_set = {2: [], 4: []}, {2: [], 4: []}

test_size = 0.2
train_data = full_data[:-int(test_size * len(full_data))]
test_data = full_data[-int(test_size * len(full_data)):]

for row in train_data:
    train_set[row[-1]].append(row[:-1])
for row in test_data:
    test_set[row[-1]].append(row[:-1])

correct, total = 0, 0

for group in test_set:
    for row in test_set[group]:
        result, confidence = k_nearest_neighbors(train_set, row, k=5)
        if result == group:
            correct += 1
        else:
            print(confidence)
        total += 1
        

print(correct/total)