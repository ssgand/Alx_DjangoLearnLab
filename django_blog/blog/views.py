from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib import messages
from .forms import RegisterForm, ProfileUpdateForm
from.models import Post
from .models import Comment
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .forms import PostForm
from .forms import CommentForm


# --- LOGIN VIEW ---
# class UserLoginView(LoginView):
    # template_name = 'blog/login.html'

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'blog/login.html')


# --- LOGOUT VIEW ---
# class UserLogoutView(LogoutView):
#     template_name = 'blog/logout.html'

def logout_user(request):
    logout(request)
    return redirect('login')


# --- REGISTRATION / SIGNUP ---
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created successfully! You can now log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form': form})


# --- PROFILE VIEW (VIEW + EDIT PROFILE) ---
@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, "Your profile has been updated successfully!")
            return redirect('profile')
    else:
        form = ProfileUpdateForm(instance=request.user)

    return render(request, 'blog/profile.html', {'form': form})

def home(request):
    return render(request, "blog/home.html")

def posts(request):
    return render(request, "blog/posts.html")

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'   # template path
    context_object_name = 'posts'
    paginate_by = 10  # optional pagination

# Show a single post (public)
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

# Create a new post — only for authenticated users
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # assign the author as the current user before saving
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Post created successfully.")
        return response

# Update a post — only the author may update
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        # Shouldn't need to reassign author — keep existing author
        messages.success(self.request, "Post updated successfully.")
        return super().form_valid(form)

    def test_func(self):
        # allow only the author to update
        post = self.get_object()
        return post.author == self.request.user

# Delete a post — only the author may delete
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('posts')  # redirect to posts list after deletion

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Post deleted.")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user
    

# Create a comment on a post (POST only — displays form on post detail template)
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'  # used only if you want a standalone page

    def form_valid(self, form):
        post_pk = self.kwargs.get('post_pk')
        post = get_object_or_404(Post, pk=post_pk)
        form.instance.post = post
        form.instance.author = self.request.user
        response = super().form_valid(form)
        messages.success(self.request, "Comment posted.")
        # Redirect back to the post detail page
        return redirect(post.get_absolute_url())
    
    def get_success_url(self):
        return reverse("post-detail", kwargs={'pk': self.kwargs['post_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # optionally add post to template context
        context['post'] = get_object_or_404(Post, pk=self.kwargs.get('post_pk'))
        return context

# Edit an existing comment — only the comment author
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Comment updated.")
        return redirect(self.object.post.get_absolute_url())

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

# Delete a comment — only the comment author
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Comment deleted.")
        return super().delete(request, *args, **kwargs)

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user
