from django.db import models

# Create your models here.

class Author(models.Model):
    '''
        Model to record different authors
    '''
    name = models.CharField(max_length=200)

class Book(models.Model):
    '''
        Model that will save books with these fields:
            - title: The title of the book
            - publication_year: The year the book was published
            - author: Foreign key to links a books to its author
    '''

    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='author')