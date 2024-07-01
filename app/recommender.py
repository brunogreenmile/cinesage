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

def get_recommendations(user_preferences, movies_df, cosine_sim):
    liked_movies = user_preferences['liked_movies']
    disliked_movies = user_preferences['disliked_movies']
    
    print("Liked Movies:", liked_movies)
    print("Disliked Movies:", disliked_movies)

    liked_indices = []
    for movie in liked_movies:
        idx = movies_df[movies_df['title'].str.contains(movie, case=False, na=False)].index
        print(f"Searching for '{movie}'")
        print(f"Titles in dataset matching '{movie}': {movies_df[movies_df['title'].str.contains(movie, case=False, na=False)]['title'].values}")
        if not idx.empty:
            liked_indices.append(idx[0])
    
    print("Liked Indices:", liked_indices)

    if not liked_indices:
        # If no liked movies are found, return top popular movies excluding disliked ones
        recommended_movies = [movie for movie in movies_df['title'] if movie not in disliked_movies]
        return recommended_movies[:10]  # Limit to top 10 recommendations

    sim_scores = sum(cosine_sim[idx] for idx in liked_indices)
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    recommended_movies = []
    for i, score in sim_scores:
        if movies_df.iloc[i]['title'] not in disliked_movies:
            recommended_movies.append(movies_df.iloc[i]['title'])
            if len(recommended_movies) >= 10:  # Limit to top 10 recommendations
                break

    print("Recommended Movies:", recommended_movies)
    return recommended_movies