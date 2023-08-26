#!/usr/bin/env python3
"""
    encrypt using bcrypt
"""
from bcrypt import hashpw, checkpw, gensalt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


def _hash_password(password: str) -> bytes:
    """
    hash a password using bcrypt

    Args:
        password (str): password to hash
    """
    return hashpw(password.encode('utf-8'), gensalt())


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        """ Initialize variables
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a new user

        Args:
            email (str): user email
            password (str): user password

        Returns:
            User: the new user object
        """
        try:
            obj = self._db.find_user_by(email=email)
            if obj:
                raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pass

        hashed_password: bytes = _hash_password(password)
        return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        valid user credentials for authorization

        Args:
            email (str): user email
            password (str): user password

        Returns:
            bool: true or false
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                if checkpw(password.encode('utf-8'), user.hashed_password):
                    return True
                return False

        except Exception:
            return False

    def _generate_uuid() -> str:
        """
        generates a unique UUID
        """
        return uuid4()
