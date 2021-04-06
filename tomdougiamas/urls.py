from django.urls import path

from . import views

app_name = "tomdougiamas"
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("projects/", views.projects, name="projects"),
    path("links/", views.links, name="links"),
    path("blog/", views.blog_index, name="blog_index"),
    path("blog/<str:blog_slug>/", views.blog_post, name="blog_post"),
    path("blog/login/", views.login_view, name="login"),
    path("blog/logout/", views.logout_view, name="logout"),
]
