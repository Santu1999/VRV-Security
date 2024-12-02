from flask_jwt_extended import verify_jwt_in_request, get_jwt
from flask import jsonify
from functools import wraps

def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        try:
            verify_jwt_in_request()
            return f(*args, **kwargs)
        except Exception as e:
            return jsonify({"message": "Unauthorized"}), 401
    return wrapper

def authorize_roles(*roles):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            claims = get_jwt()
            if "role" in claims and claims["role"] in roles:
                return f(*args, **kwargs)
            return jsonify({"message": "Forbidden"}), 403
        return wrapper
    return decorator
