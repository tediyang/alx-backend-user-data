#!/usr/bin/env python3
"""
    encrypt using bcrypt
"""
from bcrypt import hashpw, gensalt


def _hash_password(password: str) -> bytes:
    """
    hash a password using bcrypt

    Args:
        password (str): password to hash
    """
    return hashpw(password.encode('utf-8'), gensalt())
