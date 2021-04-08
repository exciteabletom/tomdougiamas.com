import time

from django.contrib.auth import models as auth_models
from django.core.exceptions import ValidationError
from django.db import models

# Create your models here.


class BlogPost(models.Model):
    blog_title = models.TextField(null=False)
    blog_summary = models.TextField(null=False)
    blog_text = models.TextField(null=False)
    blog_slug = models.SlugField(unique=True, null=False)
    pub_date = models.DateField("Date published", null=False)

    def __str__(self):
        return f"Blog: {self.blog_title}"

    def get_absolute_url(self):
        return f"/blog/{self.blog_slug}_{self.id}/"


class BlogComment(models.Model):
    max_length = 750
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=False)
    author = models.ForeignKey(auth_models.User, on_delete=models.PROTECT, null=False)
    comment_text = models.TextField(max_length=max_length, null=False)
    pub_date = models.DateField("Date published", null=False)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Blog Comment by {self.author} on '{self.blog.blog_title}': {self.comment_text[0:75]}"

    def clean(self):
        if time.mktime(self.pub_date.timetuple()) < time.mktime(self.blog.pub_date.timetuple()):
            raise ValidationError("A comment cannot be newer than a post.")

        if self.votes < 0:
            raise ValidationError("Votes cannot be negative.")

        if len(self.comment_text) > self.max_length:
            raise ValidationError("Message too long")




