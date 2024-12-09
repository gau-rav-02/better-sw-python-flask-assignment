from flask import request, jsonify

def token_required(func):
    def wrapper(*args, **kwargs):
        token = request.headers.get("Authorization")
        if token != "Bearer your_secret_token":
            return jsonify({"error": "Unauthorized"}), 401
        return func(*args, **kwargs)
    return wrapper
