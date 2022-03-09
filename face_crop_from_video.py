# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 21:45:45 2021

@author: Vitrail
"""

import cv2
import os
from matplotlib import pyplot as plt

# Setting up a capture
cap = cv2.VideoCapture(os.path.join('Benchmark-Videos', 'Benchmark_1.mp4'))

# Haarcascade for face detection
# The face recognition library can be replaced using other face recognition such as Ageitgey/face recognition, CompareFace, Deepface, etc., by modifying the coding.
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Working with video captures
# Loop through each frame
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    # Read frame
    ret, frame = cap.read()
    
    # Gray Transform
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    print("[INFO] Found {0} Faces!".format(len(faces)))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h),
				(0, 0, 255), 2)
        faces = frame[y:y + h, x:x + w]
        
    # Show image
    cv2.imshow('Video Player', frame)
    # write image cropped
    cv2.imwrite(str(w) + str(h) + '_faces.jpg', faces)
    
    # Breaking out of the loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# CLose down everything
cap.release()
cv2.destroyAllWindows()
