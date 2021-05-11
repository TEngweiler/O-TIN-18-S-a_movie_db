from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import MovieSerializer, MovieCreateSerializer, GenreSerializer
from .models import Movie, Genre


class MovieApiView(ModelViewSet):
    # https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    # Benötigt Serializer und Queryset (Daten)

    #serializer_class = MovieSerializer
    queryset = Movie.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['genres']

    def get_serializer_class(self):
        # POST, PUT Request --> get MovieCreateSerializer ...
        if self.action == 'create' or self.action == 'update':
            return MovieCreateSerializer
        return MovieSerializer


class GenreApiView(ModelViewSet):
    serializer_class = GenreSerializer
    queryset = Genre.objects.all()

