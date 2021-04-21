import django.contrib.sitemaps.views as sitemap_views
from django.urls import path

from . import sitemaps
from . import views

app_name = "tomdougiamas"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("links/", views.links, name="links"),
    path("blog/", views.blog_index, name="blog_index"),
    path(
        "sitemap-<section>.xml",
        sitemap_views.sitemap,
        {"sitemaps": sitemaps},
        name="sitemaps",
    ),
    path("blog/login/", views.login_view, name="login"),
    path("blog/logout/", views.logout_view, name="logout"),
    path("blog/addcomment/<int:blog_id>/", views.add_comment, name="add_blog_comment"),
    path("blog/<str:blog_slug>_<int:blog_id>/", views.blog_post, name="blog_post"),
]
