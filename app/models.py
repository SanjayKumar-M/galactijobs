from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    director = models.CharField(max_length=50)
    genre = models.CharField(max_length=50)
    year = models.PositiveIntegerField()

    def __str__(self) ->str:
        return self.title