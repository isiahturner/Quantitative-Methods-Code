######### Resizing an Image ##########

# When resizing an image, it is important to keep in mind the original height and weight if you want
# to maintain the same in the resized image. Reducing the size of an image will require resampling
# of the pixels. Increasing the size of an image requires reconstruction of the image, so you will
# need to interpolate new pixels

# Importing our modules
import cv2
import numpy as np

# First we are going to make an image larger and smaller by resizing with custom height and width

# Read the image
manualImage = cv2.imread('kobePic.jpg')

# Obtaining the size dimensions using the shape() function. It returns the height, width and number of
# channels of the image. Can also use the size() function (image.size().width for example)
imageHeight, imageWidth, imageChannels = manualImage.shape
print(f'Original Height and Width: {imageHeight} x {imageWidth}')

# Officially resizing the image with the OpenCV resize() function. Requires two arguments: First the source image
# and then the desired size of the resized image (dsize). cv2.resize(src, dsize, fx, fy, interpolation). src
# is the required input image as a string with the path of the input image. dsize is the desired size of
# the output image, it can be a new height and width. fx is the scale factor along the horizontal axis. fy is
# the scale factor along the vertical axis. Interpolation is the option of different methods of resizing
# the image.

# Creating the variables to manually set the width and height for downsizing and upsizing.
downWidth = 300
downHeight = 200
downPoints = (downWidth, downHeight)

upWidth = 600
upHeight = 400
upPoints = (upWidth, upHeight)

# Creating our resized images
resizeUp = cv2.resize(manualImage, upPoints, interpolation=cv2.INTER_LINEAR)
resizeDown = cv2.resize(manualImage, downPoints,
                        interpolation=cv2.INTER_LINEAR)

# Displaying each of our newly created images
cv2.imshow('Sized Down Video', resizeDown)
cv2.waitKey()
cv2.imshow('Sized Up Image', resizeUp)
cv2.waitKey()
cv2.destroyAllWindows()

# Resizing with a scalar factor. Used to multiply or scale some quantity and helps keep the aspect
# ratio intact for the image, this avoids distortion.

# Creating the scaling variables
scaleUpWidth = 1.2
scaleUpHeight = 1.2

scaleDown = 0.6

# Creating our scaled images
scaledDown = cv2.resize(manualImage, None, fx=scaleDown,
                        fy=scaleDown, interpolation=cv2.INTER_LINEAR)
scaledUp = cv2.resize(manualImage, None, fx=scaleUpWidth,
                      fy=scaleUpHeight, interpolation=cv2.INTER_LINEAR)

# Displaying the newly scaled images
cv2.imshow('Scale Up', scaledUp)
cv2.waitKey()
cv2.imshow('ScaleDown', scaledDown)
cv2.waitKey()
cv2.destroyAllWindows()

# Resizing with Different Interpolation Methods for different resizing purposes

# cv2.INTER_AREA: It uses pixel area relation for resampling. This is best suited for reducing the size
# of an image (shrinking).

# cv2.INTER_CUBIC: This uses cubic interpolation for resizing the image. While resizing and interpolating
# new pixels, this method acts on the 4x4 neighboring pixels to get the weight average for the
# interpolated pixel

# cv2.INTER_LINEAR: This method is somewhat linear to the INTER_CUBIC interpolation. But unlike
# INTER_CUBIC, this uses a 2x2 neighboring pixels to get the weighted average for the
# interpolated pixels

# cv2.INTER_NEAREST: This method uses the neighbor concept for interpolation. This is one of the simplest
# methods, using only one neighboring pixel from the image for interpolation. Used for zooming into the
# image.

# Scaling down using different concatenation methods
inter_nearest = cv2.resize(
    manualImage, None, fx=scaleDown, fy=scaleDown, interpolation=cv2.INTER_NEAREST)
inter_linear = cv2.resize(manualImage, None, fx=scaleDown,
                          fy=scaleDown, interpolation=cv2.INTER_LINEAR)
inter_area = cv2.resize(manualImage, None, fx=scaleDown,
                        fy=scaleDown, interpolation=cv2.INTER_AREA)

# Concatenating images in the horizontal axis for comparison. Use numpy because the arrays can store any kind
# of information.
imagesCombined = np.concatenate(
    (inter_nearest, inter_linear, inter_area), axis=0)
cv2.imshow('Inter Nearest :: Inter Linear :: Inter Area', imagesCombined)
cv2.waitKey()
cv2.destroyAllWindows()
