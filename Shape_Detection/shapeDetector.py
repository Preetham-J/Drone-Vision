# Import libraries
import cv2

class ShapeDetector:
	def __init__(self):
		pass

	def detect(self, contour):
		# Initialize shape name, approximate the contour of shape
		shape = "Unidentified"
		perimeter = cv2.arcLength(contour, True)
		approximation = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

		# Triangle detection for 3 vertices
		if len(approximation) == 3:
			shape = "Caution"

		# Square/rectangle detection for 4 vertices
		elif len(approximation) == 4:
			# Get the bounding box of the contour
			(x, y, w, h) = cv2.boundingRect(approximation)
			# Use bounding box to calculate aspect ratio
			aspectRatio = w/float(h)
			# If the aspect ratio ~ 1, detect square (Landing); else, detect rectangle ()
			shape = "Increase Altitude" if aspectRatio >= 0.95 and aspectRatio <= 1.05 else "Reduce Altitude"

		# Pentagon detection for 5 vertices (stop)
		elif len(approximation) == 5:
			shape = "Stop"

		# SHAPE CAP AT 5 VERTICES
		# Circle detection for > 5 vertices (slow approach)
		else:
			shape = "Landing Zone"

		# Return shape name
		return shape

