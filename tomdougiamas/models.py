from django.contrib.auth import models as auth_models
from django.db import models


# Create your models here.
class BlogPost(models.Model):
    blog_title = models.TextField()
    blog_summary = models.TextField()
    blog_text = models.TextField()
    blog_slug = models.SlugField(unique=True)
    pub_date = models.DateField("Date published")

    def __str__(self):
        return f"Blog: {self.blog_title}"

    def get_absolute_url(self):
        return f"/blog/{self.blog_slug}_{self.id}/"


class BlogComment(models.Model):
    blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(auth_models.User, on_delete=models.PROTECT)
    comment_text = models.TextField(max_length=750)
    pub_date = models.DateField("Date published")
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"Blog Comment by {self.author} on '{self.blog.blog_title}': {self.comment_text[0:75]}"
