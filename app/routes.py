from flask import request, render_template, current_app as app
from .recommender import create_recommender, get_recommendations

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    liked_movies = request.form.get('liked_movies', '').split(',')
    disliked_movies = request.form.get('disliked_movies', '').split(',')
    user_preferences = {
        'liked_movies': [movie.strip() for movie in liked_movies if movie.strip()],
        'disliked_movies': [movie.strip() for movie in disliked_movies if movie.strip()],
    }

    print("User Preferences:", user_preferences)  # Debugging line

    movies_df, cosine_sim = create_recommender()
    if movies_df.empty:
        return render_template('recommendations.html', recommendations=[])

    recommendations = get_recommendations(user_preferences, movies_df, cosine_sim)
    print("Recommendations:", recommendations)  # Debugging line
    return render_template('recommendations.html', recommendations=recommendations)