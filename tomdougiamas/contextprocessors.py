def current_username(request):
    user = request.user
    username = ""
    if user.is_authenticated:
        username = user.get_username

    return {"username": username}
