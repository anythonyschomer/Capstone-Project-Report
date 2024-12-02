# Music Streaming and Song Recommendations Using ML Algorithms

## Project Overview
This capstone project investigates the algorithms used by music streaming services to recommend similar songs and enhance user experiences. The focus is on how platforms like Spotify and Apple Music use listeners' preferences to create personalized playlists tailored to individual tastes.

## Table of Contents
- [Key Objectives](#key-objectives)
- [Data Sources](#data-sources)
- [Computational Resources and Tutorials](#computational-resources-and-tutorials)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Machine Learning Implementation](#machine-learning-implementation)
- [Key Findings](#key-findings)
- [Conclusions](#conclusions)
- [Installation](#installation)
- [Usage](#usage)
- [Future Work](#future-work)
- [Project Deliverables](#project-deliverables)
- [Tools and Technologies Used](#tools-and-technologies-used)
- [Author](#author)

## Key Objectives
- Analyze open datasets from Spotify and MusicBrainz.
- Develop a test system for song recommendations based on user behavior and preferences.
- Explore machine learning methods such as collaborative filtering and content-based analysis.
- Address challenges in current recommendation algorithms.

## Data Sources
- [Spotify Million Playlist Dataset](https://www.kaggle.com/datasets/shubhendra/million-playlist-dataset)
- [Spotify Web API](https://developer.spotify.com/documentation/web-api/)
- [MusicBrainz Database](https://musicbrainz.org/)

## Computational Resources and Tutorials
- **Spotify Web API Documentation**: Used for accessing and understanding the Spotify dataset structure.
- **Scikit-learn documentation**: Utilized for implementing machine learning algorithms.
- **Pandas documentation**: Referenced for data manipulation and analysis.

## Exploratory Data Analysis (EDA)

### Introduction
Exploratory Data Analysis (EDA) is a crucial step in understanding the dataset and uncovering patterns that inform our recommendation algorithms.

### Key Findings
- **Distribution of Audio Features**: The distribution of key audio features such as danceability, energy, and tempo was analyzed.
- **Insights**: The analysis provided insights into how different audio features relate to each other and their potential impact on user preferences.

### Conclusion
The insights gained from the EDA will guide the development of our recommendation system by highlighting important features that influence user preferences.

## Machine Learning Implementation

### Content-Based Filtering
We implemented a content-based recommender using cosine similarity on audio features:
1. Vectorizing tracks based on their audio features and genre.
2. Computing cosine similarity between track vectors.
3. Recommending tracks with the highest similarity scores.

### Collaborative Filtering
We used matrix factorization for collaborative filtering:
1. Creating a user-item interaction matrix.
2. Applying Singular Value Decomposition (SVD) to factorize the matrix.
3. Predicting user preferences based on latent factors.

### Hybrid Approach
We combined content-based and collaborative filtering results using a weighted average to produce final recommendations.

## Key Findings

### Audio Feature Distribution
![Audio Feature Distribution](audio_feature_distribution.png)  
*Figure 1: Distribution of key audio features (danceability, energy, valence, and tempo)*

- Most audio features exhibit normal distributions.
- Valence shows a slight positive skew, indicating a tendency towards more positive-sounding tracks.

### Feature Correlations
![Correlation Heatmap](correlation_heatmap.png)  
*Figure 2: Correlation heatmap of audio features*

- Strong positive correlation (0.76) between energy and loudness.
- Acousticness shows negative correlations with energy (-0.72) and loudness (-0.59).
- Moderate positive correlation (0.39) between danceability and valence.

## Conclusions
1. The balanced distribution of audio features suggests a diverse dataset.
2. Strong correlations between certain features (e.g., energy and loudness) indicate their importance in music perception.
3. The relationship between danceability and valence suggests potential for mood-based playlist creation.
4. Content-based recommendation systems provide consistent suggestions but may lack serendipity in discovering new music styles.

## Installation
To install the project, clone the repository:
```bash
git clone https://github.com/anythonyschomer/Capstone-Project-Report.git
cd Capstone-Project-Report
pip install -r requirements.txt
