
import cv2
import os
import numpy as np
from scipy import ndimage
from time import time
import warnings

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    from sklearn.model_selection import train_test_split

from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA as RandomizedPCA
from sklearn.svm import SVC

import utils as ut

#pca = RandomizedPCA(n_components=n_components, svd_solver='randomized', whiten=True).fit(X_train)

def test_SVM(face_profile_data, face_profile_name_index, face_dim, face_profile_names):
    
    X = face_profile_data
    y = face_profile_name_index

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    n_components = 45 # maximum number of components to keep

    print("\nExtracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))

    pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)

    print("\nProjecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test) 

    # Train a SVM classification model

    print("\nFitting the classifier to the training set")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }

    clf = SVC(C=1000.0, cache_size=200, class_weight='balanced',
  decision_function_shape=None, degree=3,  kernel='rbf',
  max_iter=-1, probability=True, random_state=None, shrinking=True, verbose=False)

    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(X_train_pca, y_train)

    print("\nPredicting people's names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("\nPrediction took %0.8f second per sample on average" % ((time() - t0)/y_pred.shape[0]*1.0))

    error_rate = errorRate(y_pred, y_test)
    print ("\nTest Error Rate: %0.4f %%" % (error_rate * 100))
    print ("Test Recognition Rate: %0.4f %%" % ((1.0 - error_rate) * 100))

    return clf, pca


def build_SVC(face_profile_data, face_profile_name_index, face_dim):

    X = face_profile_data
    y = face_profile_name_index

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

    n_components = 45 # maximum number of components to keep

    print("\nExtracting the top %d eigenfaces from %d faces" % (n_components, X_train.shape[0]))

    pca = RandomizedPCA(n_components=n_components, whiten=True).fit(X_train)
    #eigenfaces = pca.components_.reshape((n_components, face_dim[0], face_dim[1]))

    print("\nProjecting the input data on the eigenfaces orthonormal basis")
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test) 

    # Train a SVM classification model
    print("\nFitting the classifier to the training set")
    #param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5], 'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }

    clf = SVC(C=1000.0, cache_size=200,
  decision_function_shape=None, degree=3,  kernel='rbf',
  max_iter=-1, probability=True, random_state=24, shrinking=True, verbose=False)


    clf = clf.fit(X_train_pca, y_train)

    print("\nPredicting Rhesus Macaque names on the test set")
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("\nPrediction took %s per sample on average" % ((time() - t0)/y_pred.shape[0]*1.0))

    # print "predicated names: ", y_pred
    # print "actual names: ", y_test
    error_rate = errorRate(y_pred, y_test)
    print ("\nTest Error Rate: %0.4f %%" % (error_rate * 100))
    print ("Test Recognition Rate: %0.4f %%" % ((1.0 - error_rate) * 100))

    return clf, pca


def predict(clf, pca, img, face_profile_names):

    img = img.reshape(-1, 1)
    principle_components = pca.transform(img)
    pred = clf.predict(principle_components)
    #name = face_profile_names[pred]
    #print(pred)
    name = np.array(face_profile_names)[pred]
    #print(name)
    return name

def errorRate(pred, actual):
    
    if pred.shape != actual.shape: return None
    error_rate = np.count_nonzero(pred - actual)/float(pred.shape[0])
    return error_rate


