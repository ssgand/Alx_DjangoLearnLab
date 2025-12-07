from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post
from .models import Comment
from taggit.forms import TagWidget


# Registration Form with Email Field
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Profile Update Form
class ProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Post title', 'required': True}),
            'content': forms.Textarea(attrs={'placeholder': 'Write your post here...', 'rows': 8}),
            "tags": TagWidget(),
        }
class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        max_length=2000,
        help_text='Max length: 2000 characters'
    )

    class Meta:
        model = Comment
        fields = ['content']
