# How to fit a straight line MANUALLY to data by minimizing the sum of squares error
from sklearn.linear_model import LinearRegression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Variables
x = list(range(1, 8))
y = [0.2474, 0.18532, 0.28638, 0.58132, 0.54259, 0.72938, 0.71378]


# Guessing the slope
slope = 0.1
intercept = 0.09
guess = [slope, intercept]

# Equation for a straight line
# y = (gradient * x) + intercept

# Creating line fit function


def calculateLine(xFit, slope, intercept):
    yFitList = []
    for xValue in xFit:
        yFit = (slope * xValue) + intercept
        yFitList.append(yFit)
    return yFitList

# Creating the fit erro rfunction


def calculateFitError(guess, x_data, y_data):
    # Returns least squares error
    guessSlope = guess[0]
    guessIntercept = guess[1]

    guessY = calculateLine(x_data, guessSlope, guessIntercept)

    # calculating sum of squares error
    amountOfError = 0
    counter = 0
    for value in guessY:
        amountOfError += (value - y_data[counter]) ** 2
        counter += 1

    # Plotting the error
    fig2, ax1 = plt.subplots()

    # First we want to plot the actual data
    ax1.plot(x_data, y_data, 'bo')

    # Next we plot our line of best fit, our expected values
    ax1.plot(x_data, guessY, 'r-')

    for item in range(len(x_data)):
        ax1.plot([x_data[item], x_data[item]], [
                 y_data[item], guessY[item]], 'm-')

    ax1.set_xlim(0, 8)
    return fig2, amountOfError


graph, error = calculateFitError(guess, x, y)

print(error)


### * This isn't realistic though, so need to get about it an easier way ###

# Import Modules

# Initializing variables
# .reshape turns the horizontal array into a vertical array
x2 = np.array(list(range(1, 8))).reshape((-1, 1))
y2 = np.array([0.2474, 0.18532, 0.28638, 0.58132, 0.54259, 0.72938, 0.71378])

# x2.shape
# print(x2)

# Create an instance of the Linear Regression class, this can have serveral option parameters.
# Such as fit_intercept, normalize, copy_X, n_jobs.
model = LinearRegression()

# Now we call the .fit() method on the model
model.fit(x2, y2)

# We combine these two approaches because the .fit() method returns self which would be the
# model itself
model = LinearRegression().fit(x2, y2)

# Getting our results for r-squared, slopes and intercepts
r_sq = model.score(x2, y2)
print('Coefficient of Determination: ', r_sq)
print('Slope: ', model.coef_)
print('Intercept: ', model.intercept_)

yGuess = model.predict(x2)
# print(model.predict(x2))

dataframe = pd.DataFrame({'Actual': y2, 'Predicted': yGuess})
print('Residual Sum of Squares: ' +
      str(np.sum(np.square(dataframe['Predicted'] - dataframe['Actual']))))
print('\n', dataframe)


# Plotting and visualizing our model
fig3, ax2 = plt.subplots()
ax2.scatter(x2, y2, color='black')
ax2.plot(x2, yGuess, color='blue', linewidth=3)
for item in range(len(x2)):
    ax2.plot([x2[item], x2[item]], [y2[item], yGuess[item]], 'm-')

plt.show()
