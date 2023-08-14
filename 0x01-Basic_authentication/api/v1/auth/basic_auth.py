#!/usr/bin/env python3
""" File that create a Basic Authentication Model
"""
from api.v1.auth.auth import Auth
from models.user import User
import re
import base64
from typing import TypeVar


class BasicAuth(Auth):
    """
    Implementation of Basic Authentication Model

    Args:
        Auth (TypeVar('Auth')): the authentication model
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        base64 authorization header

        Args:
            authorization_header (str): the string that start with basic.

        Returns:
            str: the base64 string extracted
        """
        if not authorization_header or type(authorization_header) != str:
            return None

        fetched = re.search(r'Basic\s+(.*)', authorization_header)
        if fetched:
            return fetched.group(1)
        return None

    def decode_base64_authorization_header(self,
                                           base64_authorization_header: str
                                           ) -> str:
        """
        decode base64 authorization header

        Args:
            base64_authorization_header (str): the encoded string

        Returns:
            str: the decoded string
        """
        encoded = base64_authorization_header
        if not encoded or type(encoded) != str:
            return None
        try:
            data: bytes = base64.b64decode(base64_authorization_header)
            decoded_data: str = data.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
        return decoded_data

    def extract_user_credentials(self,
                                 decoded_base64_authorization_header: str
                                 ) -> (str, str):
        """
        return a tuple containing the username and password

        Args:
            decoded_base64_authorization_header (str): the decoded string.

        Returns:
            (str, str): (username, password)
        """
        decoded = decoded_base64_authorization_header
        if not decoded or type(decoded) != str or ":" not in decoded:
            return None, None
        return tuple(decoded.split(":"))

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        return the user object gotten from the provided params

        Args:
            user_email (str): user email
            user_pwd (str): user password

        Returns:
            TypeVar('User'): the user object
        """
        if not user_email or not user_pwd:
            return None

        if type(user_email) != str or type(user_pwd) != str:
            return None

        database = User.search()
        if len(database) == 0:
            user = User()
            user.email = user_email
            user.password = user_pwd
            user.save()
            return user

        for user in database:
            if user.email == user_email:
                if user.is_valid_password(user_pwd):
                    return user
        return None
