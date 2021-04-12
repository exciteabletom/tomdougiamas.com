from django.core.exceptions import ValidationError

from .models import BlogComment


def validate_comment(comment):
    comment = comment.strip()
    if len(comment) == 0:
        return ValidationError("Comment cannot be empty")

    if len(comment) > BlogComment.max_length:
        return ValidationError("Comment too long!")
