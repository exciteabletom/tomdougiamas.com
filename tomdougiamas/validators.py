from django.core.exceptions import ValidationError


def validate_comment(comment):
    comment = comment.strip()
    if len(comment) == 0:
        return ValidationError("Comment cannot be empty")
