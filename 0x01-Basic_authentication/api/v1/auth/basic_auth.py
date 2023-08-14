#!/usr/bin/env python3
""" File that create a Basic Authentication Model
"""
from api.v1.auth.auth import Auth
import re


class BasicAuth(Auth):
    """
    Implementation of Basic Authentication Model

    Args:
        Auth (TypeVar('Auth')): the authentication model
    """
    pass
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        base64 authorization header

        Args:
            authorization_header (str): the string that start with basic.

        Returns:
            str: the base64 string
        """
        if not authorization_header or type(authorization_header) != str:
            return None

        fetched = re.search(r'Basic\s+(.*)', authorization_header)
        if fetched:
            return fetched.group(1)
        return None
