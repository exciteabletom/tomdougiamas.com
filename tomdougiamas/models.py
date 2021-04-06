from django.db import models


# Create your models here.
class BlogPost(models.Model):
    blog_title = models.TextField()
    blog_summary = models.TextField()
    blog_text = models.TextField()
    blog_slug = models.SlugField()
    pub_date = models.DateField("Date published")


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.TextField(max_length=30)
    comment_text = models.TextField(max_length=500)
    pub_date = models.DateField("Date published", null=True)
    votes = models.IntegerField(default=0)
