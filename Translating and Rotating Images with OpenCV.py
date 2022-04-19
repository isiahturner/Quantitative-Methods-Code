###### Image Rotation and Translation Using OpenCV ######
# Rotation and translation of images are among the most basic operations in image editing.
# Both of these fall under the broader class of AFFINE transformations.

# We can perform image rotation by using getRotationMatrix2D(center, angle, scale). center
# is the center of ration for the input image. angle is the angle of rotation in degrees.
# scale is an isotropic scale factor which scales the image up or down. If the angle is
# positive, the image gets rotated counter-clockwise. This function sets up our transformation
# matrix.

# Rotation is a 3-step operation. First, need to get the center of rotation which is typically
# the middle of the image. Next, create the 2D-rotation matrix by using the getRotationMatrix2D()
# function. Finally, apply the affine transformation to the image using the rotation matrix created
# in step 2, do this by using the warpAffine() function.

# We apply the affine transformation for the image using warpAffine(src, M, dsize, flags, borderMode,
# borderValue). src is the source image. M is the transformation matrix. dsize is the size of the
# output image. dst is the output image. flags is the comination of interpolation methods such as
# INTER_LINEAR or INTER_NEAREST. borderMode is the pixel extrapolation method. borderValue is the
# value to be used in case of a constant border, has a default value of 0.

# Importing the modules
import cv2
import numpy as np

# Reading in the image
image = cv2.imread('kobePic.jpg')

# Getting the height and width of the image, then finding the center of the image. So we are calculating
# the rotation point, aka the center of the image.
height, width, channel = image.shape
center = (width/2, height/2)

# Now based off the center of the image we just calculated, we compute a rotation matrix. Angle needs to
# be in degrees
rotationMatrix = cv2.getRotationMatrix2D(center=center, angle=45, scale=1)

# Now applying the rotation matrix to the image itself
rotatedImage = cv2.warpAffine(
    src=image, M=rotationMatrix, dsize=(width, height))

# Visualizing the original and rotated image
cv2.imshow('Original', image)
cv2.imshow('Rotated Image', rotatedImage)

# Wait indefinitely and close windows when key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()

# Translation of Images. So we are shifting by a specified number of pixels along the x and y axis.
# Positive values will shift to the right, negative values to the left for tx (translation in x).
# Positive will shift the image down and negative will shift the image up for ty. Have to manually
# create a translation matrix.

# We already have the height and width of the photo. Now we need our translation values
translationX = width / 4
translationY = height / 4

# Creating the translation matrix using translationX and translationY
translationMatrix = np.array(
    [[1, 0, translationX], [0, 1, translationY]], dtype=np.float32)

# Now again, applying the affine transformation to the image, which is translation in this case
translatedImage = cv2.warpAffine(
    src=image, M=translationMatrix, dsize=(width, height))

# Displaying the transformation
cv2.imshow('Original Image', image)
cv2.imshow('Translated Image', translatedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
