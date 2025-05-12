# Basic statistics
print("\nDescriptive statistics:")
print(df.describe())

# Group by species and calculate mean for each feature
print("\nMean values by species:")
print(df.groupby('species').mean())

# Observation:
print("\nObservation:")
print("Setosa has generally smaller petal length and width, while Virginica has the largest.")
