from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import MovieSerializer, GenreSerializer
from .models import Movie, Genre


class MovieApiView(ModelViewSet):
    # https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    # Benötigt Serializer und Queryset (Daten)

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()


class GenreApiView(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

