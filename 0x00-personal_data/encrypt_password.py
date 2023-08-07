#!/usr/bin/env python3
"""
Encrypting password using bcrypt
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    encrypt the password with bcrypt
    Args:
        password (str): the provided password

    Returns:
        str: the byte encrypted data
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())
