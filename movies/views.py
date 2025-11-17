from django.http import HttpResponse
from django.template import loader
from .models import Movie
from django.shortcuts import render

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render({
            'movies': movies
        },
        request))

def movie_details(request, movie_id):
        movie = Movie.objects.get(id = movie_id)
        template = loader.get_template('movie_details.html') 
        context = {
            'movie': movie
        }
        return HttpResponse(template.render(context, request))