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
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    check if a password is the same with the hashed pass.
    Args:
        hashed_password (bytes): password in bytes
        password (str): in string password

    Returns:
        bool: True or False
    """
    return bcrypt.checkpw(password.encode(), hashed_password)
