import numpy as np
from sklearn import preprocessing, model_selection, neighbors
import pandas as pd

df = pd.read_csv('breast-cancer-wisconsin.data.txt')
df.replace('?',-99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['Class'], 1))
y = np.array(df['Class'])
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)
accuracy = clf.score(X_test, y_test)

example_measure = np.array([[4,2,1,1,1,2,3,2,1], [10,1,1,1,1,1,9,7,1]])
# example_measure = example_measure.reshape(1, -1)
prediction = clf.predict(example_measure)
print(prediction)

print(accuracy)