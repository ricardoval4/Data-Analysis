# -*- coding: utf-8 -*-
"""Salinan dari Session 31 - Classification 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1clw5N4WmjsuX3gNOgoPpd8kpwxY9JzI_

# Import Libraries
"""

import pandas as pd, numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/gdrive')

"""# Load Dataset"""

path = '/content/gdrive/MyDrive/Colab Notebooks/Dataset Latihan/social_network_ads.csv'
dataset = pd.read_csv(path)
dataset.head()

"""# Train Test Split"""

X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

""" # Scaling"""

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

X_train = pd.DataFrame(X_train, columns=X.columns)
X_test = pd.DataFrame(X_test, columns=X.columns)

"""# Model Training"""

from sklearn.neighbors import KNeighborsClassifier
classifier = KNeighborsClassifier(n_neighbors=7)
classifier.fit(X_train, y_train)

y_test_pred = classifier.predict(X_test)

"""# Model Evaluation"""

from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_test_pred)

y_train_pred = classifier.predict(X_train)
accuracy_score(y_train, y_train_pred)

"""#Search K optimum"""

def search_k(X_train, X_test, y_train, y_test, maximum_k=7):
    acc_train = []
    acc_test = []
    ks = range(1, maximum_k+1)
    for k in ks:
        # Train based on number of K
        classifier = KNeighborsClassifier(n_neighbors=k)
        classifier.fit(X_train, y_train)
        
        # Predict
        y_train_pred = classifier.predict(X_train)
        y_test_pred = classifier.predict(X_test)
        
        # Train Performance
        score_train = accuracy_score(y_train, y_train_pred)
        acc_train.append(score_train)

        # Test Performance
        score_test = accuracy_score(y_test, y_test_pred)
        acc_test.append(score_test)

    result = pd.DataFrame({'k': ks, 'acc_train': acc_train, 'acc_test': acc_test})

    plt.figure(figsize=(12, 8))
    plt.title('KNN Performance')
    plt.ylabel('Accuracy')
    plt.xlabel('K')
    sns.lineplot(data=result, x='k', y='acc_train')
    sns.lineplot(data=result, x='k', y='acc_test')
    plt.grid()
    plt.xticks(result['k'])
    plt.show()

search_k(X_train, X_test, y_train, y_test, maximum_k=15)

"""We can say K = 6 or K = 11 is good

# Decision Tree
"""

dataset.head()

# Separate Training and Test set
X = dataset.iloc[:, :-1]
y = dataset.iloc[:, -1]

"""# Train Test Split"""

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

"""# Training Model"""

from sklearn.tree import DecisionTreeClassifier
dec_tree = DecisionTreeClassifier(criterion = 'entropy', random_state = 121, max_depth=5)
dec_tree.fit(X_train, y_train)

y_test_pred = dec_tree.predict(X_test)
accuracy_score(y_test, y_test_pred)

y_train_pred = dec_tree.predict(X_train)
accuracy_score(y_train, y_train_pred)

"""# Search Optimum Tree"""

def search_tree(X_train, X_test, y_train, y_test, max_depths):
    acc_train = []
    acc_test = []
    for depth in max_depths:
        # Train based on tree's depth
        classifier = DecisionTreeClassifier(criterion='entropy', random_state=121,
                                            max_depth=depth)
        classifier.fit(X_train, y_train)
        
        # Predict 
        y_train_pred = classifier.predict(X_train)
        y_test_pred = classifier.predict(X_test)
        
        # Train Performance
        score_train = accuracy_score(y_train, y_train_pred)
        acc_train.append(score_train)

        # Test Performance
        score_test = accuracy_score(y_test, y_test_pred)
        acc_test.append(score_test)

    result = pd.DataFrame({'depths': max_depths, 'acc_train': acc_train, 'acc_test': acc_test})

    plt.figure(figsize=(12, 8))
    plt.title('Decision Tree Performance')
    plt.ylabel('Accuracy')
    plt.xlabel('Max Depths')
    sns.lineplot(data=result, x='depths', y='acc_train')
    sns.lineplot(data=result, x='depths', y='acc_test')
    plt.grid()
    plt.xticks(result['depths'])
    plt.show()

search_tree(X_train, X_test, y_train, y_test, max_depths=[1,2,3,4,5,6,7,8,9])