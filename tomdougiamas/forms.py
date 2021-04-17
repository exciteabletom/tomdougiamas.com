from django import forms
from django.contrib.auth.password_validation import validate_password

from .validators import validate_comment


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    password = forms.CharField(
        label="Password",
        max_length=100,
        widget=forms.PasswordInput,
        validators=[validate_password],
    )
    register_enabled = forms.BooleanField(label="Register a new user", required=False)


class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=750,
        min_length=1,
        validators=[validate_comment],
        widget=forms.Textarea(
            attrs={"placeholder": "Write a comment", "aria-label": "Write a comment"}
        ),
    )
