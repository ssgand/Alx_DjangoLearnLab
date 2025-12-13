from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

# class CustomUserManager(models.Manager):
#     def create_user(self, username, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(username=username, email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#     def create_superuser(self, username, email, password=None, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('bio', None)
#         extra_fields.setdefault('profile_photo', None)
#         return self.create_user(username, email, password, **extra_fields)

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
    # followers = models.ManyToManyField('self', symmetrical=False, related_name='following', blank=True)
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True
    )
    # objects = CustomUserManager()