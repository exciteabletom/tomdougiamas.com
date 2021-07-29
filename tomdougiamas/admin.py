from django.contrib import admin

from .models import BlogPost, BlogComment, Project, Link

admin.site.register((BlogPost, BlogComment, Project, Link))
