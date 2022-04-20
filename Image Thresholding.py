###### Image Thresholding ######

# Thresholding has numerous applications in computer vision and is often performed in the intial
# stages in many processing pipelines.

# First going to work on global thresholding, which is when the thresholding rule is applied equally
# to every pixel in the image, and the threshold value is fixed. Hence the 'global' thresholding.
# The simplest form of global threshold is called Binary Thresholding which takes in a source image,
# threshold value and the maximum value. At each pixel location (x, y). If the pixel is greater than
# the threshold then it will set the value of the destination image pixel (outputted image) to the
# maximum value that was given. Otherwise, it is set to 0.

# Importing in the modules
import cv2

# Read in our image, transform into a grey scale image (so white, variations of grey and black colors)
originalImage = cv2.imread('thresholdPic.png', cv2.IMREAD_GRAYSCALE)

# Setting our threshold and maximum value
thresh = 0
thresh2 = 127
maxValue = 255
maxValue2 = 128
maxValueBinary = 0

# Creating a basic threshold example of 0. th is the threshold value, dst is the outputted image.
th, binary0 = cv2.threshold(originalImage, thresh, maxValue, cv2.THRESH_BINARY)

# Displaying the threshold image to compare to the original, want to show effect of this threshold
cv2.imshow('Original', originalImage)
cv2.imshow('Binary Threshold', binary0)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a basic threshold example of 127.
th, binary127 = cv2.threshold(
    originalImage, thresh2, maxValue, cv2.THRESH_BINARY)

# Displaying the threshold image to compare to the original, want to show effect of this threshold
cv2.imshow('Original', originalImage)
cv2.imshow('Binary Threshold', binary127)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a basic threshold example but changing maxValue
th, binaryMaxDiff = cv2.threshold(
    originalImage, thresh, maxValue2, cv2.THRESH_BINARY)

# Displaying the threshold image to compare to the original, want to show effect of this threshold
cv2.imshow('Original', originalImage)
cv2.imshow('Binary Threshold', binaryMaxDiff)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Creating a Inverse-Binary Thresholded image. If the corresponding source pixel is greater than the
# threshold, then the destination pixel is set to 0. If the source pixel is less than the threshold,
# then the destination pixel is set to the maxValue.
thresh = 199
maxValue = 255
th, inverseBinary127 = cv2.threshold(
    originalImage, thresh, maxValue, cv2.THRESH_BINARY_INV)

# Displaying the threshold image to compare to the original, want to show effect of this threshold.
# In this case, if the pixel is greater than the threshold then the pixel is turned black but if it
# is less then it will turn the pixel white. Since the background is all black (0) which is less than
# the threshold (199) then the background turns white.
cv2.imshow('Original', originalImage)
cv2.imshow('Inverse Binary Threshold', inverseBinary127)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a Truncate Thresholded image. The destination pixel is set to the threshold if the source
# pixel value is greater than the threshold. Otherwise, it is set to the pixel value. maxValue is
# ignored.
thresh = 127
th, truncatedImage = cv2.threshold(
    originalImage, thresh, maxValue, cv2.THRESH_TRUNC)

# Displaying the threshold image to compare to the original image. In this case, all values above 127
# will be set to our threshold of 127. If the source pixel is less than the threshold, then those pixel
# values will remain unchanged.
cv2.imshow('Original', originalImage)
cv2.imshow('Truncate Threshold', truncatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a Threshold to zero image. If the source pixel value is greater than the threshold,
# the destination pixel value is set to the pixel value of the corresponding source. Otherwise, the
# destination pixel is set to 0. The maxValue is again ignored.
thresh = 127
th, thresholdZeroImage = cv2.threshold(
    originalImage, thresh, maxValue, cv2.THRESH_TOZERO)

# Displaying the threshold image to compare to the original image. In this case, if the source pixel
# is greater than 127, then we will keep the source pixel the same value when placed in the destination
# image. If the source pixel is not greater then we get rid of it by turning it black (0).
cv2.imshow('Original', originalImage)
cv2.imshow('Threshold to Zero', thresholdZeroImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating an Inverted Threshold to Zero image. If the source pixel is greater than the threshold, then the
# destination pixel is set to zero (black). Otherwise, the destination pixel is set to the source pixel.
# maxValue is ignored again.
thresh = 127
th, thresholdZeroImageInverse = cv2.threshold(
    originalImage, thresh, maxValue, cv2.THRESH_TOZERO_INV)

# Displaying the threshold image to compare to the original image. In this case, if the source pixel
# is greater than 127, then we get rid of it by turning it black (0). If the source pixel is not greater than
# the threshold, we will keep the source pixel value and set it to the destination pixel value. Values at the
# threshold's boundaries will create artifacts (aka the outlines in this case).
cv2.imshow('Original', originalImage)
cv2.imshow('Threshold to Zero', thresholdZeroImageInverse)
cv2.waitKey(0)
cv2.destroyAllWindows()
