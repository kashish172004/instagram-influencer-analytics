
import pandas as pd
from pathlib import Path

# Find project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load processed dataset
input_file = PROJECT_DIR / "data" / "processed" / "influencers_features.csv"

df = pd.read_csv(input_file)

print("\n========== DATA QUALITY REPORT ==========")

# 1. Total records
print("\n1. Total records:", len(df))

# 2. Missing values
print("\n2. Missing values:")
print(df.isnull().sum())

# 3. Duplicate usernames
print("\n3. Duplicate usernames:", df["username"].duplicated().sum())

# 4. Invalid follower counts
invalid_followers = df[
    (df["followers"] <= 0) |
    (df["followers"] >= 1000000)
]

print("\n4. Invalid follower records:", len(invalid_followers))

# 5. Category distribution
print("\n5. Category distribution:")
print(df["follower_category"].value_counts())

# 6. Duplicate complete rows
print("\n6. Duplicate rows:", df.duplicated().sum())

print("\n========== VALIDATION COMPLETED ==========")

