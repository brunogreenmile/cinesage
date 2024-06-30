import requests
from flask import current_app as app

def get_movie_data():
    url = f"{app.config['BASE_URL']}/movie/popular?api_key={app.config['API_KEY']}&language=en-US&page=1"
    response = requests.get(url)
    try:
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"Other error occurred: {err}")
        return []

    data = response.json()
    print(data)  # Debugging line to check the response
    if 'results' not in data:
        print(f"KeyError: {app.config['API_KEY']}")
        return []
    return data['results']