from django.http import HttpResponse
from django.shortcuts import render

app_name = "tomdougiamas"


# Create your views here.
def index(request):
    return render(request, "tomdougiamas/index.html")


def about(request):
    return render(request, "tomdougiamas/about.html")


def projects(request):
    return render(request, "tomdougiamas/projects.html")


def links(request):
    return render(request, "tomdougiamas/links.html")
