def get_navbar(request):

    role_id = request.session.get('role_id', False)
    role_page = request.session.get('role_page', False)

    return {
        "navbar": {}
    }
