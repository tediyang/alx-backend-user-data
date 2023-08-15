#!/usr/bin/env python3
""" File that create a Session Authentication Model
"""
from api.v1.auth.auth import Auth
from uuid import uuid4


class SessionAuth(Auth):
    """
    Implementation of Session Authentication Model

    Args:
        Auth (TypeVar('Auth')): the authentication model
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """
        creates a Session ID for a user.

        Args:
            user_id (str, optional): current user id. Defaults to None.

        Returns:
            str: returns the session id
        """
        if not user_id:
            return None
        if not isinstance(user_id, str):
            return None

        sess_id = uuid4()
        self.user_id_by_session_id[sess_id] = user_id
        return sess_id
