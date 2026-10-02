favorite_movies = [
    {"name": "The Matrix", "release_year": 1999},
    {"name": "Inception", "release_year": 2010},
    {"name": "Pulp Fiction", "release_year": 1994},
    {"name": "Interstellar", "release_year": 2014},
    {"name": "Spirited Away", "release_year": 2001},
    {"name": "Goodfellas", "release_year": 1990},
    {"name": "Parasite", "release_year": 2019},
]


def check_release_year(movie):
    if movie["release_year"] < 2000:
        print(f"{movie['name']}: This movie was released before 2000")
    else:
        print(f"{movie['name']}: This movie was released after 2000")
        return movie["name"]


recent_movies = []

for movie in favorite_movies:
    result = check_release_year(movie)
    if result is not None:
        recent_movies.append(result)

print(recent_movies)
