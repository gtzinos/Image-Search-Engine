import cv2

def get_features(imageDirectory):
       img=cv2.imread(imageDirectory)
       histogram=cv2.calcHist([img],[0,1,2],None,  [8,8,8],,256,0,256,0,256])
       Nhistogram=cv2.normalize(histogram)
       return Nhistogram.flatten()