"""
Forms for creating and editing posts and comments
"""

from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):
    """
    Form for creating/editing a Post.
    """
    class Meta:
        model = Post
        fields = ["title", "content", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(
                attrs={"class": "form-control", "rows": 6}
            ),
            "category": forms.Select(attrs={"class": "form-select"}),
        }
    

class CommentForm(forms.ModelForm):
    """
    Form for adding a comment to posts.
    """
    class Meta:
        model = Post
        fields = ["content"]
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 3,
                    "placeholder": "write a comment...",
                }
            ),
        }
