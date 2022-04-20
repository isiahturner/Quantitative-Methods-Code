###### Image Filtering using Convolution in OpenCV ######

# In image processing, a convolution kernel is a 2D matrix that is used to filter images. Typically
# a Rows x Columns matrix that are always odd integers (3x3, 5x5, 7x7). They perform mathematical
# operations on each pixel of an image toa desired effect. Why would you want to blur an image?
# Reason 1 is it reduces certain types of noise in an image, which is why blurring is often referred
# to as smoothing. Reason 2 is to remove a distracting background. Either way, convolution is a
# fundamental processing technique in Computer Vision.

# In OpenCV, we use apply an identity kernel. The identity kernel is a square matrix where the
# middle element is 1 and all of the other elements is 0. This is special because by multiplying any
# other matrix with the identity kernel, you will return the original matrix.

# Importing the modules
import numpy as np
import cv2

# Reading in the image
testImage = cv2.imread('kobePic.jpg')

# Creating our first identity kernel that shows it will leave the original image unchanged.
neutralKernel = np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])

# Performing a linear filtering operation using filter2D(src, ddepth, kernel). src is the image we are
# working with. ddepth is th edepth of the resulting image, a value of -1 indicates that the final
# image will also have the same depth as the source image. kernel is the kernel we apply to the source
# image.
identity = cv2.filter2D(src=testImage, ddepth=-1, kernel=neutralKernel)

# Displaying the original image and new image (should get the same image)
cv2.imshow('Original', testImage)
cv2.imshow('New', identity)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Creating a custom 2D-Convolution Kernel to blur an image. BEFORE APPLYING ANY CONVOLUTION TO AN IMAGE
# USING 2D CONVOLUTION, NORMALIZE THE VALUES BY DIVIDING EACH ELEMENT OF THE KERNEL BY THE NUMBER OF
# ELEMENTS IN THE KERNEL (In a 5x5 kernel, each element would need to be divided by 25). This ensures
# all values stay within the range of [0, 1]
blurKernel = np.ones((5, 5), np.float32) / 25

# Blurring the image
blurImage = cv2.filter2D(testImage, ddepth=-1, kernel=blurKernel)

# Displaying the two images for comparison
cv2.imshow('Original', testImage)
cv2.imshow('Blurred Image', blurImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# You can also blur with OpenCV's built-in blur function. Simply specify the kernel size, using the ksize
# input argument.
blurImage2 = cv2.blur(testImage, ksize=(5, 5))
blurImage3 = cv2.blur(testImage, ksize=(7, 7))

# Showing how the blur function changes the picture and how increasing ksize increases the blur
cv2.imshow('blur', blurImage2)
cv2.imshow('blur more', blurImage3)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Gaussian Blur to the images using GaussianBlur(src, ksize, sigmaX, dst, sigmaY, borderType).
# This technique uses a Gaussian filter, which performs a weighted average and weighs pixel values based
# on their distance from the center of the kernel. Pixels further from the center have less influence on
# the weighted average.
# src is the image we are working with, ksize is the size of the Gaussian kernel. sigmaX and sigmaY are
# the kernel standard deviations in the x (horizontal) and y (vertical) direction, the default is 0.

gaussianBlurImage = cv2.GaussianBlur(
    testImage, ksize=(5, 5), sigmaX=0, sigmaY=0)

cv2.imshow('Original', testImage)
cv2.imshow('Gaussian Blur', gaussianBlurImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying Median Blurring to an image using medianBlur(src, ksize). Each pixel in the source image is
# replaced by the median value of the image pixels in the kernel area. ksize in this function is a
# a single odd integer. Effect of median blurring is more prominent than Gaussian blurring, this
# method is often used to reduce 'salt and pepper' noise in images.
medianBlurring = cv2.medianBlur(testImage, ksize=5)

cv2.imshow('original', testImage)
cv2.imshow('median blur', medianBlurring)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sharpening an image with a custom 2D-Convolution Kernel and filter2D(). This kernel is a commonly
# used one.
sharpenKernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

sharpImage = cv2.filter2D(src=testImage, ddepth=-1, kernel=sharpenKernel)

cv2.imshow('Original', testImage)
cv2.imshow('Sharper Image', sharpImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Applying the Bilateral Filtering to an image bilateralFilter(src, d, sigmaColor, sigmaSpace). This
# method lets you blur images while sharp edges are preserved wherever possible. It also lets you
# control not only the spatial size of the filter but also the degreee to which the neighboring pixels
# are included in the filtered output. This is done, based on variation in their color intensity and
# distance from the filtered pixel. Regions of more uniform intensity are blurred heavier since they
# are not associated with strong edges.
# src is the image being worked with, d is the diameter of the pixel neighborhood used for filtering,
# sigmaColor defines the standard deviation of the 1D color-intensity distribution, sigmaSpace defines
# the 2D spatial distribution. sigmaSpace defines the spatial extent of the kernel in both x and y
# directions, similar to the Gaussian blur. sigmaColor defines the one-dimensional Gaussian distribution
# that specifies the degree to which differences in pixel intensity can be tolerated.
bilateralImage = cv2.bilateralFilter(
    src=testImage, d=9, sigmaColor=75, sigmaSpace=75)

cv2.imshow('original', testImage)
cv2.imshow('Bilateral Filter', bilateralImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
