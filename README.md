# 📊 Instagram Influencer Analytics

**SR NEXT – Data Analytics Project**

A Python-based Instagram Influencer Analytics project focused on data cleaning, influencer segmentation, country-wise analysis, category distribution, and data visualization.

## 🚀 Project Overview

This project analyzes Instagram influencer account data to identify patterns based on follower counts, account categories, and geographical distribution.

The objective is to transform raw influencer data into a structured dataset and meaningful insights that can support influencer research and marketing decisions.

## 🎯 Project Objectives

- Collect and explore Instagram influencer account data.
- Clean and preprocess raw datasets using Python.
- Filter accounts with fewer than 1 million followers.
- Categorize influencers based on follower count.
- Analyze country-wise and category-wise distributions.
- Generate visual reports and data quality checks.

## 🛠️ Technologies Used

- Python
- Pandas
- Matplotlib
- Git & GitHub
- VS Code

## 📁 Project Structure

```text
instagram-influencer-analytics/
│
├── data/
│   ├── raw/
│   │   └── instagram_latest.csv
│   │
│   └── processed/
│
├── src/
│   ├── analyze_data.py
│   ├── category_visualization.py
│   ├── country_category_analysis.py
│   ├── create_sample_data.py
│   ├── data_quality_check.py
│   ├── feature_engineering.py
│   ├── filter_influencers.py
│   └── influencer_visualization.py
│
├── .gitignore
└── README.md
```

## ⚙️ Features Implemented

### 1. Data Cleaning
- Removed duplicate influencer usernames.
- Handled missing and invalid values.
- Converted follower counts into numeric format.
- Prepared a cleaned dataset for analysis.

### 2. Influencer Segmentation

Influencers are categorized based on follower count:

| Category | Followers |
|---|---:|
| Nano | Below 10K |
| Micro | 10K–49,999 |
| Mid-tier | 50K–499,999 |
| Macro | 500K–999,999 |

### 3. Exploratory Data Analysis
- Country-wise influencer distribution.
- Category-wise influencer distribution.
- Comparison of influencer segments across countries.

### 4. Data Visualization
- Top countries analysis.
- Category distribution chart.
- Visual representation of influencer data.

### 5. Data Quality Validation
- Missing-value analysis.
- Duplicate record checks.
- Invalid follower count checks.
- Dataset validation.

## 📈 Key Findings

After filtering and preprocessing:

- **12,108** original account records.
- **7,241** records retained with follower counts above zero and below 1 million.
- **7 duplicate usernames** removed.
- **0 duplicate usernames** in the final filtered dataset.
- **0 invalid follower records** in the final dataset.

### Influencer Distribution

| Category | Number of Accounts |
|---|---:|
| Mid-tier | 3,938 |
| Macro | 1,428 |
| Micro | 1,177 |
| Nano | 698 |

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/kashish172004/instagram-influencer-analytics.git
```

### 2. Navigate to the project folder

```bash
cd instagram-influencer-analytics
```

### 3. Install dependencies

```bash
pip install pandas matplotlib
```

### 4. Run the analysis scripts

Run these commands from the project root:



