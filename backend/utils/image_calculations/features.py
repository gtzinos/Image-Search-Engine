import cv2
import imutils
import numpy as np

def get_features(imageDirectory):
    image=cv2.imread(imageDirectory)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # check to see if we are using OpenCV 3.X
    if imutils.is_cv3():
        # detect and extract features from the image
        descriptor = cv2.xfeatures2d.SIFT_create()
        (kps, features) = descriptor.detectAndCompute(gray, None)

    # otherwise, we are using OpenCV 2.4.X
    else:
        # detect keypoints in the image
        detector = cv2.FeatureDetector_create("SIFT")
        kps = detector.detect(gray)

        # extract features from the image
        extractor = cv2.DescriptorExtractor_create("SIFT")
        (kps, features) = extractor.compute(gray, kps)

    # convert the keypoints from KeyPoint objects to NumPy
    # arrays
    kps = np.float32([kp.pt for kp in kps])

    # return a tuple of keypoints and features
    return (kps, features)

def cut_dimensions(dim_array):
    counter = 0
    sum = 0
    mean = []
    
    #Calculate mean
    for index, row in enumerate(dim_array): 
        for number in row:
            sum += number
            counter += 1
              
        mean.append([index, sum / counter])
    
    #Sort values
    mean.sort(key=lambda x: x[1], reverse=True)

    #Get mean length
    mean_length = len(mean)

    mean = mean[0:mean_length]

    mean = [index for index, number in enumerate(mean)]

    return np.delete(dim_array, mean)
    #dim_array = result = [number for index, number in enumerate(dim_array) if index in mean]

    #return dim_array