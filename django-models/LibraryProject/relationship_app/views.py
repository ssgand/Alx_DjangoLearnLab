from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

class list_books(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    # context_object_name = 'book'

class register(CreateView):
    form_class = UserCreationForm                # UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

@user_passes_test(lambda user: user.userprofile.role == 'ADMIN')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html', {})