import json
import os

from django.shortcuts import render
from moviesApp.models import Movie, Genre, Actor, Rating
from backend.settings import BASE_DIR


def getAllMovies(request):
    """
    Initialize movies store and get all movies ordered by title
    :param request: petition
    :return: Render view whit movies data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = __initMovies()  # Initialize movies store
    return render(request, 'movies.html', {'movies_all': movies})


def getMostPopularMovies(request):
    """
    Gets the most popular movies ordered by imdbRating
    :param request: petition
    :return: Render view whit movies data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.all().order_by(
        '-imdbRating')  # Find movies order most popular
    return render(request, 'movies.html', {'movies_all': movies})


def getMovieDetails(request, movieId):
    """
    Get a movie details by id
    :param request: petition
    :param movieId: Pk movie for search
    :return: Render view whit a movie data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    from django.db.models import Q
    movie = Movie.objects.filter(id=movieId).first()  # Find a movie by ID
    similarMovies = Movie.objects.filter(
        Q(genre__in=movie.genre.all()) | Q(actor__in=movie.actor.all()) & Q(
            imdbRating=movie.imdbRating)
    ).exclude(id=movie.id).distinct().all()
    return render(request, 'details.html', {
        'movie': movie,
        'similarMovies': similarMovies
    })


def getMoviesByActor(request, actorName):
    """
    Get movies by actor
    :param request: petition
    :param actorName: Name Actor movie for search
    :return: Render view whit a movie data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.filter(
        actor__name=actorName).all()  # Find movies by actor
    return render(request, 'movies.html', {'movies_all': movies})


def getPlaylistByActor(request, actorName, position):
    """
    Get playlist by actor
    :param request: petition
    :param actorName: Name Actor movie for search
    :param position: Position to actual movie
    :return: Render view whit a movie data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.filter(
        actor__name=actorName).all()  # Find movies by actor
    actual_movie = movies[position]
    return render(request, 'playList.html',
                  {'movies_all': movies, 'movie': actual_movie,
                   'position': position, 'actorName': actorName}
                  )


def getMoviesByGenre(request, genreName):
    """
    Get movies by genre
    :param request: petition
    :param genreName: Name Genre movie for search
    :return: Render view whit a movie data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.filter(
        genre__name=genreName).all()  # Find movies by genre
    return render(request, 'movies.html', {'movies_all': movies})


def getPlaylistByGenre(request, genreName, position):
    """
    Get playlist by genre
    :param request: petition
    :param genreName: Name Genre movie for search
    :return: Render view whit a movie data
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.filter(
        genre__name=genreName).all()  # Find movies by genre
    actual_movie = movies[position]
    return render(request, 'playListGenre.html',
                  {'movies_all': movies, 'movie': actual_movie,
                   'position': position, 'actorName': genreName}
                  )


def __initMovies():
    """
    Initialize storage whit movies if doesn't exists.
    :return: Movies found into database
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    movies = Movie.objects.all().order_by('title')
    if movies:  # Verify if exists movies in the database
        return movies
    else:  # There are no movies in the database then they are loaded from the json file
        json_data = os.path.join(BASE_DIR, 'static',
                                 "movies.json")  # File directory
        with open(json_data) as file:  # Open json file to read data
            data = json.load(file)  # Read data file

            for movie in data:
                genres = __getGenres(
                    movie.get('genres', []))  # Generate list of genres objects
                actors = __getActors(
                    movie.get('actors', []))  # Generate list of actors objects
                ratings = __getRatings(movie.get('ratings',
                                                 []))  # Generate list of ratings objects

                # Search for the existence of a movie by title and year
                movie_aux = \
                    Movie.objects.filter(title=movie.get('title', ''),
                                         year=movie.get('year', '')).first()

                if movie_aux is None:
                    # Generate a new movie in the data base
                    imdbRating = movie.get('imdbRating', 0.0)
                    movie = Movie(
                        title=movie.get('title', ''),
                        year=movie.get('year', ''),
                        poster=movie.get('poster', ''),
                        contentRating=movie.get('contentRating', ''),
                        duration=movie.get('duration', ''),
                        releaseDate=movie.get('releaseDate', None),
                        averageRating=movie.get('averageRating', 0),
                        originalTitle=movie.get('originalTitle', ''),
                        storyline=movie.get('storyline', ''),
                        imdbRating=0.0 if type(
                            imdbRating) == str else imdbRating,
                        posterurl=movie.get('posterurl', '')
                    )
                    movie.save()
                    movie.genre.add(*genres)
                    movie.actor.add(*actors)
                    movie.rating.add(*ratings)
                    movie.save()
        movies = Movie.objects.all().order_by('title')
        return movies


def __getGenres(genres):
    """
    Get list of genres objects
    :return: List of genre objects
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    genres_response = list()
    for genre in genres:
        genre_aux = Genre.objects.filter(name=genre).first()
        if genre_aux is None:
            genre_aux = Genre(name=genre)
            genre_aux.save()
        genres_response.append(genre_aux)
    return genres_response


def __getActors(actors):
    """
    Get list of actors objects
    :return: List of actors objects
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    actors_response = list()
    for actor in actors:
        actor_aux = Actor.objects.filter(name=actor).first()
        if actor_aux is None:
            actor_aux = Actor(name=actor)
            actor_aux.save()
        actors_response.append(actor_aux)
    return actors_response


def __getRatings(ratings):
    """
    Get list of ratings objects
    :return: List of ratings objects
    @author: Diego Cortés <ingdiego.corts65@gmail.com>
    """
    ratings_response = list()
    for rating in ratings:
        rating_aux = Rating.objects.filter(rating=rating).first()
        if rating_aux is None:
            rating_aux = Rating(rating=rating)
            rating_aux.save()
        ratings_response.append(rating_aux)
    return ratings_response
