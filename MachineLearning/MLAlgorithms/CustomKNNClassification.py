import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')


dataset = {'k':[[1,2],[2,3],[3,1]],'r':[[6,5],[7,7],[8,6]]}
new_feature = [5,7]

# for i in dataset:
#     for ii in dataset[i]:
#         plt.scatter(ii[0], ii[1], color=i)
#
# plt.scatter(new_feature[0], new_feature[1], color='g')
# plt.show()

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
    return votes_results

results = k_nearest_neighbours(dataset, new_feature )
print(results)

for i in dataset:
    for ii in dataset[i]:
        plt.scatter(ii[0], ii[1], color=i)

plt.scatter(new_feature[0], new_feature[1], color=results)
plt.show()