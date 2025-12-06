from django.urls import path
# from .views import UserLoginView
from .views import login_user
from .views import logout_user
from .views import register
from .views import profile
from .views import home
from .views import posts
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('login/', login_user, name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('posts/new/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]