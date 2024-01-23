"""
Synthetic data
"""

import pandas as pd
from sklearn.datasets import make_classification

#Data matrix X and response y
X, y = make_classification(
    n_samples = 200, 
    n_features = 2, 
    n_redundant = 0,
    n_clusters_per_class=1,
	)

#Data matrix
print(X)
print(type(X))

#Response (classification)
print(y)
print(type(y))

#Merge converted DataFrame and Series
df = pd.concat([pd.DataFrame(X), pd.Series(y)], axis=1)
#Rename columns
df.columns = ['x1', 'x2', 'y']
print(df.head())
print(df.tail())