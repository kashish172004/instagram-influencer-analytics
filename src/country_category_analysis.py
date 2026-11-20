
import pandas as pd
from pathlib import Path

# Find the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Load the feature-engineered dataset
input_file = PROJECT_DIR / "data" / "processed" / "influencers_features.csv"

df = pd.read_csv(input_file)

# Handle accounts with missing country information
df["country"] = df["country"].fillna("Unknown")

# Create a country-wise category table
country_category = pd.crosstab(
    df["country"],
    df["follower_category"]
)

# Calculate total accounts in each country
country_category["Total"] = country_category.sum(axis=1)

# Show the 10 countries with the most accounts
top_10_countries = country_category.sort_values(
    by="Total",
    ascending=False
).head(10)

# Save the analysis
output_file = PROJECT_DIR / "data" / "processed" / "country_category_analysis.csv"

top_10_countries.to_csv(output_file)

# Display results
print("\nCountry-wise Influencer Category Analysis:")
print(top_10_countries.to_string())

print("\nAnalysis saved successfully!")
print("Saved to:", output_file)
