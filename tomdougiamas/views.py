from datetime import datetime

from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import Http404, render, redirect
from django.urls import reverse
from ratelimit.decorators import ratelimit

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


@ratelimit(key="user", method="POST", rate="1/2m", block=True)
@ratelimit(key="header:x-real-ip", method="POST", rate="2/2m", block=True)
@login_required(redirect_field_name="")
def add_comment(request, blog_id):
    if request.method == "POST":
        user = request.user
        blog = BlogPost.objects.get(id=blog_id)
        text = request.POST.get("text")
        text = text.strip()

        comment = BlogComment.objects.create(
            blog=blog, author=user, comment_text=text, pub_date=datetime.now(), votes=0
        )

        try:
            comment.clean()
        except ValidationError as e:
            return HttpResponse(f"{e.message}", status=422)

        comment.save()

        # Send 201
        return HttpResponse(status=201)

    else:
        return HttpResponseNotFound()


@ratelimit(key="header:x-real-ip", method="POST", rate="6/m", block=True)
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
        register_enabled = bool(request.POST.get("register"))

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
            return redirect("tomdougiamas:blog_index")
        # Logging in
        else:
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("tomdougiamas:blog_index")
            else:  # redirect with error
                return login_error("Invalid credentials")
    else:
        raise Http404


@login_required(redirect_field_name="")
def logout_view(request):
    logout(request)
    return redirect("tomdougiamas:blog_index")
