#!/usr/bin/env python3
""" Session authentication viewa
"""
from flask import jsonify, abort, request
from api.v1.views import app_views
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'])
def session_login():
    email = request.form.get('email')
    password = request.form.get('password')
    if not email:
        return jsonify({ "error": "email missing" }), 400
    if not password:
        return jsonify({ "error":"password missing" }), 400

    try:
        database = User.search()
        if len(database) == 0:
            return jsonify({ "error": "no user found for this email" }), 400

        for user in database:
            if user.email == email:
                if not user.is_valid_password(password):
                    return jsonify({ "error": "wrong password" }), 401
                else:
                    from api.v1.app import auth
                    from os import getenv

                    sess_id = auth.create_session(user.id)
                    user_data = jsonify(user.to_json())
                    user_data.set_cookie(getenv('SESSION_NAME'), sess_id)
                    return user_data

        return jsonify({ "error": "no user found for this email" }), 400
    except Exception:
        return None
