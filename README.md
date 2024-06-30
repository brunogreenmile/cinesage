# CineSage: Your Personal Movie Recommender

CineSage is a movie recommendation system built with Flask and the TMDB API.

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