#!/usr/bin/env python3
"""
    A basic flask app
"""
from flask import Flask, jsonify, request, abort, redirect
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
            return jsonify({"email": email,
                            "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login():
    """
    log into an existing account
    """
    email: str = request.form.get("email")
    password: str = request.form.get("password")

    if AUTH.valid_login(email, password):
        sess_id = AUTH.create_session(email)
        response = jsonify({"email": email, "message": "logged in"})
        response.set_cookie("session_id", sess_id)
        return response

    abort(401)


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout from the current account.
    """
    sess_id = request.cookies.get("session_id")
    user = AUTH.get_user_from_session_id(sess_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')

    abort(403)


@app.route('/profile', strict_slashes=False)
def profile():
    """
    fetch the user data
    """
    sess_id = request.cookies.get("session_id")
    if not sess_id:
        abort(403)

    user = AUTH.get_user_from_session_id(sess_id)
    if user:
        return jsonify({"email": user.email})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
