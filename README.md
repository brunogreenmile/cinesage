# CineSage: Your Personal Movie Recommender

CineSage: Your Personal Movie Recommender

CineSage is a movie recommendation system designed to provide personalized movie suggestions using data from the TMDB API. This project showcases the integration of multiple technologies to create a seamless and efficient web application.

Technologies Used:

Python: The core programming language used for building the application logic and handling data processing.
Flask: A lightweight WSGI web application framework in Python that serves as the backbone of the web server, handling requests and responses.
TMDB API: The Movie Database API is utilized to fetch real-time data on popular movies, ensuring the recommendations are always up-to-date.
pandas: A powerful data manipulation and analysis library used to process and analyze the movie data.
scikit-learn: A machine learning library used for implementing the recommendation algorithm, specifically for vectorizing text data and computing similarity scores.
requests: A simple HTTP library for making API requests to the TMDB API and handling responses.
pytest: A testing framework used to ensure the reliability and correctness of the application through automated tests.
Project Highlights:

API Integration: Seamlessly integrates with the TMDB API to fetch and display a list of recommended movies.
Data Processing: Utilizes pandas for efficient data handling and processing, enabling quick transformations and analysis.
Machine Learning: Implements a content-based recommendation system using scikit-learn to compute movie similarities based on descriptions.
Web Development: Leverages Flask to create a responsive and interactive web interface that allows users to get movie recommendations by simply entering a title.
Testing: Ensures code quality and reliability with pytest, providing a robust suite of tests for continuous integration.
This project not only demonstrates proficiency in Python and web development but also showcases the ability to integrate external APIs and implement machine learning algorithms to deliver a practical and user-friendly application. 

## Installation - you must have at least Python 3.12.14

1. Clone the repository:
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
   - Open your web browser and go to `http://127.0.0.1:5000/recommend` to get a list of popular movies.

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
