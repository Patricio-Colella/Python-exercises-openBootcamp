from asyncio.windows_events import NULL
from email.policy import default
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=20,help_text="titulo de la pelicula",null=True)
    author = models.ForeignKey("Author",on_delete=models.SET_NULL,null=True)
    summary = models.TextField(max_length=200,null=True)

    def __str__(self):
        return f"{self.title},{self.author},{self.summary}"

class Author(models.Model):
    name = models.CharField(max_length=20,null=True)

    def __str__(self):
        return f"{self.name}"