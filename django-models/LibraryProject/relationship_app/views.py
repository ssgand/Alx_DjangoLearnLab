from django.shortcuts import render, redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse

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

class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    permission_required = 'relationship_app.can_add_book'
    success_url = reverse_lazy('book_list')
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
    
class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    fields = ['title', 'author']
    template_name = 'relationship_app/book_form.html'
    permission_required = 'relationship_app.can_change_book'
    success_url = reverse_lazy('book_list')

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Book
    template_name = 'relationship_app/book_confirm_delete.html'
    permission_required = 'relationship_app.can_delete_book'
    success_url = reverse_lazy('book_list')