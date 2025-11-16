from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("list/", views.book_list, name="book_list"),
    path('create/', views.book_create, name='create_book'),
    path('edit/<int:pk>/', views.book_update, name='edit_book'), # edit_book/
    path('delete/<int:pk>/', views.book_delete, name='delete_book'),
]
