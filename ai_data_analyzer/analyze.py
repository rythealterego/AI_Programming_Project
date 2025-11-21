import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("iris.csv")

print("=== FIRST 5 ROWS ===")
print(df.head())

print("\n=== SUMMARY STATISTICS ===")
print(df.describe())

print("\n=== NULL VALUES ===")
print(df.isnull().sum())

# Simple visualization
plt.figure(figsize=(7,5))
plt.hist(df['sepal_length'], bins=20)
plt.title("Distribution of Sepal Length")
plt.xlabel("Sepal Length")
plt.ylabel("Frequency")
plt.show()
