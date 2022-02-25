#!/usr/bin/env python3
"""auth class for authentication"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


class Auth:
    """Auth class to interact with the authentication database.
    """

    def _init_(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """save the user to the database
        using self._db and return the User object"""
        try:
            user = self._db.find_user_by(email=email)
            raise ValueError('User {} already exists'.format(email))
        except NoResultFound:
            hash_pwd = _hash_password(password)
            return self._db.add_user(email, hash_pwd)

    def valid_login(self, email: str, password: str) -> bool:
        """If it matches return True.
        In any other case, return False."""
        try:
            found_user = self._db.find_user_by(email=email)
            if bcrypt.checkpw(password.encode('utf8'),
                              found_user.hashed_password):
                return True
            else:
                return False
        except NoResultFound:
            return False

    def create_session(self, email: str) -> str:
        """ It takes an email string argument
        and returns the session ID as a string"""
        try:
            user = self._db.find_user_by(email=email)
            session_id = _generate_uuid()
            user.session_id = session_id
            self._db._session.commit()
            return session_id
        except NoResultFound:
            return None
el 

def _hash_password(password: str) -> bytes:
    """hash a password"""
    hash_pasw = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return hash_pasw


def _generate_uuid() -> str:
    """returns a string in uuid
    """
    return str(uuid4())
