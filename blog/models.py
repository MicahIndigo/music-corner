"""
Database models for Music Corner.


Entities:
- Category: groups posts by topic/genre.
- Post: main content users create and read.
- Comment: user replies on posts.

Relationships:
- Post -> User (author)
- Post -> Category (topic/genre)
- Comment -> Post
- Comment -> User (author)
"""


from django.conf import settings
from django.db import models


user = settings.AUTH_USER_MODEL


class Category(models.Model):
    """
    A topic/genre grouping for posts.
    (e.g. Hip-Hop, Reviews, Interviews)
    """
    name = models.CharField(max_length=60, unique=True)

    class Meta:
        ordering = ["name"]   

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    """
    A user-created post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="posts"
    )
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        related_name="posts"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
    
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    A comment made by a user on a post
    """
    post = models.ForeignKey(
        Post, 
        on_delete=models.CASCADE, 
        related_name="comments"
        )
    author = models.ForeignKey(
        user,
        on_delete=models.CASCADE,
        related_name="comments"
        )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]
    
    def __str__(self) -> str:
        return f"comment by {self.author} on {self.post}"
