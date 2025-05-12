import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Error handling when loading data
try:
    # Load Iris dataset
    iris = load_iris()
    df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    
    # Display the first few rows
    print("First 5 rows of the dataset:")
    print(df.head())
    
    # Check data types and missing values
    print("\nData types:")
    print(df.dtypes)

    print("\nMissing values:")
    print(df.isnull().sum())

    # Clean the dataset (no missing values in Iris, but example shown)
    df = df.dropna()
except FileNotFoundError:
    print("Dataset file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
