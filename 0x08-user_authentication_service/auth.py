#!/usr/bin/env python3
"""hash a password"""

import bcrypt


def _hash_password(password: str) -> bytes:
    """hash a password"""
    hash_pasw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash_pasw
