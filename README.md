# Drone Vision
After assembling and testing my quad-copter camera drone (shown below), I'm currently looking into using computer vision to analyze basic drone footage. Seeing as it has a camera on it, my ultimate goal with this project is to use a receiver to input video data to my computer and interpret the video collected. From there, detection information can be presented, or instructions can be sent out through a transmitter.

## Drone:
![alt text](drone.jpg?raw=true "Drone")

## Current Stage
I am currently exploring object detection using OpenCV's C++ library. The goal for this stage is to get my program to the point where drone footage can be inputted, and detection information can be presented to the user. 

### Shape Detection
As an introduction to OpenCV's Python library, I created a basic shape detection program that detects squares, rectangles, circles, and pentagons:

Image Inputted:
![alt text](/shape_detection/shapes.png?raw=true "Inputted Image")
Image Outputted:
![alt text](/shape_detection/detection.PNG?raw=true "Outputted Image")

## How to Use
To use all the files, make sure you have the following installed: OpenCV, Matplotlib, NumPy, SciPy and imutils.
