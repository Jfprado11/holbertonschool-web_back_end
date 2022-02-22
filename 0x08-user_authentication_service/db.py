"""DB module
"""
from typing import TypeVar
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
        property(self._session)
        new_user = User(email=email, hashed_password=hashed_password)
        self.__session.add(new_user)
        self.__session.commit()
        return new_user

    def find_user_by(self, **args):
        """find a user depeding on the keywards
        """
        property(self._session)
        query = "SELECT * FROM users "
        i = 0
        for arg, value in args.items():
            if i == 0:
                query += "WHERE "
            else:
                query += "AND "
            query += "{} == '{}'".format(arg, value)
            i += 1
        query += ";"
        users = None
        try:
            users = self.__session.query(
                User).from_statement(text(query)).all()
        except OperationalError:
            raise InvalidRequestError
        if len(users) == 0:
            raise NoResultFound
        return users[0]
