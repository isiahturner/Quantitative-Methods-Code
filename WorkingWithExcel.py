
# * The purpose of this code is to import an excel file, access the imported data and then create a function that
# * finds the last names beginning with 'a' while counting how many of the list start with 'a'. Will be using
# * pandas processes to get more practice using it.


# Importing the modules
import pandas as pd

# Importing the data

patientInfo = pd.read_excel(
    r'C:\Users\Isiah Turner\OneDrive\Documents\Quantitative Methods Code\faked_inventory (1).xlsx')

# Isolating the last names from the data frame to create a series
lastNames = patientInfo.iloc[:]['LastName']


print(lastNames[0])


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


# Using the function
lastNamesA, nameCountA = lastNameTracker(lastNames, 'a')
# print(lastNamesA)

# Preparing to export the list by converting to a dataframe
namesConversion = pd.DataFrame(lastNamesA)
# print(namesConversion)

namesConversion.to_excel('listOfNames1.xlsx')
