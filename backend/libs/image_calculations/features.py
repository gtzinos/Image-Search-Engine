import cv2
import imutils

def get_features(imageDirectory):
    image=cv2.imread(imageDirectory)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    histogram = cv2.calcHist([hsv], [0, 1, 2], None, (8,8,8),
		[0, 180, 0, 256, 0, 256])

    # handle normalizing the histogram if we are using OpenCV 2.4.X
    if imutils.is_cv2():
        histogram = cv2.normalize(histogram)
    # otherwise, perform "in place" normalization in OpenCV 3 (I
    # personally hate the way this is done
    else:
        cv2.normalize(histogram, histogram)

    return histogram.flatten()