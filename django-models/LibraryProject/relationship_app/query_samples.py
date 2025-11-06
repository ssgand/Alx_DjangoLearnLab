from .models import Author
from .models import Library
from .models import Book
from .models import Librarian

# All books by a specific author
# objects.filter(author=author)
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = author.books.all()

# All books in a library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()

# Librarian for a library
library = Library.objects.get(name=library_name)
librarian = library.librarian