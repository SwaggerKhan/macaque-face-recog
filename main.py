import cv2
import sys
import os
import numpy as np
from scipy import ndimage
from time import time
import matplotlib.pyplot as plt
import utils as ut
import svm
import logging
import warnings

FACE_DIM = (50,50)
# Load training data from face_profiles/
face_profile_data, face_profile_name_index, face_profile_names  = ut.load_training_data("../face_profiles/")

print ("\n", face_profile_name_index.shape[0], " samples from ", len(face_profile_names), " Monkeys(Classes) are loaded")

# Build the classifier
clf, pca = svm.build_SVC(face_profile_data, face_profile_name_index, FACE_DIM)

SCALE_FACTOR = 4
imagePath = sys.argv[1]
cascPath = "./MacaqueFrontalFaceModel.xml"

# Create the haar cascade
faceCascade = cv2.cv2.CascadeClassifier(cascPath)

# Read the image
image = cv2.cv2.imread(imagePath)
gray = cv2.cv2.cvtColor(image, cv2.cv2.COLOR_BGR2GRAY)

sep = '/'
new_name_to_display = "Monkey " + imagePath.split(sep, 3)[2]

frame = cv2.cv2.imread(imagePath)
frame_scale = int((frame.shape[1]/SCALE_FACTOR) / 2), int((frame.shape[0]/SCALE_FACTOR) / 2)
gray = cv2.cv2.cvtColor(frame, cv2.cv2.COLOR_BGR2GRAY)

resized_frame = cv2.cv2.resize(frame, frame_scale)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.15,
    minNeighbors=5,
    minSize=(50, 50)
    #flags = cv2.CV_HAAR_SCALE_IMAGE
)

#print("Found {0} faces!".format(len(faces)))

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    face_to_predict = cv2.cv2.resize(resized_frame, FACE_DIM, interpolation = cv2.cv2.INTER_AREA)
    face_to_predict = cv2.cv2.cvtColor(face_to_predict, cv2.cv2.COLOR_BGR2GRAY)
    name_to_display = svm.predict(clf, pca, face_to_predict, face_profile_names)
    cv2.cv2.rectangle(image, (x, y), (x+w, y+h), (23, 112, 19), 6)
    name_to_display.flatten()
    #print(name_to_display)
    imagePath = sys.argv[1]
    
    cv2.cv2.putText(image, new_name_to_display, (x,y), cv2.cv2.FONT_HERSHEY_SIMPLEX, 5.0, (0,255,0), 3)

image = cv2.cv2.resize(image, frame_scale)
cv2.cv2.imshow("Faces found", image)
k = cv2.cv2.waitKey(0)