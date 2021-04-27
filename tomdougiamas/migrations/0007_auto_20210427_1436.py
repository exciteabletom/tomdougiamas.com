# Generated by Django 3.2 on 2021-04-27 14:36

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ("tomdougiamas", "0006_merge_0004_auto_20210427_1137_0005_auto_20210422_0231"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="blog_text",
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name="project",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
        migrations.AlterField(
            model_name="project",
            name="project_description",
            field=tinymce.models.HTMLField(),
        ),
    ]
