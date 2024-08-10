from .models import Director, Genre, Actor, Country

def seeder_func():
    directors = ['Steven Spielberg', "Martin Scorsese"]
    genres = ['Comedy', 'Drama', 'Melodrama', 'Horror', 'Historic']
    actors = ['Satoh Takeru', 'Jack Nicholson', 'Tom Hanks']
    countries = ['Japan', 'China', 'Georgia', 'USA']

    for director in directors:
        if not Director.objects.filter(name=director):
            new_director = Director(name=director)
            new_director.save()

    for genre in genres:
        if not Genre.objects.filter(name=genre):
            new_genre = Genre(name=genre)
            new_genre.save()

    for actor in actors:
        if not Actor.objects.filter(name=actor):
            new_actor = Actor(name=actor)
            new_actor.save()

    for country in countries:
        if not Country.objects.filter(name=country):
            new_country = Country(name=country)
            new_country.save()