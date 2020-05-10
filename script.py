# Import the libraries
import numpy as np

# Load the data
calorie_stats = np.genfromtxt('cereal.csv', delimiter=',')

# Calcuate how much higher the average calorie count is compared to competitors using the mean
average_calories = np.mean(calorie_stats)
print(average_calories)

# Sort the data to see if the average adequately reflects the distribution of the dataset
calorie_stats_sorted = np.sort(calorie_stats)
print(calorie_stats_sorted)

# Check to see if the median is a better represenation of the dataset since monst of the cereals are higher than the mean
median_calories = np.median(calorie_stats)
print(median_calories)

# Find the percentile that is greater than 60 calories
print(np.percentile(calorie_stats, 25))
print(np.percentile(calorie_stats, 12))
print(np.percentile(calorie_stats, 6))
print(np.percentile(calorie_stats, 3))
print(np.percentile(calorie_stats, 4))

nth_percentile = np.percentile(calorie_stats, 4)

# Calculate the percentage of cereals that have more than 60 calories per serving
more_calories = np.mean(calorie_stats > 60)
print(more_calories)

# Calcuate the amount of variation in th data by finding the standard deviation
calorie_std = np.std(calorie_stats)
print(calorie_std)
