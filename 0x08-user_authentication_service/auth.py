#!/usr/bin/env python3
"""hash a password"""

import bcrypt
from db import DB
from sqlalchemy.orm.exc import NoResultFound
import uuid
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """returns the register user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError("User {} already exists".format(email))
        except NoResultFound:
            pwd = _hash_password(password)
            self._db.add_user(email, pwd)

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
        """creates a session id for a new user and store it in the database
        """
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            return session_id
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
