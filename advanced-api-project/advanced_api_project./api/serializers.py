from rest_framework import serializers
from .models import Book
from .models import Author
from django.utils import timezone

class BookSerializer(serializers.ModelSerializer):
    '''
        Serializer that will validate the fields of the book model
    '''
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate(self, data):
        current_year = timezone.now().year
        if data['publicatoin_year'] > current_year:
            raise serializers.ValidationError(f"Year cannot be in the future (>{current_year}).")


class AuthorSerializer(serializers.ModelSerializer):
    '''
        Serializer that will validate the author model plus a nested books serializer that will validate
        the books by this author
    '''

    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']