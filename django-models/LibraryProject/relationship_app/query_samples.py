from .models import Author
from .models import Library
from .models import Book
from .models import Librarian

# All books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()

# All books in a library
library = Library.objects.get(name="library_name")
books_in_library = library.books.all()

# Librarian for a library
library = Library.objects.get(name="library_name")
librarian = library.librarian