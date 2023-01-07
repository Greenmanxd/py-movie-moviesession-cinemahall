from db.models import Movie

from django.db.models import QuerySet


def get_movies(genres_ids: list = None, actors_ids: list = None) -> QuerySet:
    movies = Movie.objects.all()
    if genres_ids:
        movies = movies.filter(genres__id__in=genres_ids)

    if actors_ids:
        movies = movies.filter(actors__id__in=actors_ids)

    return movies


def get_movie_by_id(movie_id: int) -> QuerySet:
    return Movie.objects.get(id=movie_id)


def create_movie(
        movie_title: str,
        movie_description: str,
        genres_ids: list = None,
        actors_ids: list = None) -> None:

    new_movie = Movie.objects.create(
        title=movie_title,
        description=movie_description,
    )

    if genres_ids:
        new_movie.genres.set(genres_ids)

    if actors_ids:
        new_movie.actors.set(actors_ids)