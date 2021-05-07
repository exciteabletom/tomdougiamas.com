from django.contrib import admin

from .models import BlogPost, BlogComment, Project

admin.site.register((BlogPost, BlogComment, Project))
