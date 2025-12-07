from django.urls import path
# from .views import UserLoginView
from .views import login_user
from .views import logout_user
from .views import register
from .views import profile
from .views import home
from .views import posts
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, search_posts, posts_by_tag

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('login/', login_user, name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('post/', PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path("search/", search_posts, name="search_posts"),
    path("tag/<str:tag_name>/", posts_by_tag, name="posts_by_tag"),
]