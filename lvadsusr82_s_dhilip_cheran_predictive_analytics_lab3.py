# -*- coding: utf-8 -*-
"""LVADSUSR82_S DHILIP CHERAN_predictive analytics_LAB3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1fdn-rdrThd0SqdwaMXIRgztLG-cC9zgi
"""

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import silhouette_score
from sklearn.compose import ColumnTransformer

# Step 1: Read Data
data = pd.read_csv("/content/seeds.csv")

# Step 2: Data Preprocessing
# Handle missing values
# If there are missing values, replace them with the mean of the respective column

missing_values_cols = data.columns[data.isnull().any()]
missing_values_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])
preprocessor = ColumnTransformer(
    transformers=[
        ('missing_values', missing_values_transformer, missing_values_cols)
    ]
)
# Apply preprocessing pipeline
data_preprocessed = preprocessor.fit_transform(data)
data_preprocessed = pd.DataFrame(data_preprocessed, columns=data.columns)

# Handle outliers
# No specific outlier handling needed for clustering, as outliers can sometimes represent distinct clusters.

# Standardize features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data_preprocessed)

# Step 3: Exploratory Data Analysis
# Descriptive Statistics
print("Descriptive Statistics:")
print(data.describe())

# Correlation Heatmap
print("\nCorrelation Heatmap:")
plt.figure(figsize=(10, 8))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap")
plt.show()

# Pairplot
print("\nPairplot:")
sns.pairplot(data, diag_kind='kde')
plt.title("Pairplot")
plt.show()

# Distribution of each feature
print("\nDistribution of Each Feature:")
plt.figure(figsize=(12, 10))
for i, col in enumerate(data.columns[:-1]):
    plt.subplot(3, 3, i + 1)
    sns.histplot(data[col], bins=20, kde=True)
    plt.title(f"Distribution of {col}")
plt.tight_layout()
plt.show()


#Visualization

import matplotlib.pyplot as plt
import seaborn as sns


sns.pairplot(pd.DataFrame(data_scaled, columns=data.columns))
plt.title("Pairplot of Scaled Features")
plt.show()
# Checking for missing values

missing_values_cols = data.columns[data.isnull().any()]
missing_values_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean'))
])
preprocessor = ColumnTransformer(
    transformers=[
        ('missing_values', missing_values_transformer, missing_values_cols)
    ]
)
# Apply preprocessing pipeline
data_preprocessed = preprocessor.fit_transform(data)
data_preprocessed = pd.DataFrame(data_preprocessed, columns=data.columns)

# Handle missing values (if any)
data.fillna(data.mean(), inplace=True)

# Handle outliers:

def winsorize(data):
    return mstats.winsorize(data, limits=[0.05, 0.05])

for col in data.select_dtypes(include=['float64', 'int64']).columns:
    data[col] = winsorize(data[col])


print("Descriptive Statistics:")
print(data.describe())

print("\nShape of the Data:")
print(data.shape)

# Step 4: Model Training & Testing (using ensemble model - Agglomerative Clustering)
# Standardize features
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# Choose the number of clusters (K)
k = 3

# Initialize and fit Agglomerative Clustering model
agg_clustering = AgglomerativeClustering(n_clusters=k)
clusters = agg_clustering.fit_predict(data_scaled)

# Step 5: Model Evaluation Metrics
# Evaluate the model using silhouette score
silhouette_avg = silhouette_score(data_scaled, clusters)
print("\nSilhouette Score:", silhouette_avg)