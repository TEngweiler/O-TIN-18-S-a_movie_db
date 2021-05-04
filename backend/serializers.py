from rest_framework.serializers import ModelSerializer

from .models import Movie, Genre


class GenresNestedSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']


class MovieSerializer(ModelSerializer):
    genres = GenresNestedSerializer(many=True)


    # https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    # Benötigt Model und Fields
    class Meta:
        model = Movie
        # Alle Felder explizit angeben
        fields = ['id', 'title', 'description', 'duration', 'genres']

        # Alle Felder ausser ....
        #exclude = ['genres']

        # Alle Felder darstellen
        #fields = '__all__'


class MovieCreateSerializer(ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class GenreSerializer(ModelSerializer):

    class Meta:
        model = Genre
        fields = ['id', 'name']