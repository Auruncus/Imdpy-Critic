from django.db import models
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)


class Movie(models.Model):
    imdb_movie_id = models.CharField(blank=False, null=False, unique=True, max_length=100, default="")
    title = models.CharField(blank=False, null=False, max_length=255, default='')
    year = models.PositiveIntegerField()
    genre1 = models.CharField(blank=False, null=False, max_length=255, default='')
    genre2 = models.CharField(blank=False, null=False, max_length=255, default='')
    genre3 = models.CharField(blank=False, null=False, max_length=255, default='')
    director = models.CharField(blank=False, null=False, max_length=255, default='')
    director_id = models.CharField(blank=False, null=False, max_length=100, default="")
    writer = models.CharField(blank=False, null=False, max_length=255, default='')
    writer_id = models.CharField(blank=False, null=False, max_length=100, default="")
    actor1 = models.CharField(blank=False, null=False, max_length=255, default='')
    actor1_id = models.CharField(blank=False, null=False, max_length=100, default="")
    actor2 = models.CharField(blank=False, null=False, max_length=255, default='')
    actor2_id = models.CharField(blank=False, null=False, max_length=100, default="")
    actor3 = models.CharField(blank=False, null=False, max_length=255, default='')
    actor3_id = models.CharField(blank=False, null=False, max_length=100, default="")

class RatingInfo(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(validators=(MinValueValidator(0),MaxValueValidator(5)))

    class Meta:
        abstract = True

class MovieRating(RatingInfo):
    title = models.CharField(blank=False, null=False, max_length=255, default='')
    imdb_movie_id = models.CharField(blank=False, null=False, max_length=100, default="")


class GenreRating(RatingInfo):
    genre = models.CharField(blank=False, null=False, max_length=255, default='')

class DirectorRating(RatingInfo):
    director = models.CharField(blank=False, null=False, max_length=255, default='')
    imdb_person_id = models.CharField(blank=False, null=False, max_length=100, default="")

class WriterRating(RatingInfo):
    writer = models.CharField(blank=False, null=False, max_length=255, default='')
    imdb_person_id = models.CharField(blank=False, null=False, max_length=100, default="")

class ActorRating(RatingInfo):
    actor = models.CharField(blank=False, null=False, max_length=255, default='')
    imdb_person_id = models.CharField(blank=False, null=False, max_length=100, default="")

