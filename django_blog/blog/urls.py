from django.urls import path
# from .views import UserLoginView
from .views import login_user
from .views import logout_user
from .views import register
from .views import profile
from .views import home
from .views import posts

urlpatterns = [
    path('', home, name='home'),
    path('posts/', posts, name='posts'),
    # path('login/', UserLoginView.as_view(), name='login'),
    path('login/', login_user, name='login'),
    # path('logout/', UserLogoutView.as_view(), name='logout'),
    path('logout/', logout_user, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]