# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 00:08:33 2021

@author: Vitrail
"""

import cv2
import os
from matplotlib import pyplot as plt

# Setting up a capture
cap = cv2.VideoCapture(os.path.join('Benchmark-Videos', 'Benchmark_1.mp4'))

# Grab a frame
ret, frame = cap.read()
plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
plt.show()

### Realease capture
cap.release()
cap.read()


# Capture Properties

# Height
cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
# Width
cap.get(cv2.CAP_PROP_FRAME_WIDTH)

# Get number of frames
cap.get(cv2.CAP_PROP_FRAME_COUNT)/15

# Framez per second
cap.get(cv2.CAP_PROP_FPS)
320/30


# Working with video captures

# Estabilish capture
cap = cv2.VideoCapture(os.path.join('Benchmark-Videos', 'Benchmark_1.mp4'))

# Loop through each frame
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    # Read frame
    ret, frame = cap.read()
    
    # Gray Transform
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    
    # Show image
    cv2.imshow('Video Player', frame)
    
    # Breaking out of the loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# CLose down everything
cap.release()
cv2.destroyAllWindows()
