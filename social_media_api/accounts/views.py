from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate

from .models import User
from .serializers import RegisterSerializer, UserSerializer
# from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from accounts.models import User as CustomUser
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)
        if not user:
            return Response({"error": "Invalid credentials"}, status=400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({"token": token.key})
    

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    # def post(self, request, user_id):
    #     user_to_follow = get_object_or_404(User, id=user_id)

    #     if user_to_follow == request.user:
    #         return Response({"error": "You cannot follow yourself"}, status=400)

    #     request.user.following.add(user_to_follow)
    #     return Response({"message": f"You are now following {user_to_follow.username}"})

    # 👇 Base queryset
    queryset = CustomUser.objects.all() # above is valid just trying to use this option

    def post(self, request, user_id):
        user_to_follow = get_object_or_404(self.get_queryset(), id=user_id)

        if user_to_follow == request.user:
            return Response(
                {"detail": "You cannot follow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        request.user.following.add(user_to_follow)

        return Response(
            {"detail": f"You are now following {user_to_follow.username}"},
            status=status.HTTP_200_OK
        )


class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    # def post(self, request, user_id):
    #     user_to_unfollow = get_object_or_404(User, id=user_id)

    #     request.user.following.remove(user_to_unfollow)
    #     return Response({"message": f"You unfollowed {user_to_unfollow.username}"})
    queryset = CustomUser.objects.all() # above is valid just trying to use this option

    def post(self, request, user_id):
        user_to_unfollow = get_object_or_404(self.get_queryset(), id=user_id)

        request.user.following.remove(user_to_unfollow)

        return Response(
            {"detail": f"You unfollowed {user_to_unfollow.username}"},
            status=status.HTTP_200_OK
        )
