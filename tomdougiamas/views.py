from django.shortcuts import render

from .models import Project, Link

app_name = "tomdougiamas"


def index(request):
    project_items = reversed(Project.objects.order_by("project_date"))
    return render(request, "tomdougiamas/index.html", context={"projects": project_items, "links": Link.objects.all()})