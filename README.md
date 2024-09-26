Movie Recommendation System
This is a Python-based movie recommendation system that suggests movies similar to the one a user likes. The recommendations are made based on various features of the movies like genres, keywords, cast, and crew.

Features
Uses the TMDB 5000 Movies and Credits dataset to provide recommendations.
Text vectorization using the Bag of Words approach.
Stemming is applied to movie tags using NLTK.
Movie similarity is calculated using cosine similarity.

Datasets
tmdb_5000_movies.csv: Contains movie metadata such as title, genres, keywords, and overview.
tmdb_5000_credits.csv: Contains cast and crew information for the movies.

How It Works
Data Preprocessing:
Merge movie and credit datasets.
Select key features: movie_id, title, overview, genres, keywords, cast, crew.
Handle missing and duplicate values.
Convert genres, keywords, cast, and crew into lists using ast.literal_eval.
Apply stemming to reduce words to their root forms.

Feature Engineering:
Combine important features into a single column called tags.
Use CountVectorizer to convert text data into vectors (Bag of Words approach).
Remove stop words to clean the data.

Similarity Calculation:
Calculate cosine similarity between the movies based on their tags.

Recommendation Function:
Given a movie title, the system finds the most similar movies based on cosine similarity.

Given a movie title, the system finds the most similar movies based on cosine similarity.

