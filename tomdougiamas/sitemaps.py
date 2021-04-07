from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .models import BlogPost


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return BlogPost.objects.order_by("pub_date")

    @staticmethod
    def lastmod(obj):
        return obj.pub_date


class StaticViewSitemap(Sitemap):
    changefreq = "monthly"

    @staticmethod
    def priority(item):
        if item == "tomdougiamas:index":
            return 1.0
        else:
            return 0.5

    def items(self):
        paths = [
            "index",
            "about",
            "projects",
            "links",
            "blog_index",
        ]

        paths = ["tomdougiamas:" + i for i in paths]
        return paths

    def location(self, item):
        return reverse(item)
