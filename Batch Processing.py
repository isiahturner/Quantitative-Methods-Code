# Importing modules that are needed throughout the script
import pandas as pd
from pathlib import Path
import os

# Defining function that filters through the last names of the excel files and
# pulls the ones that have the letter you are searching for


def lastNameTracker(series, desiredLetter):
    # The function takes in a pandas dataframe series and iterates throught the series to create a list of
    # people with the last name starting with the letter you want to search for. Series is inputted as a pandas
    # series and desiredLetter is inputted as a string. It will also return a count of how many people are
    # in the list with that name.

    # Creating an empty list to store the series that are selected
    nameList = []
    count = 0

    # Iterating through the pandas series of names and checking whether the name starts with the letter
    # you want to keep track of. The names that return true will be appended to the list. The list
    # will be a list of lists essentially, the second list is the pandas series that contains the
    # information for that subject's row.
    for name in series:
        if name[0] == desiredLetter.upper():
            nameList.append(patientInfo.iloc[count][:])

        count += 1

    nameCount = len(nameList)

    return nameList, nameCount


# Retrieving the working directory that is going to be looped through
cwd = os.getcwd()

# Setting the directory to the current working directory so the file name can be concatenated
# to open each file individually
directory = os.getcwd()

# Creating a generator object that contains all of the excel files in the directory
# Asterisks is a wild card, so is saying take any file name that has .blahblah
# Could do sub wildcards i.e baseball.xlsx
files = Path(directory).glob('*.xlsx')

# Creating an empty list to append the results for each file, each part of list
# will be a data series
filesToCombine = []

# Looping through the generator object and interact with each file
for file in files:
    # Print out file to make sure you are interacting with the correct file
    print(file)

    # Reads in the excel file as a dataframe
    patientInfo = pd.read_excel(r'{filename}'.format(filename=file))

    # Takes the imported dataframe and isolates the last names into a data series
    lastNames = patientInfo.iloc[:]['LastName']

    # Using the function that filters the last name based on the letter you want
    lastNameA, nameCountA = lastNameTracker(lastNames, 'a')

    # Convert the list of filtered names into a data series
    listToDataframe = pd.DataFrame(lastNameA)

    # Add the new data series to the list
    filesToCombine.append(listToDataframe)

# Compile the list of data series into one final dataframe containing the filtered name for all
# files in the directory
finalDataframe = pd.concat(filesToCombine, ignore_index=True)

# print(finalDataframe)

# Export the dataframe to an excel sheet
finalDataframe.to_excel('List of Last Names.xlsx')
