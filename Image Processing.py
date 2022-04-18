### Image Processing Basics ###

# * What is bit-depth?

# Bit-depth is the number of binary digits for each color. 8 bit means numbers can range
# from 0 to 2^8 which = 255. 16 bit means number can range from 0 to 2^16 = 65, 536. More
# bits means more potential colors but requires more memory. So 1 bit would be black and
# white.

# * Rules about bit levels

# 1: You only have the information you collected in the original picutre
# 2: Converting to higher bit level uses more memory and takes more time
# but doesn't give you extra anything.
# 3: Converting to a lower bit level throws away information

# * Compression

# Storing the picture is less memory than a straight pixel by pixel description.
# Lossless compression is when you store the same information, which is our .png.
# Lossy compression is when we store a variant and can't go back to the original,
# this generally takes less memory.

# * Bitmap vs Vector-based Images

# Bitmaps CAN'T be scalable while vector-based images can.
# Vector-based images describes a picture using 'geometrical primitives' like
# curves, lines and polygons.
# Vector-based is also interchangeable.

# So for example, when zooming in on an image, the vector-based image will allow a
# clear zoom in while the bitmap image would become pixelated.

# * Vector Formats

# Vector-based: .eps, .ai, .svg, .emf, .pdf, .pict
# Lossless Bitmap: .tif, .png, .bmp, .psd
# Lossy Bitmap: .jpg, .gif

# Importing the Pillow image processing module and other necessary modules
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageEnhance

# Opening the image file, in this case a jpg
kobeImage = Image.open(
    'C:\\Users\\Isiah Turner\\OneDrive\\Documents\\Quantitative Methods Code\\kobePic.jpg')

# Visualizing and assigning the image sizes
print(kobeImage.size)
w, h = kobeImage.size

# Resizing the image to be half the size
kobeImage = kobeImage.resize((int(w * 0.5), int(h * 0.5)))

# Showing the changed image
kobeImage.show()

# Saving the image
kobeImage.save('newKobePic.png')

#######################################################

# Importing modules

# Variables
numPopulation = 1000000
numSample = 10

# Creating the data for the code
s = np.random.normal(loc=120, scale=20, size=numPopulation)
plt.hist(s, bins=240, range=(50, 190))
plt.ylabel('Number of People')
plt.xlabel('Systolic Blood Pressure')
plt.savefig('Plot Example.png')

# Opening the image we want to resize
originalImage = Image.open(
    r'C:\Users\Isiah Turner\OneDrive\Documents\Quantitative Methods Code\Plot Example.png')

# Assigning the sizes to variables
w2, h2 = originalImage.size

# Resizing the image
originalImage = originalImage.resize((int(w2 * 1.5), int(h2 * 1.5)))

# Adding brightness to the image
enhancer = ImageEnhance.Brightness(originalImage)
brightenedImage = enhancer.enhance(1.5)


# Showing and then saving the image
brightenedImage.show()
brightenedImage.save('Updated Image.png')
