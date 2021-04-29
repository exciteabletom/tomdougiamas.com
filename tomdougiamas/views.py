from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse

# noinspection PyPackageRequirements
from ratelimit.decorators import ratelimit

from .forms import LoginForm, CommentForm
from .models import BlogPost, BlogComment, Project

app_name = "tomdougiamas"


def index(request):

    return render(request, "tomdougiamas/index.html")


def about(request):
    return render(request, "tomdougiamas/about.html")


def projects(request):
    project_items = Project.objects.all()

    return render(
        request, "tomdougiamas/projects.html", context={"projects": project_items}
    )


def links(request):
    return render(request, "tomdougiamas/links.html")


def blog_index(request):
    latest_blog_posts = reversed(BlogPost.objects.order_by("pub_date"))
    posts_exist = BlogPost.objects.count() > 0
    context = {"latest_blog_posts": latest_blog_posts, "posts_exist": posts_exist}

    return render(request, "tomdougiamas/blog_index.html", context)


def blog_post(request, blog_slug, blog_id):
    blog = BlogPost.objects.get(blog_slug=blog_slug)
    comments = BlogComment.objects.filter(blog_id=blog_id).order_by("pub_date")
    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        user = request.user

        if form.is_valid() and user.is_authenticated:
            comment_text = form.cleaned_data.get("comment")
            comment_text = comment_text.strip()

            comment = BlogComment.objects.create(
                blog=blog,
                author=user,
                comment_text=comment_text,
                pub_date=datetime.now(),
                votes=0,
            )
            try:
                comment.full_clean()
            except ValidationError as e:
                form.add_error(None, e)
            else:  # All form data validated
                comment.save()
                return redirect(
                    reverse("tomdougiamas:blog_post", args=[blog_slug, blog_id])
                )

    return render(
        request,
        "tomdougiamas/blog_post.html",
        {
            "blog": blog,
            "comments": comments,
            "form": form,
        },
    )


@ratelimit(key="user", method="POST", rate="2/m", block=True)
@ratelimit(key="header:x-real-ip", method="POST", rate="2/m", block=True)
@login_required(redirect_field_name="")
def add_comment(request, blog_id):
    if request.method == "POST":
        user = request.user
        blog = BlogPost.objects.get(id=blog_id)
        text = request.POST.get("text")
        text = text.strip()

        form = CommentForm(request)

        comment = BlogComment.objects.create(
            blog=blog, author=user, comment_text=text, pub_date=datetime.now(), votes=0
        )

        try:
            comment.full_clean()
            if not form.is_valid():
                raise ValidationError
        except ValidationError as e:
            return HttpResponse(f"{e.message}", status=422)

        comment.save()

        # Send 201
        return HttpResponse(status=201)

    else:
        return HttpResponseNotFound()


@ratelimit(key="header:x-real-ip", method="POST", rate="60/h", block=True)
def login_view(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            return redirect("tomdougiamas:blog_index")

        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            register_enabled = form.cleaned_data.get("register_enabled")

            if register_enabled:
                if not User.objects.filter(username=username):
                    user = User.objects.create_user(
                        username=username, password=password
                    )
                    user.save()

                    login(request, user)
                    return redirect("tomdougiamas:blog_index")

                else:
                    form.add_error("username", "Username already taken")

            # Logging in
            else:
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    return redirect("tomdougiamas:blog_index")
                else:
                    form.add_error(None, "Invalid credentials")

    else:
        form = LoginForm()

    return render(request, "tomdougiamas/login.html", context={"form": form})


@login_required(redirect_field_name="")
def logout_view(request):
    logout(request)
    return redirect("tomdougiamas:blog_index")
