### Statistics ###
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd

# Variables
numPopulation = 1000000
numSample = 10

# Creating the data for the code
s = np.random.normal(loc=120, scale=20, size=numPopulation)
plt.hist(s, bins=240, range=(50, 190))
plt.ylabel('Number of People')
plt.xlabel('Systolic Blood Pressure')

# Standard deviation describes the spread of the population while the standard error
# while the spread of the sample mean is the standard error. Remember, we calculate sample
# means over and over again and place it on a distrubution. The sample means indicate where
# the center of our population is

# T-Statistic is the ratio of the departure of the estimated value of a parameter from
# its hypothesized value. Extreme t-statistics would suggest that the population's
# center is elsewhere. Then as the p-value goes down, means it is unlikely that the value
# comes from a different distribution increases.

### One sample t-tests ###
dataset = pd.read_excel(
    r'C:\Users\Isiah Turner\OneDrive\Documents\Quantitative Methods Code\deidentified_clinical_data.xlsx')
f = np.array(list(dataset.columns))
print(f)

# Pulling off BMI
bmi = list(dataset['mh_bmi'].dropna())
# for thing in bmi:
#     print(thing)
# # print(bmi)
# # print(bmi[1])

# Running a one-sample t-test to comparing the sample mean to 0
result0 = stats.ttest_1samp(bmi, 0)
print('\n')
print(f'The t-statistic for a sample compared to 0 is: {result0.statistic}')
print(f'The p-value for a sample compared to 0 is: {result0.pvalue}')
print('\n')

# Running a one-sample t-test to compare the sample mean to 28
result25 = stats.ttest_1samp(bmi, 28)
print(f'The t-statistic for a sample compared to 28 is: {result25.statistic}')
print(f'The p-value for a sample compared to 28 is is: {result25.pvalue}')
print('\n')

# Running a sample t-test to compare the sample mean to 28 and
# show importance of the number of samples used
lowSample = stats.ttest_1samp(bmi[0:10], 28)
print(f'The t-statistic when splicing values is: {lowSample.statistic}')
print(f'The p-value when splicing values is: {lowSample.pvalue}')
print('\n')

### Running a two sample t-test between males and females ###

# Isolating the data we want to work with. Want to compare the bmi between sexes
# so I will need to sync up BMI and sex so we can filter between men and women.
bmi2 = dataset['mh_bmi']
sex = dataset['demo_sex']

# Initializing our variables
counter = 0
males = []
females = []

# Filtering the bmi data into men and women lists
for element in bmi2:
    if np.isnan(element):
        counter += 1
    else:
        if sex[counter] == 'Male':
            males.append(element)
            counter += 1
        elif sex[counter] == 'Female':
            females.append(element)
            counter += 1
        else:
            counter += 1

# Checking whether there are the correct number of data points
# after cleaning out the NaN values.
if len(males) + len(females) == len(bmi2.dropna()):
    print('Correctly filtered the male and female BMI')
    print('\n')

# Running the two sample test and reporting the p-value and t-statistic
twoSample = stats.ttest_ind(males, females, equal_var=True)
print(f'The t-statistic for the two sample is: {twoSample.statistic}')
print(f'The p-value for the two sample is: {twoSample.pvalue}')
print('\n')

### Running a paired t-test ###

# Creating the dataset to work with to compare before and after
pairedDataset = {'Name': ['Ken', 'Marisa', 'Fiona', 'Tucker', 'Patterson'], 'Before': [1.1, 1.2, 1.3, 1.4, 1.5],
                 'After': [1.15, 1.26, 1.34, 1.45, 1.53]}
df = pd.DataFrame(pairedDataset)

# Running the paired sample t-test and reporting the t-statistics and pvalue
pairedSamples = stats.ttest_rel(df['Before'], df['After'])
print(f'The t-statistic for the paired sample is: {pairedSamples.statistic}')
print(f'The p-value for the paired sample is: {pairedSamples.pvalue}')
