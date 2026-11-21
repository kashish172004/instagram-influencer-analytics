
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load the feature-engineered dataset
input_file = PROJECT_DIR / "data" / "processed" / "influencers_under_1m.csv"

# Read the dataset
df = pd.read_csv(input_file)
# Count influencers in each content category
category_counts = df["category"].fillna("Unknown").value_counts()
top_countries = df["country"].fillna("Unknown").value_counts().head(10)

# Create the chart
plt.figure(figsize=(10, 6))
top_countries.plot(kind="bar")

plt.title("Top 10 Countries by Influencer Count")
plt.xlabel("Country")
plt.ylabel("Number of Influencers")
plt.xticks(rotation=45)

plt.tight_layout()

# Save the chart
output_file = PROJECT_DIR / "data" / "processed" / "top_countries.png"
plt.savefig(output_file)

plt.close()

print("Chart saved successfully!")
print("Saved to:", output_file)

