import pandas as pd 
from pathlib import Path 

# find the main project directory
PROJECT_DIR =Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_DIR / "data" / "raw"
DATA_DIR.mkdir(parents=True, exist_ok = True)

# Fictional records for testing the project
 
influencers = [
    {
        "username": "demo_beauty_01",
        "followers": 25000,
        "niche": "Beauty",
        "avg_likes_last10": 1200,
        "avg_comments_last10": 80,
        "posts_per_month": 12,
        "contact_public": False,
        "data_type": "synthetic"
    },
    {
        "username": "demo_fashion_02",
        "followers": 40000,
        "niche": "Fashion",
        "avg_likes_last10": 1000,
        "avg_comments_last10": 50,
        "posts_per_month": 8,
        "contact_public": False,
        "data_type": "synthetic"
    },
    {
        "username": "demo_tech_03",
        "followers": 12000,
        "niche": "Tech",
        "avg_likes_last10": 600,
        "avg_comments_last10": 30,
        "posts_per_month": 15,
        "contact_public": False,
        "data_type": "synthetic"
    },
    {
        "username": "demo_lifestyle_04",
        "followers": 8000,
        "niche": "Lifestyle",
        "avg_likes_last10": 400,
        "avg_comments_last10": 20,
        "posts_per_month": 10,
        "contact_public": False,
        "data_type": "synthetic"
    },
    {
        "username": "demo_travel_05",
        "followers": 50000,
        "niche": "Travel",
        "avg_likes_last10": 1500,
        "avg_comments_last10": 100,
        "posts_per_month": 6,
        "contact_public": False,
        "data_type": "synthetic"
    }
]

df = pd.DataFrame(influencers)

output_file = DATA_DIR / "influencers.csv"
df.to_csv(output_file, index=False)

print("Sample dataset created successfully!")
print(f"Number of records: {len(df)}")
print(f"Saved to: {output_file}")
print(df.head())
 