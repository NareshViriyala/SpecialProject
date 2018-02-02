#test code to check all the packages installed on the system
'''
import sys
print('Python: {}'.format(sys.version))
import numpy
print('numpy: {}'.format(numpy.__version__))
import scipy
print('scipy: {}'.format(scipy.__version__))
import matplotlib
print('matplotlib: {}'.format(matplotlib.__version__))
import pandas
print('pandas: {}'.format(pandas.__version__))
import sklearn
print('sklearn: {}'.format(sklearn.__version__))

below should be the output of the above code

Python: 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
numpy: 1.14.0
scipy: 1.0.0
matplotlib: 2.1.2
pandas: 0.22.0
sklearn: 0.19.1
'''

#load libraries
import pandas
from matplotlib.pyplot import subplot
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

#load dataset
url = 'C:\\Naresh\\Github\\SpecialProject\\PurePython\\MLHelloWorld\\IrisData.txt'
names = ['sepal-length','sepal-width','petal-length','petal-width','class']
dataset = pandas.read_csv(url,names=names)

#shape of data
#print(dataset.shape)

#head of data
#print(dataset.head(20))

#description
#print(dataset.describe())

#calss distribution
#print(dataset.groupby('class').size())


dataset.plot(kind='area', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

'''
dataset.hist()
plt.show()
'''

'''
scatter_matrix(dataset)
plt.show()
'''
array = dataset.values
X = array[:,0:4]
Y = array[:,4]
validation_size = 0.20
seed = 7
X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(X, Y, test_size=validation_size,  random_state=seed)

#test options and evaluation metircs
scoring = 'accuracy'

'''
#spot check algorithms
models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))
models.append(('SVM', SVC()))

#evaluate each model in turn
results = []
names = []


for name, model in models:
    kfold = model_selection.KFold(n_splits=10, random_state=seed)
    cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()
'''

'''
knn = KNeighborsClassifier()
knn.fit(X_train, Y_train)
predictions = knn.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))
'''



