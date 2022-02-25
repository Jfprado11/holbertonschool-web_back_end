#!/usr/bin/env python3
"""hash a password"""

from typing import Union
import uuid
import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound

from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Method that checks if a user already exists
        """
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            passw = _hash_password(password)
            return self._db.add_user(email, passw)

    def valid_login(self, email: str, password: str) -> bool:
        """validate the password
        """
        try:
            user = self._db.find_user_by(email=email)
            return bcrypt.checkpw(password.encode('utf-8'),
                                  user.hashed_password)
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """creates a session id creates a sess
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except NoResultFound:
            return None


def _hash_password(password: str) -> bytes:
    """hash a password"""
    hash_pasw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash_pasw


def _generate_uuid() -> str:
    """returns a string in uuid
    """
    return str(uuid.uuid4())
