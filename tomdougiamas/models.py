from django.db import models


# Create your models here.


class BlogPost(models.Model):
    blog_title = models.TextField()
    blog_text = models.TextField()
    pub_date = models.DateTimeField("Date published")


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    comment_text = models.TextField()
    pub_date = models.DateTimeField("Date published", null=True)
    votes = models.IntegerField(default=0)
