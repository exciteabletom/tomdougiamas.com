# Generated by Django 3.2 on 2021-04-28 03:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tomdougiamas", "0001_squashed_0007_auto_20210427_1436"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="blog_summary",
            field=models.TextField(blank=True),
        ),
    ]
