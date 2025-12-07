from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone
from taggit.managers import TaggableManager
from django.shortcuts import render

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = TaggableManager(blank=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']   # newest first

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Used by generic views to redirect to detail after create/update
        return reverse('post-detail', kwargs={'pk': self.pk})
class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # safe for migrations
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_at']  # oldest-first in the context of a single post

    def __str__(self):
        return f'Comment by {self.author.username} on {self.post.title}'

    def get_edit_url(self):
        return reverse('comment-update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('comment-delete', kwargs={'pk': self.pk})
    
def search_posts(request):
    q = request.GET.get("q", "")

    results = Post.objects.filter(
        Q(title__icontains=q) |
        Q(content__icontains=q) |
        Q(tags__name__icontains=q)
    ).distinct()

    return render(request, "search_results.html", {"results": results, "q": q})
    
def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name__in=[tag_name]).distinct()
    return render(request, "posts_by_tag.html", {"posts": posts, "tag_name": tag_name})


