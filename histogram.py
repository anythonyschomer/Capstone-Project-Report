import matplotlib.pyplot as plt

features = ['danceability', 'energy', 'valence', 'tempo']
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
axes = axes.ravel()

for i, feature in enumerate(features):
    axes[i].hist(tracks_df[feature], bins=30)
    axes[i].set_title(feature.capitalize())
    axes[i].set_xlabel('Value')
    axes[i].set_ylabel('Frequency')

plt.tight_layout()
plt.show()