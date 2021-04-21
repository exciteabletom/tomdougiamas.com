from django.conf import settings
from django.core.exceptions import MiddlewareNotUsed
from django.utils.encoding import DjangoUnicodeDecodeError
from django.utils.html import strip_spaces_between_tags as minify_html


# Adapted from: https://djangomango.com/blog/post-detail/stripping-whitespace-from-your-django-html-8b9c723a-02c1-49b4-be1a-190429a1d003/
class HTMLMinifyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

        if settings.DEBUG:
            raise MiddlewareNotUsed

    def __call__(self, request):
        response = self.get_response(request)

        if (
            response.has_header("Content-Type")
            and "text/html" in response["Content-Type"]
        ):

            try:
                response.content = minify_html(response.content.decode("utf-8").strip())
                response["Content-Length"] = str(len(response.content))

            except DjangoUnicodeDecodeError:
                pass

        return response
