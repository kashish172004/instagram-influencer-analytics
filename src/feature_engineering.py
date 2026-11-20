
import pandas as pd
from pathlib import Path

# Find project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Input and output files
input_file = PROJECT_DIR / "data" / "processed" / "influencers_under_1m.csv"
output_file = PROJECT_DIR / "data" / "processed" / "influencers_features.csv"

# Load filtered dataset
df = pd.read_csv(input_file)

# Create follower categories
def categorize_followers(followers):
    if followers < 10000:
        return "Nano"
    elif followers < 50000:
        return "Micro"
    elif followers < 500000:
        return "Mid-tier"
    else:
        return "Macro"

df["follower_category"] = df["followers"].apply(categorize_followers)

# Save feature-engineered dataset
df.to_csv(output_file, index=False)

print("Feature engineering completed!")
print("\nFollower category distribution:")
print(df["follower_category"].value_counts())

print("\nSaved file:", output_file)
