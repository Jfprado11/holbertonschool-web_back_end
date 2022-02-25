#!/usr/bin/env python3
"""Auth module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
from uuid import uuid4


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
        """Method that locates a user by email and checks
        the password
        """
        try:
            user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode(
                    'utf-8'), user.hashed_password):
                return True
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """Method that generate a session ID and store it in the database
        """
        try:
            user = self._db.find_user_by(email=email)
            self._db.update_user(user.id, session_id=_generate_uuid())
            return user.session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """Method that returns the user by session
        """
        try:
            user = self._db.find_user_by(session_id=session_id)
            return user
        except Exception:
            return None

    def destroy_session(self, user_id: int) -> None:
        """Method that updates the corresponding user's
        session ID to None
        """
        user = self._db.find_user_by(id=user_id)
        user.session_id = None


def _hash_password(password: str) -> bytes:
    """Function that returns a salted, hashed password,
    which is a byte string
    """
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed


def _generate_uuid() -> str:
    """Function that generates a new UUID"""
    new_id = str(uuid4())
    return new_id
