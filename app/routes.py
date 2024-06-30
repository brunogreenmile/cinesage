from flask import request, jsonify, current_app as app
from .recommender import create_recommender, get_recommendations

@app.route('/recommend', methods=['GET'])
def recommend():
    print("Received request for recommendations")  # Debugging line
    movies_df, cosine_sim = create_recommender()
    if movies_df.empty:
        return jsonify({'error': 'No movies found'}), 404
    recommendations = get_recommendations(movies_df)
    return jsonify(recommendations)