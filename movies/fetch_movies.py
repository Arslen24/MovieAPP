import requests
from rental.models import Movie  # Make sure 'Movie' model is correctly imported

# Replace this with your actual API key
TMDB_API_KEY = "cbd0e8dee46a56f9f1ec46051fdf36bc"
BASE_URL = "https://api.themoviedb.org/3"

def fetch_movies_from_tmdb():
    url = f"{BASE_URL}/movie/popular"
    params = {"api_key": TMDB_API_KEY, "language": "en-US", "page": 1}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        movies_data = response.json().get("results", [])
        for movie_data in movies_data:
            title = movie_data.get("title")
            description = movie_data.get("overview")
            release_year = movie_data.get("release_date", "").split("-")[0]
            poster_path = movie_data.get("poster_path")
            image_url = f"https://image.tmdb.org/t/p/w500{poster_path}" if poster_path else None

            Movie.objects.create(
            title=title,
            description=description,
            release_year=release_year,
            image_url=image_url,
        )
            
        print("Movies successfully fetched and added to the database!")
    else:
        print(f"Failed to fetch movies: {response.status_code}")