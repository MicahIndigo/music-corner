"""
Admin registrations for blog models.
"""


from django.contrib import admin
from .models import Category, Post, Comment, Vote

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Vote)
