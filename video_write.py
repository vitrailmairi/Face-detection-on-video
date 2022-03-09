# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 00:55:39 2021

@author: Vitrail
"""

import cv2
import os
from matplotlib import pyplot as plt

# Working with video captures

# Estabilish capture
cap = cv2.VideoCapture(os.path.join('Benchmark-Videos', 'Benchmark_1.mp4'))

# Propeties
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = cap.get(cv2.CAP_PROP_FPS)
# Video Writer
# CV_FOURCC('P','I','M,'1') // this is an MPEG1 codec from the characters to integer (https://www.fourcc.org/codecs.php)
video_writer = cv2.VideoWriter(os.path.join('Benchmark-Videos', 'Benchmark_output.avi'),
                               cv2.VideoWriter_fourcc('P', 'I', 'M', '1'), fps, (width, height))

# Loop through each frame
for frame_idx in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    # Read frame
    ret, frame = cap.read()
    
    # Gray Transform
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Show image
    cv2.imshow('Video Player', frame)
    # Write out frame
    video_writer.write(frame)
    
    # Breaking out of the loop
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# CLose down everything
cap.release()
cv2.destroyAllWindows()
# Release Video Writer
video_writer.release()