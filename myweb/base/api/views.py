from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/movies",
        "GET /api/movies/:id"
    ]
    return Response(routes)

@api_view(['GET'])
def get_movies(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_movie(request, id):
    movie = Movie.objects.get(id=id)
    serializer = MovieSerializer(movie, many=False)
    return Response(serializer.data)