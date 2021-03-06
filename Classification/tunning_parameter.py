# -*- coding: utf-8 -*-
"""tunning_parameter.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xuWtfWQ69OgLoQW9ik28vjZaPNb3OPJ_
"""

import time
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, StratifiedKFold, GridSearchCV
data=pd.read_csv('E:\MAGISTER\DATA\ANALISIS\POTONG DATA\EEG_dataset.csv', index_col=None)
y=data['label']
X=data.iloc[:,1:43]

"""Tunning for SVM kernel RBF"""

def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01,0.025, 0.1, 0.5, 1, 10, 10,100]
    param_grid = {'C': Cs}
    grid_search = GridSearchCV(svm.SVC(kernel='linear'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    grid_search.best_params_
    return grid_search.best_params_

start = time.time()
tunning=svc_param_selection(X, y, 10)
end = time.time()
print ("Waktu Tuning Paremeter kerne linier yaitu", end - start,"Second ")
print (tunning)

"""TUnning for SVM kernel RBF"""

from sklearn import svm
def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01,0.025, 0.1, 0.5, 1, 10, 10,100]
    gammas = [0.001, 0.01,0.025, 0.1, 0.5, 1, 10, 10,100]
    param_grid = {'C': Cs, 'gamma' : gammas}
    grid_search = GridSearchCV(svm.SVC(kernel='rbf'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    grid_search.best_params_
    return grid_search.best_params_

start = time.time()
tunning=svc_param_selection(X, y, 10)
end = time.time()
print ("Waktu Tuning Paremeter kerne linier yaitu", end - start,"Second ")
print (tunning)

"""Tunning for SVM kernel Poly"""

def svc_param_selection(X, y, nfolds):
    Cs = [0.001, 0.01,0.025, 0.1, 0.5, 1, 10, 10, 100]
    Degrees = [0, 1, 2, 3, 4, 5, 6]
    param_grid = {'C': Cs, 'degree' : Degrees }
    grid_search = GridSearchCV(svm.SVC(kernel='poly'), param_grid, cv=nfolds)
    grid_search.fit(X, y)
    grid_search.best_params_
    return grid_search.best_params_

start = time.time()
tunning=svc_param_selection(X, y, 10)
end = time.time()
print ("Waktu Tuning Paremeter kerne linier yaitu", end - start,"Second ")
print (tunning)