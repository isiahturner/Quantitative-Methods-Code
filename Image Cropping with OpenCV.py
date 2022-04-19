###### Cropping an Image using OpenCV ######

# There isn't a specific cropping function but by using numpy array slicing we are able
# to crop. Every image that is read in gets stored in a 2D array for each color channel.
# So we just need to specify the height and width (in pixels) of the area to be cropped

# Import our modules
import cv2
import numpy as np

# Reading in our image
image = cv2.imread('kobePic.jpg')

# Print the dimensions of the image
height, width, channel = image.shape
print(f'The height is {height}')
print(f'The width is {width}')

# Slicing the image the same way numpy arrays are spliced. First dimension is height, second
# dimension is the width
croppedImage = image[48:360, 153:459]

# Showing our cropped image
cv2.imshow('Cropped', croppedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
