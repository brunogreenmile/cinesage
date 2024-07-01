## CineSage: Your Personal Movie Recommender
CineSage is a movie recommendation system designed to provide personalized movie suggestions using data from the TMDB API. This project showcases the integration of multiple technologies to create a seamless and efficient web application.

**Technologies Used:**

1. Python: The core programming language used for building the application logic and handling data processing.
   
2. Flask: A lightweight WSGI web application framework in Python that serves as the backbone of the web server, handling requests and responses. 

3. TMDB API: The Movie Database API is utilized to fetch real-time data on popular movies, ensuring the recommendations are always up-to-date. 

4. pandas: A powerful data manipulation and analysis library used to process and analyze the movie data.

5. scikit-learn: A machine learning library used for implementing the recommendation algorithm, specifically for vectorizing text data and computing similarity scores.

6. requests: A simple HTTP library for making API requests to the TMDB API and handling responses. 

7. pytest: A testing framework used to ensure the reliability and correctness of the application through automated tests. 

**Project Highlights**:

1. API Integration: Seamlessly integrates with the TMDB API to fetch and display a list of recommended movies.

2. Data Processing: Utilizes pandas for efficient data handling and processing, enabling quick transformations and analysis.

3. Machine Learning: Implements a content-based recommendation system using scikit-learn to compute movie similarities based on descriptions.

4. Web Development: Leverages Flask to create a responsive and interactive web interface that allows users to get movie recommendations by simply entering a title.

5. Testing: Ensures code quality and reliability with pytest, providing a robust suite of tests for continuous integration.

6. This project not only demonstrates proficiency in Python and web development but also showcases the ability to integrate external APIs and implement machine learning algorithms to deliver a practical and user-friendly application.

**AI in Movie Recommendations**
Movie recommendations use machine learning techniques to analyze and suggest movies based on user preferences. In the code, this is done through the following steps:

1. Data Representation (Feature Extraction):
The CountVectorizer from the scikit-learn library is used to transform the texts (movie synopses) into a matrix of word counts.
Each row of the matrix represents a movie, and each column represents a word (or term) present in the synopses. The cell contains the count of times the word appears in the movie synopsis.

2. Similarity Calculation (Cosine Similarity):
The cosine_similarity calculates the similarity between the word count vectors of the movies.
Cosine similarity is a metric that measures how similar two documents (or, in this case, movie synopses) are, regardless of their size.
The result is a similarity matrix, where each entry [i][j] indicates how similar the movies i and j are.
Similarity-Based Recommendation:

3. The system uses the user's preferences (movies they liked) to find similar movies.
For each movie the user liked, the system sums the corresponding similarity vectors to obtain an aggregate score.
The movies with the highest scores (which are not in the list of movies the user disliked) are recommended to the user.

## Installation - you must have at least Python 3.12.14

1. **Clone the repository**:
   ```sh
   git clone https://github.com/brunosantos/cinesage.git
   cd moviemate

2. **Install Miniconda**:
   - Download and install Miniconda from the official [Miniconda website](https://docs.conda.io/en/latest/miniconda.html).

3. **Create and activate a new conda environment with Python 3.10**:
   - Open your terminal or command prompt and run the following commands:

     ```sh
     conda create -n cinesage python=3.10
     conda activate cinesage
     ```

4. **Install the required packages**:
   - Install the necessary libraries using `conda`, which will handle all dependencies:

     ```sh
     conda install flask requests pandas scikit-learn
     ```

5. **Verify the installation**:
   - Ensure that all packages are installed correctly:

     ```sh
     conda list
     ```

## Running the Application

6. **Activate the conda environment**:
   - If not already activated, activate the environment:

     ```sh
     conda activate cinesage
     ```

7. **Run the Flask application**:
   - Start the Flask server:

     ```sh
     python run.py
     ```

8. **Access the application**:
   - Open your web browser and go to http://127.0.0.1:5000 to input your movie preferences and get personalized recommendations.

## Running the Tests

9. **Install pytest**:
   - Ensure `pytest` is installed in your conda environment:

     ```sh
     conda install pytest
     ```

10. **Run the tests**:
   - Execute the tests with the following command:

     ```sh
     pytest
     ```
