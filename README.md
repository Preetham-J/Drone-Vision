# Drone Vision
After assembling and testing my quad-copter camera drone (shown below), I'm currently looking into giving it the ability to autonomously
make basic decisions (ex. take-off, hover, land). Seeing as it has a camera on it, my ultimate goal with this project is to use a receiver
to input video data to my computer, interpret the data collected, and send out instructions through a transmitter.

## Drone:
![alt text](drone.jpg?raw=true "Drone")

## Current Stage
I am currently exploring computer vision by learning how to use OpenCV (computer vision library) on Python. As time goes on, I'll be adding any relevant tutorial projects here.

### Shape Detection
I've added a shape detection program that detects squares, rectangles, circles, and pentagons. This will be useful in the future to allow
the drone to recognize signs (ex. landing zone areas).

Image Inputted:
![alt text](/Shape_Detection/shapes.png?raw=true "Inputted Image")
Image Outputted:
![alt text](/Shape_Detection/detection.PNG?raw=true "Outputted Image")

## How to Use
To use all the files, make sure you have the following installed: OpenCV, Matplotlib, NumPy, SciPy and imutils.
