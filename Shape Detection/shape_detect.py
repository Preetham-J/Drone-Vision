# Import libraries
import cv2
import imutils
from shapeDetector import ShapeDetector
import argparse

# Construct and parse arguments
argumentParse = argparse.ArgumentParser()
argumentParse.add_argument("-i", "--image", required = True, help = "Path to input image")
args = vars(argumentParse.parse_args())

# Load image and resize to a smaller factor
image = cv2.imread(args["image"])
resizedImage = imutils.resize(image, width = 300)
ratio = image.shape[0] / float(resizedImage.shape[0])

# Convert resized image to grayscale, blur, threshold
grayImage = cv2.cvtColor(resizedImage, cv2.COLOR_BGR2GRAY)
blurredImage = cv2.GaussianBlur(grayImage, (5,5), 0)
thresholdImage = cv2.threshold(blurredImage, 60, 255, cv2.THRESH_BINARY)[1]

# Determine contours in thresholdImage and use ShapeDetector
contours = cv2.findContours(thresholdImage.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if imutils.is_cv2() else contours[1]
shapeDetect = ShapeDetector()

# Loop through contours
for i in range(len(contours)):
	for c in contours:
		# Calculate center of contour, detect shape name using contour
		middle = cv2.moments(c)
		# Get correct position of center based on ratio of resized image
		cX = int((middle["m10"] / middle["m00"]) * ratio)
		cY = int((middle["m01"] / middle["m00"]) * ratio)
		shape = shapeDetect.detect(c)

		# Get correct position of contours based on ratio of resized image
		c = c.astype("float")
		c *= ratio
		c = c.astype("int")
		cv2.drawContours(image, [c], -1, (0,255,0), 2)
		cv2.putText(image, shape, (cX, cY), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)

		# Display output image
		cv2.imshow("Image", image)
cv2.waitKey(0)


