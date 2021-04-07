from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseServerError
from django.shortcuts import Http404, render, redirect
from django.urls import reverse

from .models import BlogPost, BlogComment

app_name = "tomdougiamas"


def index(request):
    return render(request, "tomdougiamas/index.html")


def about(request):
    return render(request, "tomdougiamas/about.html")


def projects(request):
    return render(request, "tomdougiamas/projects.html")


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
    context = {
        "blog": blog,
        "comments": comments,
    }

    return render(request, "tomdougiamas/blog_post.html", context)


def login_view(request):
    def login_error(message):
        return render(request, "tomdougiamas/login.html", context={"error": message})

    if request.method == "GET":
        return render(request, "tomdougiamas/login.html")
    elif request.method == "POST":
        if request.user.is_authenticated:
            return login_error(f"{request.user.username} you are already logged in!")

        username = request.POST.get("username")
        password = request.POST.get("password")
        register_enabled = request.POST.get("register") == "on"

        if len(username) > 30:
            return login_error("Username too long")

        if len(password) > 100:
            return login_error("Password too long")

        if register_enabled:
            if User.objects.filter(username=username).exists():
                return login_error("User already exists")

            try:
                validate_password(password)
            except ValidationError as e:
                return login_error(" ".join(e.messages))

            user = User.objects.create_user(username=username, password=password)
            user.save()

            login(request, user)
            return redirect(reverse("tomdougiamas:blog_index"))
        # Logging in
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect(reverse("tomdougiamas:blog_index"))
            else:  # redirect with error
                return login_error("Invalid credentials")
    else:
        raise Http404


def logout_view(request):
    logout(request)
    return redirect(reverse("tomdougiamas:blog_index"))


def add_comment(request, blog_id):
    if request.method == "POST" and request.user.is_authenticated:
        user = request.user
        blog = BlogPost.objects.get(id=blog_id)
        text = request.POST.get("text")

        if len(text) > 750:
            return HttpResponseServerError()

        comment = BlogComment.objects.create(
            blog=blog, author=user, comment_text=text, pub_date=datetime.now(), votes=0
        )
        comment.save()
        return redirect(blog)

    else:
        return HttpResponseForbidden
    pass
