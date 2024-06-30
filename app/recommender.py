import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import get_movie_data

def create_recommender():
    movies = get_movie_data()
    if not movies:
        return pd.DataFrame(), None
    movies_df = pd.DataFrame(movies)
    count_vectorizer = CountVectorizer(stop_words='english')
    count_matrix = count_vectorizer.fit_transform(movies_df['overview'].fillna(''))
    cosine_sim = cosine_similarity(count_matrix, count_matrix)
    return movies_df, cosine_sim

def get_recommendations(movies_df):
    return movies_df['title'].tolist()