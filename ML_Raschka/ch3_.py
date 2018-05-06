import sklearn
from sklearn import datasets
import numpy as np
import dec_reg
import matplotlib.pyplot as plt

print(sklearn.__version__)
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target

print('Class labels:', np.unique(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

from sklearn.linear_model import Perceptron
ppn = Perceptron(max_iter=40, eta0=0.01, random_state=0)
ppn.fit(X_train_std, y_train) #Values, target

y_pred = ppn.predict(X_test_std)
print('Misslcassified samples: %d' % (y_test != y_pred).sum())

X_combined_std = np.vstack((X_train_std, X_test_std)) #Vertical stack of matrixes
y_combined = np.hstack((y_train, y_test))
dec_reg.plot_decision_regions(X=X_combined_std, y=y_combined, classifier=ppn, test_idx=range(105,150)) #45 ostatnich to test
plt.xlabel('petal length [std]')
plt.ylabel('petal width [std]')
plt.legend(loc='best')
plt.show()
