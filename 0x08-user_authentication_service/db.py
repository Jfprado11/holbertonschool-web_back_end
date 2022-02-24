#!/usr/bin/env python3
"""DB module
"""
from typing import Dict, TypeVar
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError, OperationalError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> TypeVar("User"):
        """adding a new user
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **args: Dict[str, str]) -> TypeVar("User"):
        """find a user depeding on the keywards
        """
        try:
            users = self._session.query(User).filter_by(**args).all()
        except OperationalError:
            raise InvalidRequestError
        if len(users) == 0:
            raise NoResultFound
        return users[0]

    def update_user(self, user_id: int, **args: Dict[str, str]) -> None:
        """update an user for its id
        """
        user = self.find_user_by(id=user_id)
        for arg, value in args.items():
            if arg not in user.__dict__.keys():
                raise ValueError
            setattr(user, arg, value)
            self._session.commit()
