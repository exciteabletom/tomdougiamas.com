# Generated by Django 3.2 on 2021-07-29 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tomdougiamas", "0003_alter_project_project_title"),
    ]

    operations = [
        migrations.CreateModel(
            name="Link",
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
                ("title", models.TextField()),
                ("url", models.URLField()),
            ],
        ),
    ]
