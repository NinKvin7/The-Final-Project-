from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('movies/', views.get_movies),
    path('movies/<str:id>', views.get_movie)
]