import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Load the dataset
data = pd.read_csv('purchase_history.csv')

# Select features for clustering
features = data[['TotalAmountSpent', 'NumberOfPurchases', 'AvgPurchaseValue', 'PurchaseFrequency', 'Recency']]

# Standardize the features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Using the elbow method to determine the optimal number of clusters
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(scaled_features)
    inertia.append(kmeans.inertia_)

# Plot the elbow curve
plt.figure(figsize=(8, 6))
plt.plot(K, inertia, 'bo-')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# Assume the optimal number of clusters is 4 (determined from the elbow plot)
optimal_k = 4
kmeans = KMeans(n_clusters=optimal_k, random_state=42)
kmeans.fit(scaled_features)

# Add cluster labels to the original data
data['Cluster'] = kmeans.labels_

# Analyze cluster centers
cluster_centers = scaler.inverse_transform(kmeans.cluster_centers_)
cluster_centers_df = pd.DataFrame(cluster_centers, columns=features.columns)
print(cluster_centers_df)

# Visualize the clusters
plt.figure(figsize=(8, 6))
plt.scatter(data['TotalAmountSpent'], data['NumberOfPurchases'], c=data['Cluster'], cmap='viridis')
plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Purchases')
plt.title('Customer Clusters')
plt.show()
