from django.urls import path
from .views import book_list
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from .views import SignUpView

urlpatterns = [
    path("list/", book_list, name="book_list"),
    path("library/<int:pk>/", list_books.as_view(), name="library_detail"),
    path("login/", LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path("logout/", LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path("register/", SignUpView.as_view(), name='register'),
]