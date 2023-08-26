#!/usr/bin/env python3
"""
    A basic flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def home():
    """
    Flask home page
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=["POST"], strict_slashes=False)
def users():
    """
    register a new user in the database
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")

    try:
        new_user = AUTH.register_user(email, password)
        if new_user:
            return jsonify({"email": "<registered email>",
                            "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
