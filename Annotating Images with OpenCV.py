###### Annotating Images Using OpenCV ######

# Can use OpenCV to add information to your demos, drawing bounding boxes around objects in case of
# object detection

# Drawing a line on an image by using the line() function. Before we do that though we need to use
# the copy() function in python to ensure we do not affect the original image.
# line(image, start_point, end_point, color, thickness). image is the copied image we are working with
# start_point is a point (x1, y1) where the line starts. end_point is a point (x2, y2) where the line
# ends. The points are pixel locations. color is the color of the line we want to have. thickness is
# how thick we want the line.

# Importing our modules
import cv2

# Read in the original image
image = cv2.imread('kobePic.jpg')

# Copy the original image so we can annotate it
copiedImage = image.copy()

# Determinining the points we want to work with
height, width, channel = copiedImage.shape
print(height)
print(width)
pointA = (300, 0)
pointB = (300, height)

# Drawing the line on the copied image
cv2.line(copiedImage, pointA, pointB, (255, 255, 0), thickness=3)

# Visualizing our annotated image
cv2.imshow('Line Image', copiedImage)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Drawing a circle with circle(image, center_coordinates, radius, color, thickness).
# image is the copied image being worked with. center_coordinates is the location of the center
# of the circle. color and thickness are straightforward

# Copying the image
circleImage = image.copy()

# Setting circle variables
circleCenter = (306, 204)
radius = 100

# Drawing the circle, make thickness -1 if you want to fill the circle
cv2.circle(circleImage, circleCenter, radius,
           (0, 0, 255), thickness=3, lineType=cv2.LINE_AA)

# Displaying the result
cv2.imshow('circle picture', circleImage)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Draw rectangle with rectangle(image, start_point, end_point, color, thickness). start_point is the
# top left of the rectangle and end_point is the bottom right of the rectangle.

# Creating a copy of our image
imageRectangle = image.copy()

# Initializing the start points
startPoint = (300, 225)
endPoint = (475, 400)

# Drawing the rectangle on the copied image
cv2.rectangle(imageRectangle, startPoint, endPoint,
              (0, 255, 0), thickness=3, lineType=cv2.LINE_8)

# Displaying the result
cv2.imshow('Rectangle on Image', imageRectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Adding text to an image using putText(image, text, org, font, fontScale, color). The image is the
# copied image we are working with. text is the actual text string you want on the image. org is the
# starting location for the top corner of the text string. font is the font type you want to use,
# openCV has a list. fontScale is to scale the size of the text. color is a BGR triplet that is
# inputted as a tuple.

# Creating a copy of our image
textImage = image.copy()

# Initializing text and text location
text = 'The Greatest of All Time'
org = (0, 50)

# Placing the text on our copied image
cv2.putText(textImage, text, org, fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=0.75,
            color=(250, 225, 100))

# Display the image
cv2.imshow('Image Text', textImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
