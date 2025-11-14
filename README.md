# 📊 Customer Segmentation in Marketing with Python
## 📝 Project Overview

Understanding how customers discover a product — and how this influences their engagement and long-term value — is central to modern data-driven marketing. This project applies practical machine learning and statistical analysis to uncover relationships between acquisition channels, study behavior, engagement levels, and customer lifetime value (CLV), using a real-world dataset derived from onboarding surveys, usage metrics, and lifetime-value records.

The core objective is to use unsupervised learning (clustering) to segment customers into meaningful groups that reflect behavioral, demographic, and value-based differences. These segments provide actionable insights for marketing teams, enabling them to optimize acquisition spend, refine messaging, and better understand which channels yield the most engaged and highest-value learners.


# 📂 Repository Structure
    customer-segmentation/
    │
    ├── README.md
    ├── requirements.txt
    ├── .gitignore
    │
    ├── data/
    │   ├── raw/                    # Original CSV dataset(s)
    │   ├── interim/                # Data after cleaning but before modeling
    │   └── processed/              # Final dataset used for clustering
    │
    ├── notebooks/
    │   ├── 01_data_exploration.ipynb
    │   ├── 02_preprocessing.ipynb
    │   ├── 03_clustering.ipynb
    │   └── 04_results_and_insights.ipynb
    │
    ├── src/
    │   ├── __init__.py
    │   │
    │   ├── data_prep.py            # Cleaning, missing values, encoding
    │   ├── feature_engineering.py  # Dummy creation, correlation filtering
    │   ├── clustering.py           # Hierarchical + K-means methods
    │   ├── visualization.py        # Heatmaps, dendrograms, elbow plots, etc.
    │   └── utils.py                # Helper functions
    │
    ├── models/
    │   ├── kmeans_model.pkl        # Saved final k-means model (if needed)
    │   └── scaler.pkl              # Saved StandardScaler
    │
    ├── reports/
    │   ├── figures/                # Visualizations generated in notebooks
    │   │   ├── dendrogram.png
    │   │   ├── elbow_curve.png
    │   │   └── cluster_visuals.png
    │   │
    │   ├── exploratory_report.md   # Summary of data exploration
    │   ├── clustering_report.md    # Summary of modeling results
    │   └── final_marketing_insights.pdf
    │
    └── scripts/
        ├── run_preprocessing.py    # CLI script for preprocessing
        ├── run_clustering.py       # CLI script for running clustering
        └── generate_report.py      # Auto-generate plots/reports



# 📈 Business Questions

Does acquisition channel influence learning behavior?

Are students from different regions more likely to come through specific channels?

Do minutes watched and CLV vary significantly across segments?

How can segmentation inform marketing investment?



# 📦 Dataset Description

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



# 🧼 Data Cleaning & Preprocessing

Handling null values

Encoding categorical variables (dummy variables for survey answers & regions)

Dropping redundant columns

Feature scaling using StandardScaler

Correlation analysis

Visualizations (heatmap, scatter plots)



# 🤖 Modeling: Clustering
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



# 📊 Results & Insights

(You will fill this after modeling.)

What segments emerged?

Behavioral differences?

Channel performance insights?

Recommendations for marketing strategy

# 🖼️ Visualizations

List or display:

Heatmap

Dendrogram

Elbow curve

Cluster scatter plots

# 🧠 Key Learnings

Highlight technical + business learnings:

Importance of scaling in clustering

Why hierarchical and K-Means differ

Marketing strategy implications

# 🚀 Future Work

Add DBSCAN or GMM clustering

Build a dashboard for marketing teams

Deploy as an API

Add automated reporting

# 📘 Requirements

    State dependencies and link to requirements.txt.

# 👤 Author

@Enock Rotich
