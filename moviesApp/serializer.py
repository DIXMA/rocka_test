from rest_framework import serializers

from moviesApp.models import Movie, Actor, Genre, Rating


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'
