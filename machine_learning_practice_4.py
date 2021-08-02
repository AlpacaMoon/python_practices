# K nearest neighbors by hand

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
from random import randrange
import warnings
from collections import Counter

plt.style.use('ggplot')

def create_features_from_center(center= [0,0], deviation=1, n=1):
    return [[randrange(center[i]-deviation, center[i]+deviation) for i in range(len(center))] for _ in range(n)]

def k_nearest_neighbors(dataset, predict, k=3):
    if len(dataset) >= k:
        warnings.warn("K should be less than the amount of groups in the dataset. ")
        return
    
    distances = []
    for group in dataset:
        for feature in dataset[group]:
            # Way 1 (Fastest)
            distances.append([np.linalg.norm(np.array(feature) - np.array(predict)), group])

            # # Way 2
            # distances.append([np.sqrt(np.sum((np.array(feature) - np.array(predict))**2)), group])
 
            # # Way 3
            # distances.append([sqrt(sum([(feature[i] - predict[i])**2 for i in range(len(feature))])), group])


    # Shortest form: 
    # distances = [[np.linalg.norm(np.array(feature) - np.array(predict)), group] for feature in dataset[group] for group in dataset]

    votes = [i[1] for i in sorted(distances)][:k]
    result = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1] / k
    return result, confidence


dataset = {'red': create_features_from_center([10,10], 20, 20), 'blue': create_features_from_center([30,30], 20, 20)}
new_feature = create_features_from_center([20,20], 5, 1)[0]

result_group, confidence = k_nearest_neighbors(dataset, new_feature, 3)

print(dataset)
print(new_feature)
print(result_group, confidence)

for group in dataset:
    for pt in dataset[group]:
        plt.scatter(pt[0], pt[1], color=group)

plt.scatter(new_feature[0], new_feature[1], color=result_group, marker='x')

plt.show()

