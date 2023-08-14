#!/usr/bin/env python3
""" File that create a Basic Authentication Model
"""
from api.v1.auth.auth import Auth
import re
import base64


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

    def decode_base64_authorization_header(
        self, base64_authorization_header: str) -> str:
        """
        decode base64 authorization header

        Args:
            base64_authorization_header (str): the encoded string

        Returns:
            str: the decoded string
        """
        if not base64_authorization_header or type(
            base64_authorization_header) != str:
            return None
        try:
            data: bytes = base64.b64decode(base64_authorization_header)
            decoded_data: str = data.decode('utf-8')
        except (base64.binascii.Error, UnicodeDecodeError):
            return None
        return decoded_data
