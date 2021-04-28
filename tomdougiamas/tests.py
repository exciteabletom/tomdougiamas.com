from datetime import datetime

from django.contrib.auth import models as auth_models
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from .models import BlogPost, BlogComment, Project


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

    def test_votes_not_negative(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 3),
            votes=-1,
        )

        with self.assertRaises(ValidationError):
            comment.full_clean()

    def test_not_older_than_post(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 1),
        )

        with self.assertRaises(ValidationError):
            comment.full_clean()

    def test_max_length(self):
        comment = BlogComment(
            author=self.user,
            comment_text="",
            blog=self.blog_post,
            pub_date=datetime(2021, 1, 3),
        )

        comment.comment_text = "".zfill(BlogComment.max_length + 1)

        with self.assertRaises(ValidationError):
            comment.full_clean()


class BlogPostTests(TestCase):
    def test_unique_slug(self):
        post0 = BlogPost(
            blog_title="asdf",
            blog_text="asdf",
            blog_summary="asdf",
            blog_slug="not_unique",
            pub_date=datetime.now(),
        )
        post1 = BlogPost(
            blog_title="asdf",
            blog_text="asdf",
            blog_summary="asdf",
            blog_slug="not_unique",
            pub_date=datetime.now(),
        )

        with self.assertRaises(IntegrityError):
            post0.save()
            post1.save()

    def test_title_not_null(self):
        post = BlogPost(
            blog_title="",
            blog_text="asdf",
            blog_summary="asdf",
            blog_slug="asdf",
            pub_date=datetime.now(),
        )

        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_text_not_null(self):
        post = BlogPost(
            blog_title="asdf",
            blog_text="",
            blog_summary="asdf",
            blog_slug="asdf",
            pub_date=datetime.now(),
        )

        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_summary_not_null(self):
        # Summary is allowed to be null
        post = BlogPost(
            blog_title="asdf",
            blog_text="asdf",
            blog_summary="",
            blog_slug="asdf",
            pub_date=datetime.now(),
        )

        post.full_clean()


class ProjectTests(TestCase):
    def test_title_not_too_long(self):
        project = Project(
            project_title="".zfill(51), project_description="asdfasdsadsad"
        )

        with self.assertRaises(ValidationError):
            project.full_clean()
