from datetime import datetime

from django.test import TestCase
from django.contrib.auth import models as auth_models

from .models import BlogPost, BlogComment

# Create your tests here.

class BlogTests(TestCase):
    def test_comment_not_older_than_post(self):
        post = BlogPost(blog_title="", blog_slug="", blog_text="", blog_summary="", pub_date=datetime(2021, 1, 2))

        comment = BlogComment(author=auth_models.User(username="test", password="testing123!"),
                              comment_text="", blog=post, pub_date=datetime(2021, 1, 1))



