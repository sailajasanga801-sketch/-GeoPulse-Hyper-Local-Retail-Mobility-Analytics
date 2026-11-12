
import pandas as pd

# Load the raw dataset
file_path = "data/raw/OSM_four_arc_merged_V3.csv"
df = pd.read_csv(file_path)

print("===== GEOPULSE DATASET INSPECTION =====")

# Dataset dimensions
print("\n1. Dataset Shape:")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

# Column names
print("\n2. Column Names:")
print(df.columns.tolist())

# Data types
print("\n3. Data Types:")
print(df.dtypes)

# Missing values
print("\n4. Missing Values:")
print(df.isnull().sum())

# Duplicate records
print("\n5. Duplicate Records:")
print(df.duplicated().sum())

# First five records
print("\n6. First Five Records:")
print(df.head())

print("\n===== INSPECTION COMPLETED =====")

