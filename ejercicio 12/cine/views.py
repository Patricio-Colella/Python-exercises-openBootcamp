
from django.shortcuts import render

from .models import Author, Movie
from django.http import QueryDict
import pprint


def index(request):
    
    if request.method=="POST":
        authorName = QueryDict(request.body)["authorName"]
        
    dbAuthors = Author.objects.all()
    if authorName!="":
        dbAuthors = Author.objects.filter(name=authorName)

    authors=[]
    for author in dbAuthors:
        filteredMovies = Movie.objects.filter(author=author.id)
        authors.append((author,filteredMovies))

    return render(
        request,
        "index.html",
        context={
            "authors":authors,
        }
    )
