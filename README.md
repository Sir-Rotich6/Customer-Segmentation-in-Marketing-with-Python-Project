📊 Customer Segmentation in Marketing with Python
📝 Project Overview

A concise summary of the project’s purpose, the business questions, and why segmentation matters for marketing teams.
(Use the GitHub description you already created.)

📂 Repository Structure
├── data/
│   ├── raw/
│   ├── processed/
│   └── final/
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_preprocessing.ipynb
│   ├── 03_clustering.ipynb
│   └── 04_insights.ipynb
├── src/
│   ├── data_prep.py
│   ├── clustering.py
│   ├── visualization.py
│   └── utils.py
├── reports/
│   ├── figures/
│   └── final_report.pdf
├── README.md
└── requirements.txt

📈 Business Questions

Does acquisition channel influence learning behavior?

Are students from different regions more likely to come through specific channels?

Do minutes watched and CLV vary significantly across segments?

How can segmentation inform marketing investment?

📦 Dataset Description

Explain the source and structure of the dataset (without exposing sensitive info):

Onboarding survey features

Country region

Acquisition channel

Minutes watched

Engagement metrics

Customer Lifetime Value (CLV)

Include:

Data shape

Feature types

Missing value notes (e.g., minutes watched nulls → 0)

🧼 Data Cleaning & Preprocessing

Handling null values

Encoding categorical variables (dummy variables for survey answers & regions)

Dropping redundant columns

Feature scaling using StandardScaler

Correlation analysis

Visualizations (heatmap, scatter plots)

🤖 Modeling: Clustering
1. Hierarchical Clustering (Ward)

Dendrogram interpretation

Determining number of clusters

2. K-Means Clustering

Elbow method

Final cluster selection based on hierarchical results

3. Final Segmentation

Cluster assignment

Cluster-level summaries

Key observations

📊 Results & Insights

(You will fill this after modeling.)

What segments emerged?

Behavioral differences?

Channel performance insights?

Recommendations for marketing strategy

🖼️ Visualizations

List or display:

Heatmap

Dendrogram

Elbow curve

Cluster scatter plots

🧠 Key Learnings

Highlight technical + business learnings:

Importance of scaling in clustering

Why hierarchical and K-Means differ

Marketing strategy implications

🚀 Future Work

Add DBSCAN or GMM clustering

Build a dashboard for marketing teams

Deploy as an API

Add automated reporting

📘 Requirements

State dependencies and link to requirements.txt.

👤 Author

@Enock Rotich
