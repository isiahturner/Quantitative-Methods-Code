import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Importing the excel file using pandas
dogPlotData = pd.read_excel(
    r'C:\Users\Isiah Turner\OneDrive\Documents\Quantitative Methods Code\dog_treats.xlsx')
print(dogPlotData)

# * Splitting the data into groups based off of the breed of a dog
# * This creates a bucket for each dog breed containing the information for each one
# Grouping the data using one key
dogBreeds = dogPlotData.groupby("Breed")

# * After splitting a data into a group, we aply a function to each group.
# * The three operations are aggregation, transformation and filtration.
# * AGGREGATION: perform summary statistic on each group (i.e sum or means)
# * TRANSFORMATION: Perform group specific computations and return a like indexed list/dictionary
# * FILTRATION: Discard some groups according to a group-wise computation that evaluates True or False (Filter based on the group mean/sum)


# Aggregating the dog data by finding the mean and standard deviation for each breed's treats per day
# Aggregate takes in a single function or a list of functions (i.e [np.sum, np.mean])

dogTreats = dogBreeds['Treats_per_day'].agg([np.mean, np.std])
print(dogTreats)

# This is how we would go about it if we wanted to apply different functions to different columns
#dogTreats2 = dogBreeds.agg({'Treats_per_day' : 'mean'})
# print(dogTreats2)

print(dogTreats.columns)


fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(8, 4))
breedNames = list(dogTreats.index)
ax1.bar(breedNames, dogTreats['mean'])
ax1.set_xlabel('Breed')
ax1.set_ylabel('Mean')

ax2.bar(breedNames, dogTreats['std'])
ax2.set_xlabel('Breed Names')
ax2.set_ylabel('Standard Deviation')

# print(test.agg(np.mean))
#print(test["Treats_per_day"].agg([np.mean, np.std]))
#print(test.agg(np.mean, np.sum, np.std))
plt.show()
