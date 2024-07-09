from rest_framework import viewsets

from movie.models import Movie
from movie.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filterset_fields = ('tittle', 'director', 'year', 'point')
    search_fields = ('tittle', 'director')
    ordering_fields = ('tittle', 'director', 'year', 'point')
    ordering = ('point', )
