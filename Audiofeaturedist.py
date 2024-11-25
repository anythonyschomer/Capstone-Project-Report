import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data with appropriate encoding
df = pd.read_csv('top10s.csv', encoding='latin-1')

# List of audio features to analyze
features = ['dnce', 'nrgy', 'dB', 'live', 'val', 'dur', 'acous', 'spch']

# Create a figure with subplots for each feature
fig, axes = plt.subplots(4, 2, figsize=(20, 30))
fig.suptitle('Audio Feature Distributions', fontsize=16)

# Flatten the axes array for easier iteration
axes = axes.flatten()

# Plot distribution for each feature
for i, feature in enumerate(features):
    sns.histplot(df[feature], kde=True, ax=axes[i], color='skyblue')
    axes[i].set_title(f'Distribution of {feature}')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Frequency')

plt.tight_layout()

# Save the figure as a PNG file
plt.savefig('audio_feature_distributions.png')

print("Plots saved as 'audio_feature_distributions.png'")

# Optionally, you can still include plt.show() for environments that support it
# plt.show()