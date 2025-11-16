from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from .forms import BookForm
from bookshelf.forms import CustomUserCreationForm


def index(request):
    return HttpResponse("Welcome to my App.")

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
    form_class = CustomUserCreationForm                # UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'

# class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = Book
#     fields = ['title', 'author']
#     template_name = 'relationship_app/book_form.html'
#     permission_required = 'relationship_app.can_add_book'
#     success_url = reverse_lazy('book_list')
    
#     def form_valid(self, form):
#         form.instance.created_by = self.request.user
#         return super().form_valid(form)
    
# class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = Book
#     fields = ['title', 'author']
#     template_name = 'relationship_app/book_form.html'
#     permission_required = 'relationship_app.can_change_book'
#     success_url = reverse_lazy('book_list')

# class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
#     model = Book
#     template_name = 'relationship_app/book_confirm_delete.html'
#     permission_required = 'relationship_app.can_delete_book'
#     success_url = reverse_lazy('book_list')

@login_required
@permission_required('relationship_app.can_add_book', raise_exception=True)
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "relationship_app/book_form.html", {"form": form})


@login_required
@permission_required('relationship_app.can_change_book', raise_exception=True)
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect("book_list")
    return render(request, "relationship_app/book_form.html", {"form": form})


@login_required
@permission_required('relationship_app.can_delete_book', raise_exception=True)
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "relationship_app/book_confirm_delete.html", {"book": book})