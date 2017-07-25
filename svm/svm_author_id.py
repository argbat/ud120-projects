#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###

from sklearn import svm
from sklearn.metrics import accuracy_score

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

clfSVMLinear = svm.SVC(C=10000, kernel='rbf')

t0 = time()
clfSVMLinear.fit(features_train, labels_train)
print "training time ", round(time() - t0, 3), "s"

t0 = time()
pred = clfSVMLinear.predict(features_test)
print "prediction time ", round(time() - t0, 3), "s"

acc = accuracy_score(labels_test, pred)
print "Accuracy ", acc

print "Predictions ", pred[10], " ", pred[26], " ", pred[50]
print "Class 1 in predictor ", reduce(lambda accum, pred_value: accum + (1 if pred_value == 1 else 0), pred, 0)

#########################################################


