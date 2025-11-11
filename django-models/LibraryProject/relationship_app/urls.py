from django.urls import path
from .views import book_list
from .views import list_books

urlpatterns = [
    path("list/", book_list, name="book_list"),
    path("library/<int:pk>/", list_books.as_view(), name="library_detail"),  # LibraryDetailView
]