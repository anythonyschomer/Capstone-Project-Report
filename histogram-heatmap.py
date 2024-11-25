import matplotlib
matplotlib.use('Agg')  # Use a non-interactive backend

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data with appropriate encoding
df = pd.read_csv('top10s.csv', encoding='latin-1')

# Print the original columns to check their names
print("Original columns:", df.columns)

# Rename 'danceability' to 'dnce'
df.rename(columns={'danceability': 'dnce'}, inplace=True)

# Print the updated columns to confirm the change
print("Updated columns:", df.columns)

# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 16))

# Histogram for 'dnce'
ax1.hist(df['dnce'], bins=30, color='skyblue', edgecolor='black')
ax1.set_title('Histogram of Danceability (now dnce)')
ax1.set_xlabel('Danceability Value (dnce)')
ax1.set_ylabel('Frequency')
ax1.grid(axis='y', alpha=0.75)

# Correlation Heatmap
features = ['dnce', 'nrgy', 'dB', 'live', 'val', 'dur', 'acous', 'spch']
correlation_matrix = df[features].corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1, center=0, ax=ax2)
ax2.set_title('Correlation Heatmap of Audio Features')

plt.tight_layout()

# Save the figure as a PNG file
plt.savefig('histogram_heatmap_output.png')

print("Plots saved as 'histogram_heatmap_output.png'")

# Optionally, you can still include plt.show() for environments that support it
# plt.show()