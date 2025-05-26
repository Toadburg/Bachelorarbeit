import matplotlib.pyplot as plt
from sqlalchemy import create_engine
import pandas
import numpy as np
from sklearn.cluster import KMeans


engine = create_engine('postgresql://postgres:banana@localhost:5432/bachelor')

query = """
SELECT "SERIAL", "AGE", "INCOME", "EMP"
FROM timeuse
WHERE "COUNTRY" = 'FI'
"""

df = pandas.read_sql_query(query, engine)
dropped_df = df.drop_duplicates(subset=['SERIAL'], keep='first')
"""
plt.scatter(df["EMP"], df["INCOME"])
plt.show()
"""

clustering_kmeans = KMeans(n_clusters=3)
df['clusters'] = clustering_kmeans.fit_predict(df)
clustering_kmeans.fit(df[['AGE', 'INCOME', 'EMP']])
labels = clustering_kmeans.labels_
centroids = clustering_kmeans.cluster_centers_

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['AGE'], df['INCOME'], df['EMP'], c=labels, cmap='viridis', s=50, alpha=0.6)
ax.scatter(centroids[:, 0], centroids[:, 1], centroids[:, 2], c='red', s=200, marker='X', label='Zentren')

ax.set_xlabel('AGE')
ax.set_ylabel('INCOME')
ax.set_zlabel('EMP')

# 7. Titel und Legende
ax.set_title('K-Means Clustering in 3D')
ax.legend()

# 8. Plot anzeigen
plt.show()

print(df.head())
df.to_csv('test_data.csv')


"""
#elbow method
wcss = []

for i in range(1,11):
    k_means = KMeans(n_clusters=i, init='k-means++', random_state=42)
    k_means.fit(X)
    wcss.append(k_means.inertia_)

plt.plot(np.arange(1,11),wcss)

"""