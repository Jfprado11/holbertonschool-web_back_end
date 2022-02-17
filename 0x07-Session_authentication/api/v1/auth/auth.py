#!/usr/bin/env python3
"""
handling the auth with a class
"""

from os import getenv
from typing import List, TypeVar
from flask import request


class Auth():
    """a class to check the basic auth to the paths
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """wether the path needs auth
        """
        if (path is None) or (excluded_paths is None or
                              len(excluded_paths) == 0):
            return True

        if path[-1] == '/':
            if path in excluded_paths:
                return False
            return True

        path_slash = path + '/'
        if path_slash in excluded_paths:
            return False
        return True

    def authorization_header(self, request=None) -> str:
        """check if the header recive the auth
        """
        if (request is None):
            return None

        if "Authorization" not in request.headers.keys():
            return None

        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar('User'):
        """returns the current log user
        """
        return None

    def session_cookie(self, request=None):
        """rturns teh value the cookie based on request
        """
        if request is None:
            return None

        _my_session_id = getenv("SESSION_NAME")
        value_cookie = request.cookies.get(_my_session_id)
        return value_cookie
