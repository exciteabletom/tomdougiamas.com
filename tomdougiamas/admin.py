from django.contrib import admin

from .models import BlogPost, BlogComment, Project

# Register your models here.

admin.site.register((BlogPost, BlogComment, Project))
