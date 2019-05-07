from django.db import models


class Rating(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')
    rating = models.IntegerField()

    def __str__(self):
        return str(self.rating)


class Genre(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Actor(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')
    name = models.CharField(max_length=90)

    def __str__(self):
        return self.name


class Movie(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False,
                          verbose_name='ID')
    title = models.CharField(max_length=90)  # Title of movie
    year = models.CharField(max_length=4)
    poster = models.TextField()
    contentRating = models.CharField(max_length=5)
    duration = models.CharField(max_length=20)
    releaseDate = models.DateField()
    averageRating = models.IntegerField()
    originalTitle = models.CharField(max_length=90)
    storyline = models.TextField()
    imdbRating = models.FloatField()
    posterurl = models.TextField()
    rating = models.ManyToManyField(Rating)
    genre = models.ManyToManyField(Genre)
    actor = models.ManyToManyField(Actor)

    def __str__(self):
        return self.title
