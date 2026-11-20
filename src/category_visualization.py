
import matplotlib
matplotlib.use("Agg")

import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Find project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load feature-engineered data
input_file = PROJECT_DIR / "data" / "processed" / "influencers_features.csv"

df = pd.read_csv(input_file)

# Count influencers in each category
category_counts = df["follower_category"].value_counts()

# Create a pie chart
plt.figure(figsize=(8, 8))
category_counts.plot(
    kind="pie",
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Influencer Category Distribution")
plt.ylabel("")

plt.tight_layout()

# Save chart
output_file = PROJECT_DIR / "data" / "processed" / "category_distribution.png"
plt.savefig(output_file)

plt.close()

print("Category chart saved successfully!")
print(category_counts)
print("Saved to:", output_file)
