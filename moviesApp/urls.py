from django.urls import path
from moviesApp import views

urlpatterns = [
    # Get all movies
    path('', views.getAllMovies, name="movies_all"),
    # Get details for a movie
    path('details/<int:movieId>/', views.getMovieDetails, name="movies_all"),
    # Get most popular movies
    path('mostPopular/', views.getMostPopularMovies,
         name="movies_most_popular"),
    # Get movies by actor
    path('by/actor/<actorName>/', views.getMoviesByActor,
         name="movies_by_actor"),
    # Get movies by genre
    path('by/genre/<genreName>/', views.getMoviesByGenre,
         name="movies_by_actor"),
    path('playlist/actor/<actorName>/<int:position>/', views.getPlaylistByActor,
         name="playlist_by_actor"),
    path('playlist/genre/<genreName>/<int:position>/', views.getPlaylistByGenre,
         name="playlist_by_actor"),
    path('playlist/similarMovies/', views.getMoviesByGenre,
         name="playlist_by_similar_movies"),
]
