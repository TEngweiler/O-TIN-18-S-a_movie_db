from django.contrib import admin

# import von den Modelsklassen
from .models import Movie, Genre


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'duration']
    list_filter = ['genres']
    search_fields = ['title', 'description']


# Pass wird benötigt fals keine definition innerhalb der Klasse existiert
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass 
