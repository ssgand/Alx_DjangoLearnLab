from django.urls import path
from .views import book_list
from .views import LibraryDetailView

urlpatterns = [
    path("list/", book_list, name="book_list"),
    path("library/<int:pk>/", LibraryDetailView.as_view(), name="library_detail"),
]