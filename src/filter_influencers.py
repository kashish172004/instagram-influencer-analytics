
import pandas as pd
from pathlib import Path

# Find project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Read downloaded dataset
input_file = PROJECT_DIR / "data" / "raw" / "instagram_latest.csv"

# Save filtered dataset
output_file = PROJECT_DIR / "data" / "processed" / "influencers_under_1m.csv"

# Load data
df = pd.read_csv(input_file)

# Keep accounts with followers between 1 and 999,999
df = df[(df["followers"] > 0) & (df["followers"] < 1000000)]

# Remove duplicate usernames
df = df.drop_duplicates(subset=["username"])

# Save filtered dataset
df.to_csv(output_file, index=False)

print("Filtered dataset created successfully!")
print("Total influencers:", len(df))
print("Saved to:", output_file)
