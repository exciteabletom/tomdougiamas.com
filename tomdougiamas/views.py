from django.contrib.auth import logout, authenticate, login
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


def blog_post(request, blog_slug):
    blog = BlogPost.objects.get(blog_slug=blog_slug)
    blog_id = blog.id
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
        username = request.POST.get("username")
        password = request.POST.get("password")

        if len(username) > 30:
            return login_error("Username too long")

        if len(password) > 100:
            return login_error("Password too long")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
        if login_helper(request):  # If login successful
            return redirect(reverse("tomdougiamas:blog_index"))
        else:  # redirect with error
            return login_error("Invalid credentials")
    else:
        raise Http404


def logout_view(request):
    logout(request)
    return redirect(reverse("tomdougiamas:blog_index"))
