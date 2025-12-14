from rest_framework.routers import DefaultRouter
from .views import PostViewSet
from .views import CommentViewSet
from django.urls import path
from .views import FeedView
from .views import LikePostView
from .views import UnlikePostView

router = DefaultRouter()
# router.register(r"posts", PostViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("feed/", FeedView.as_view(), name="feed"),
    path("posts/<int:pk>/like/", LikePostView.as_view(), name="post-like"),
    path("posts/<int:pk>/unlike/", UnlikePostView.as_view(), name="post-unlike"),
]
