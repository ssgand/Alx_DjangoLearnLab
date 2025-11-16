from django.urls import path
from .views import book_list
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .admin_view import admin_view
from .librarian_view import librarian_view
from .member_view import member_view
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("list/", book_list, name="book_list"),
    path("library/<int:pk>/", list_books.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("register/", views.register.as_view(), name='register'),
    path('admin_view/', admin_view, name='Admin'),
    path('librarian_view/', librarian_view, name='librarian_view'),
    path('member_view/', member_view, name='member_view'),
    # path('books/add/', views.BookCreateView.as_view(), name='add_book'),
    # path('books/<int:pk>/edit/', views.BookUpdateView.as_view(), name='edit_book'),
    # path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='delete_book'),
    path('add_book/', views.book_create, name='add_book'),
    path('edit_book/<int:pk>/', views.book_update, name='edit_book'), # edit_book/
    path('delete_book/<int:pk>/', views.book_delete, name='delete_book'),
]