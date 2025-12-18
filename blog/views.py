"""
Views for Music Corner.

- Post list + post detail
- Post CRUD(login required)
"""


from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render


from .forms import CommentForm, PostForm
from .models import Comment, Post


def post_list(request: HttpRequest) -> HttpResponse:
    """Homepage: List of latest blog posts."""
    posts = Post.objects.select_related("category", "author").all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Post detail page:
    - show post conten
    - show comments
    - add comment form
    """
    post = get_object_or_404(Post.objects.select_related("category", "author"), pk=pk)
    comments = post.comments.select_related("author").all()

    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {"post": post, "comments": comments, "comment_form": comment_form},
    )


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    """
    Create a new post.
    (logged-in users only)
    """
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully.")
        return redirect("blog:post_list")
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, "blog/post_form.html", {"form": form, "mode": "create"})


@login_required
def post_update(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Edit an existing post.
    (Authors only)
    """
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, "You do not have permission to edit this post.")
        return redirect("blog:post_detail", pk=post.pk)
    
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)
    
    return render(request, "blog/post_form.html", {"form": form, "mode": "edit", "post": post})


@login_required
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Delete a post.
    (Author only)
    """
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, "You do not have permission to delete this post.")
        return redirect("blog:post_detail", pk=post.pk)
    
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("blog:post_list")
    
    return render(request, "blog/post_confirm_delete.html", {"post": post})


@login_required
def comment_create(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Add a comment to a post.
    (logged-in users only)
    """
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            c = form.save(commit=False)
            c.author = request.user
            c.post = post
            c.save()
            messages.success(request, "Comment added.")
    return redirect("blog:post_detail", pk=post.pk)


@login_required
def comment_delete(request: HttpRequest, comment_id: int) -> HttpResponse:
    """
    Delete a comment.
    (Comment author only)
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    post_pk = comment.post.pk

    if comment.author != request.user:
        messages.error(request, "You do not have permission to delete this comment.")
        return redirect("blog:post_detail", pk=post_pk)
    
    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted.")
    return redirect("blog:post_detail", pk=post_pk)
