import random
import warnings
import pandas as pd
import numpy as np
from collections import Counter

def k_nearest_neighbours(data, predict, k=3):
    if len(data) >= k:
        warnings.warn('k is set to a value less than total voting groups!')

    distances = []
    for group in data:
        for feature in data[group]:
            # euclidean_distance = sqrt((feature[0] - predict[0])**2 + (feature[1] - predict[1])**2) #good for 2 dimension array
            #euclidean_distance = np.sqrt(np.sum((np.array(feature) - np.array(predict)) **2))  # good for n dimensions using numpy array
            euclidean_distance = np.linalg.norm(np.array(feature) - np.array(predict)) # this is same as above 2 operations but using inbuilt method
            distances.append([euclidean_distance, group])

    votes = [i[1] for i in sorted(distances)[:k]]
    votes_results = Counter(votes).most_common(1)[0][0]
    confidence = Counter(votes).most_common(1)[0][1]/k
    return votes_results,confidence

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?',-99999,inplace=True)
df.drop(['id'], 1, inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size=0.2
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[-int(test_size*len(full_data)):]


train_set = {2:[], 4:[]}
test_set = {2:[], 4:[]}

for i in train_data:
    train_set[i[-1]].append(i[:-1])

for i in test_data:
    test_set[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote, confidence = k_nearest_neighbours(train_set, data, k=5)
        if vote == group:
            correct += 1
        if confidence != 1.0 and vote != group:
            print(confidence,vote,group)
        total += 1

print('accuracy = ', correct/total)