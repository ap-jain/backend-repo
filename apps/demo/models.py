from django.db import models
from django.contrib.auth.models import User
import uuid


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class User(models.Model):
    id = models.AutoField(primary_key=True)  
    password = models.CharField(max_length=128)  
    last_login = models.DateTimeField(null=True, blank=True)  
    is_superuser = models.BooleanField(default=False)  
    username = models.CharField(max_length=150, unique=True) 
    last_name = models.CharField(max_length=150) 
    email = models.EmailField(max_length=254)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True) 
    date_joined = models.DateTimeField(auto_now_add=True)  
    first_name = models.CharField(max_length=150)  