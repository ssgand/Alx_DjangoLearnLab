# from django.shortcuts import render

# # Create your views here.

# from rest_framework import generics, permissions
# from .models import Book
# from .serializers import BookSerializer


# # --- LIST VIEW (GET all books) ---
# class BookListView(generics.ListAPIView):
#     """
#     Returns a list of all books.
#     Accessible by anyone (read-only permission).
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]


# # --- DETAIL VIEW (GET single book) ---
# class BookDetailView(generics.RetrieveAPIView):
#     """
#     Retrieve a single book by its ID.
#     Accessible by anyone.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.AllowAny]


# # --- CREATE VIEW (POST new book) ---
# class BookCreateView(generics.CreateAPIView):
#     """
#     Create a new book instance.
#     Only authenticated users can create.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_create(self, serializer):
#         # Customize creation if needed (example: assign owner)
#         serializer.save()
#         # You can do extra logic here


# # --- UPDATE VIEW (PUT/PATCH existing book) ---
# class BookUpdateView(generics.UpdateAPIView):
#     """
#     Update an existing book.
#     Only authenticated users can update.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]

#     def perform_update(self, serializer):
#         # Custom update behavior
#         serializer.save()


# # --- DELETE VIEW (DELETE book) ---
# class BookDeleteView(generics.DestroyAPIView):
#     """
#     Delete a book by ID.
#     Only authenticated users can delete.
#     """
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     permission_classes = [permissions.IsAuthenticated]
