from datetime import datetime

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.contrib.auth import models as auth_models

from .models import BlogPost, BlogComment


# Create your tests here.


class BlogCommentTests(TestCase):
    def setUp(self):
        self.user = auth_models.User(username="test", password="testing123!")
        self.blog_post = BlogPost(
            blog_title="",
            blog_slug="",
            blog_text="",
            blog_summary="",
            pub_date=datetime(2021, 1, 2),
        )

    def test_comment_clean_method_votes_not_negative(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 3),
            votes=-1,
        )

        with self.assertRaises(ValidationError):
            comment.clean()

    def test_comment_clean_method_not_newer_than_post(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 1),
        )

        with self.assertRaises(ValidationError):
            comment.clean()

    def test_comment_clean_method_text_not_too_long(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 3),
        )

        comment.comment_text = "".zfill(BlogComment.max_length + 1)

        with self.assertRaises(ValidationError):
            comment.full_clean()