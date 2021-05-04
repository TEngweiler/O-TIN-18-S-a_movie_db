from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .serializers import MovieSerializer
from .models import Movie


class MovieApiView(ModelViewSet):
    # https://www.django-rest-framework.org/api-guide/viewsets/#modelviewset
    # Benötigt Serializer und Queryset (Daten)

    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

