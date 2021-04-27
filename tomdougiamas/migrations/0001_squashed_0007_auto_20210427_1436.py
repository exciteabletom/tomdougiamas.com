# Generated by Django 3.2 on 2021-04-27 14:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    replaces = [
        ("tomdougiamas", "0001_squashed_0017_alter_blogcomment_pub_date"),
        ("tomdougiamas", "0002_auto_20210406_2059"),
        ("tomdougiamas", "0003_auto_20210421_0308"),
        ("tomdougiamas", "0004_project"),
        ("tomdougiamas", "0005_auto_20210422_0231"),
        ("tomdougiamas", "0004_auto_20210427_1137"),
        ("tomdougiamas", "0006_merge_0004_auto_20210427_1137_0005_auto_20210422_0231"),
        ("tomdougiamas", "0007_auto_20210427_1436"),
    ]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("blog_title", models.TextField()),
                ("pub_date", models.DateField(verbose_name="Date published")),
                ("blog_summary", models.TextField()),
                ("blog_slug", models.SlugField(unique=True)),
                ("blog_text", tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name="BlogComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("comment_text", models.TextField(max_length=750)),
                ("votes", models.IntegerField(default=0)),
                (
                    "blog",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="tomdougiamas.blogpost",
                    ),
                ),
                ("pub_date", models.DateField(verbose_name="Date published")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("project_title", models.CharField(max_length=50)),
                ("project_description", tinymce.models.HTMLField()),
            ],
        ),
    ]
