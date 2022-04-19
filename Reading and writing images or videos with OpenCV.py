####### WORKING ON USING OPENCV ########

# Importing modules
import cv2

# Reading in an image with imread(filename, flags). The filename
# needs to be the filepath of the image we are working with. Flags
# tells opencv how to read in the image. -1 is for unchanged, 0 is
# for grayscale, and 1 is for color. Opencv READS IN AS BGR FORMAT
# INSTEAD OF RGB FORMAT SO KEEP THAT IN MIND WHEN USING OTHER TOOLKITS.

coloredImage = cv2.imread('kobePic.jpg', 1)
unchangedImage = cv2.imread('kobePic.jpg', -1)
greyImage = cv2.imread('kobePic.jpg', 0)

# Displaying images with imshow(window_name, image). Window name is the name
# used for the new window. The image argument is whatever image you want
# displayed on the window. This function is designed to be used with the
# waitKey() and destroyAllWindows() functions. waitKey takes in an input for
# how long the display should be open in milliseconds unless 0 is passed which
# keeps the windows displayed indefinitely. Can be set to specific keystrokes as well.
# destroyAllWindows() then closes everything off.

cv2.imshow('Colored Image', coloredImage)
cv2.imshow('Unchanged Image', unchangedImage)
cv2.imshow('Grey Image', greyImage)

cv2.waitKey(10)
cv2.destroyAllWindows()


# Writing an image using imwrite(filename, image). filename argument is whatever you want
# the new image to be named. The image argument is the specific image you want to be saved

cv2.imwrite('Grey Kobe.jpg', greyImage)

# Reading in a video file with VideoCapture(path, apiPreference). The path argument is the
# filename/path to the video file. The seocn is apiPreference which will be discussed later.
vid_capture = cv2.VideoCapture('Vince Dunk.mp4')

# Checking whether the video file was opened correctly by using the isOpened() function. This
# function returns True or False depending on whether the video was opened successfully.
if vid_capture.isOpened() == False:
    print('Error opening')
else:
    print('Success')

# Using the get() method to get the frame rate and the frame count for the video. This method
# takes in one argument from an enumerated list. This is gathered from the metadata
if vid_capture.isOpened() == False:
    print('Error Opening')
else:
    # Getting the frame rate
    fps = int(vid_capture.get(5))
    print(f'Frame Rate: {fps} frames per second')

    # Getting the frame count
    frameCount = int(vid_capture.get(7))
    print(f'Frame Count: {frameCount}')

# After we have gathered our metadata for the associated video files, we are ready to read each
# image frame from the file. We do this by creating a loop and reading one frame at a time from
# the video stream. The output for .read() is a tuple containing a boolean and the video frame.
# When the first element is true, it indicates the video stream contains a frame to read.
# If there is a frame to read, we can use the imshow() function again.

# Creating the loop using a while loop
while vid_capture.isOpened():
    # Unpacking the tuple containing the boolean and frame data if there is a frame
    ret, frame = vid_capture.read()
    # Checking if there is a frame present, if so displaying that frame
    if ret == True:
        cv2.imshow('Frame', frame)

        # Having it wait 20 milliseconds before going to the next frame, but if q is pressed
        # (the ascii for q is 113) then we stop going frame by frame
        k = cv2.waitKey(1)
        if k == 113:
            break
    else:
        break

# Once we fully process the video or the user breaks out of the video, we release the video capture
# object and close the window.

vid_capture.release()
cv2.destroyAllWindows()

# We can also process image sequences similar to how we process videos. We still use video capture
# objects but instead of specifying a video file you specify an image sequence. Using the notation
# 'Cars%04d' we grab all of the files with a 4-digit naming sequence (Cars0001.jpg, Cars0002.jpg,
#  Cars0003.jpg)
# vid_capture = cv2.VideoCapture('Cars%04d.jpg)

# OpenCV can also write videos as well. To write a file you need to:
# 1: Retrive the image frame height and width by using the get() method
# 2: Initialize a video capture object to read the video stream into memory
# 3: Create a video writer object
# 4: Use the video writer object to save the video stream to disk

# Creating the video capture object
vid_capture = cv2.VideoCapture('Vince Dunk.mp4')

# So let's first obtain the frame size information
frameWidth = int(vid_capture.get(3))
frameHeight = int(vid_capture.get(4))
frameSize = (frameWidth, frameHeight)
framesPerSecond = 120

# We now need to create a video-writer object from the VideoWriter class in order to write a video file.
# VideoWriter class takes the following argmuments: filename, apiPreference, fourcc, fps, frame_size and
# isColor. filename is the path name for the file. fourcc is a 4-character code to compress the frames.
# fps is the frame rate of the created object. frame_size is the size of the video frames.
# If not zero, the encoder will expect and encode color frames. Else it will work with grayscale frames
# (the flag is currently supported on Windows only).

# Initialize the VideoWriter object
output = cv2.VideoWriter('outputtedFile.mp4', cv2.VideoWriter_fourcc(
    *'XVID'), framesPerSecond, frameSize)

# Now that the VideoWriter is created, need to write the video file to a disk at 20 frames per second.
while vid_capture.isOpened():
    ret, frame = vid_capture.read()
    if ret == True:
        output.write(frame)
    else:
        print('Stream Disconnected')
        break

# Release the objects again
vid_capture.release()
output.release()

# Takes my computer roughly 2 minutes, is going through reading and writing a lot of data. Original video
# was roughly 3145 rames at 60 fps, so about 52 seconds long
