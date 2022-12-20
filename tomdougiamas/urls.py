from django.urls import path

from . import views

app_name = "tomdougiamas"
urlpatterns = [
    path("", views.index, name="index"),
]
