#!/usr/bin/env python3
""" file that setup authentication for users
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    Module that handles authentication for user using Basic Authentication
    system.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        fetch the path and validate it
        Args:
            path (str): required path
            excluded_paths (List[str]): list of paths

        Returns:
            bool: True if valid or False if not
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        check the header for authorization scheme and authorize the user
        based on the data.

        Args:
            request (Type, optional): Flask request object. Defaults to None.

        Returns:
            str: string
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        returns the current user authenticated.

        Returns:
            TypeVar('User'): the authenticated user object
        """
        return None
