from django.db import models

# Fields and Models description
# https://docs.djangoproject.com/en/3.2/topics/db/models/

# Movie Model
class Movie(models.Model):
    # sql -> varchar(256)
    title = models.CharField(max_length=256)
    # sql -> text
    description = models.TextField(blank=True)
    # sql -> int default 0
    duration = models.IntegerField(default=0)

    genres = models.ManyToManyField('Genre', related_name='movies')


# Genre Model
class Genre(models.Model):
    name = models.CharField(max_length=256)


