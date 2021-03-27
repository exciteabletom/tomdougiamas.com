from django.http import HttpResponse
from django.shortcuts import render

app_name = "tomdougiamas"

# Create your views here.
def index(request):
    return render(request, "tomdougiamas/index.html")
