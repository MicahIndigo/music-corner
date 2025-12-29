"""
Views for Music Corner.

- Post list + post detail
- Post CRUD(login required)
"""


from django.contrib import messages
from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum


from .forms import CommentForm, PostForm
from .models import Comment, Post, Vote


def register(request):
    """
    Register a new user account.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})


def post_list(request: HttpRequest) -> HttpResponse:
    """Homepage: List of latest blog posts."""
    posts = (
        Post.objects.select_related("category", "author")
        .annotate(score=Sum("votes__value"))
        .all()
        )
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Post detail page:
    - show post conten
    - show comments
    - add comment form
    """
    post = get_object_or_404(
        Post.objects.select_related("category", "author"), pk=pk)
    score = post.votes.aggregate(total=Sum("value"))["total"] or 0
    comments = post.comments.select_related("author").all()

    comment_form = CommentForm()
    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_form": comment_form,
            "score": score,
        },
    )


@login_required
def post_create(request: HttpRequest) -> HttpResponse:
    """
    Create a new post.
    (logged-in users only)
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Post created successfully.")
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm()

    return render(
        request,
        "blog/post_form.html",
        {"form": form, "mode": "create"},
    )


@login_required
def post_update(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Edit an existing post.
    (Authors only)
    """
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(
            request, "You do not have permission to edit this post.")
        return redirect("blog:post_detail", pk=post.pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("blog:post_detail", pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(
        request,
        "blog/post_form.html",
        {"form": form, "mode": "edit", "post": post},
    )


@login_required
def post_delete(request: HttpRequest, pk: int) -> HttpResponse:
    """
    Delete a post.
    (Author only)
    """
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(
            request, "You do not have permission to delete this post."
        )
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
        messages.error(
            request, "You do not have permission to delete this comment."
        )
        return redirect("blog:post_detail", pk=post_pk)

    if request.method == "POST":
        comment.delete()
        messages.success(request, "Comment deleted.")
    return redirect("blog:post_detail", pk=post_pk)


@login_required
def post_vote(request: HttpRequest, pk: int, value: int) -> HttpResponse:
    """
    Upvote/downvote a post.
    value should be 1 (upvote) or -1 (downvote).
    """
    post = get_object_or_404(Post, pk=pk)

    # Ensure value is either 1 or -1
    if value not in (1, -1):
        return redirect("blog:post_detail", pk=post.pk)

    vote, created = Vote.objects.get_or_create(
        post=post,
        user=request.user,
        defaults={"value": value},
    )

    # If the vote already exists, update it
    if not created and vote.value != value:
        vote.value = value
        vote.save()

    # If they clicked the same vote again, remove it
    elif not created and vote.value == value:
        vote.delete()

    return redirect("blog:post_detail", pk=post.pk)
