import pandas as pd

dataset = pd.read_excel('dataset_tablet_smartphone.xlsx')

dataset.dtypes

cleanup = {"Portatil": {"Smartphone": 1, "Tablet": 2}}

dataset.replace(cleanup, inplace=True)
dataset.head()

dataset.replace(['Smartphone', 'Tablet'], [1, 2])

y = dataset.Portatil
X = dataset.drop(columns = ['Portatil'])

from sklearn. tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4)
clf = DecisionTreeClassifier()
clf.fit(X_train,y_train)

from sklearn import metrics

print("Precision" + str(metrics.precision_score(y_true, y_pred)))