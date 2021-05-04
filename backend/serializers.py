from rest_framework.serializers import ModelSerializer

from .models import Movie


class MovieSerializer(ModelSerializer):
    # https://www.django-rest-framework.org/api-guide/serializers/#modelserializer
    # Benötigt Model und Fields
    class Meta:
        model = Movie
        # Alle Felder explizit angeben
        fields = ['id', 'title', 'description', 'duration']

        # Alle Felder ausser ....
        #exclude = ['genres']

        # Alle Felder darstellen
        #fields = '__all__'


