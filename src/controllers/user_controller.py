def create_user(request):
    data = request.get_json()
    name = data.get('name')
    return {
        "message": "User created successfully",
        "name": name
    }, 201
