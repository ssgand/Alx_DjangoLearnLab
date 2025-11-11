from django.shortcuts import render
from .models import Book
from django.views.generic import DetailView, ListView

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'list_books.html', context)

class LibraryDetailView(DetailView):
    model = Book
    template_name = 'library_detail.html'
    # context_object_name = 'book'

